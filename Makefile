migrate:
	python manage.py makemigrations;\
	python manage.py migrate

installd:
	pip install -r requirements/dev.txt

installp:
	pip install -r requirements/prod.txt

run:
	python manage.py runserver

.PHONY: start migrate installd
