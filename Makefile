install-venv:
	python -m venv ve
	ve/bin/python3 -m pip install -r requirements.txt

run:
	cd django/krohasite; python3 manage.py runserver

run-krohabot:
	cd clicker/django/krohasite/
	daphne krohasite.asgi:application

collect-static:
	cd django/krohasite; python3 manage.py collectstatic

config:
	 nano /etc/nginx/sites-available/default
