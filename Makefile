env = dev

clean:
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf

run:
	@python run.py

# -- test

check-debugger:
	@find pydojo -type f -exec egrep -iH "set_trace" {} \+ && echo "Ooops! Found 1 set_trace on your source code!" && exit 1 || exit 0

test-travis: clean check-debugger
	py.test pydojo

test: SHELL:=/bin/bash
test: clean
	py.test pydojo --pdb

test-matching: SHELL:=/bin/bash
test-matching: clean
	py.test pydojo -k $(test) --pdb

coverage: SHELL:=/bin/bash
coverage: clean
	py.test --cov-config .coveragerc --cov pydojo pydojo --cov-report term-missing

# -- instalation and execution

.env: SHELL:=/bin/bash
.env: required-env
	@if [ $(env) == "dev" -a ! -e .env ]; then cp contrib/env-sample .env; fi
	@if [ $(env) == "test" -a ! -e .env ]; then cp contrib/env-test .env; fi

required-env: SHELL:=/bin/bash
required-env:
	@if [ -z $(env) ]; then echo "env paramether is not set"; exit 1; fi
	@if [ $(env) != "prod" -a $(env) != "dev" -a $(env) != "test" ]; then echo "env paramether is not a valid value: dev, prod or test"; exit 1; fi

requirements: SHELL:=/bin/bash
requirements: required-env
	@if [ $(env) == "prod" ]; then pip install -r requirements.txt; fi
	@if [ $(env) == "dev" ]; then pip install -r requirements/development.txt; fi
	@if [ $(env) == "test" ]; then pip install -r requirements/development.txt; fi

# -- database management and execution

initialize-db:
	@python manage.py db init

create-migrations:
	@python manage.py db migrate

apply-migration:
	@python manage.py db upgrade

revert-migration:
	@python manage.py db downgrade

postgresql-docker-start:
	echo "Starting postgresql with docker..."
	@sudo ./contrib/start_postgresql_docker.sh

