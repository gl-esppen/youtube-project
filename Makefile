install:
	pip install -r requirements.txt
	python main/manage.py migrate
	python main/manage.py createsuperuser
	python main/manage.py collectstatic

migrations:
	python main/manage.py makemigrations
	python main/manage.py migrate

run:
	python main/manage.py runserver