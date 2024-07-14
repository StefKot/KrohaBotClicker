# KrohaBotClicker
This is a small test clicker for the site [Всё для Крохи](https://www.vsekroham.ru/).
![image](https://github.com/user-attachments/assets/1d424387-a8e5-4162-8def-ca71ac077712)

It has 4 pages:
- clicker
- store
- raiting
- profile

##  Makefile
``` make
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
```
