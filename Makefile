### Configure paths. ###
PROJECT_PATH := $(CURDIR)
APP_PATH := $(CURDIR)/comprendre
ENV_PATH := $(CURDIR)/virtual_env
PYTHON := $(ENV_PATH)/bin/python

### Shell configure. ###
# Enable colors for ouput. Use echo with -e.
RED=\033[0;31m
ORANGE=\033[0;33m
NC=\033[0m

### Configure virtual environment. ###
# Shortcut to set env command before each python cmd.
VENV = source $(ENV_PATH)/bin/activate && source $(PROJECT_PATH)/.comp_env

# Config is based on two environment files, initalized here.
virtualenv: .comp_env $(ENV_PATH)/bin/activate

$(ENV_PATH)/bin/activate:
	virtualenv -p /usr/local/bin/python3 --distribute $(ENV_PATH)

### Project installation. ###
# Install python requirements.
pip: virtualenv
	$(VENV) && cd $(APP_PATH) && pip install -r $(APP_PATH)/requirements.txt;

.comp_env:
	cp .comp_env_template .comp_env

install: pip

### Migrations. ###
migrate: virtualenv
	$(VENV) && $(PYTHON) $(APP_PATH)/manage.py migrate

migrations: virtualenv
	$(VENV) && $(PYTHON) $(APP_PATH)/manage.py makemigrations

showmigrations: virtualenv
	$(VENV) && $(PYTHON) $(APP_PATH)/manage.py showmigrations

### Shortcuts ###
clean:
	find . -name '*.pyc' -delete

serve_django: virtualenv
	$(VENV) && $(PYTHON) $(APP_PATH)/manage.py runserver $$COMP_PORT

createsuperuser: virtualenv
	$(VENV) && $(PYTHON) $(APP_PATH)/manage.py createsuperuser

shell: virtualenv
	$(VENV) && $(PYTHON) $(APP_PATH)/manage.py shell

### Tests ###
TEST_CMD = $(PYTHON) $(APP_PATH)/manage.py test

# Launch tests.
test:
	$(VENV) && $(TEST_CMD) -s comprendre.users comprendre.meetings

# Launch a specific test.
test_unique:
	$(VENV) && $(TEST_CMD) -x -s comprendre/comprendre/meetings/v1/tests/test_views.py:MeetingViewTestCase.test_conference_pagination

### Code linting. ###
PYLINT := pylint --load-plugins pylint_django $(APP_PATH)/comprendre/users $(APP_PATH)/comprendre/meetings

pylint: virtualenv
	$(VENV) && $(PYLINT)
