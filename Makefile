.PHONY: migrate installdev

migrate:
	python manage.py makemigrations
	python manage.py migrate

installdev:
	pip install -r requirements/dev.txt

installprod:
	pip install -r requirements/prod.txt
