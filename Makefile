install:
	pip install -r requirements.txt

migrations:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate
superuser:
	python manage.py createsuperuser
collectstatic:
	python manage.py collectstatic

serve:
	python3 manage.py runserver

test:
	python manage.py test

.PHONY: set_env_vars