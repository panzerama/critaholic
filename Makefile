#!make

include .env

test:
	env

up:
	docker-compose up -d

dbshell:
	mysql -h 127.0.0.1 -P 3306 -u $(MYSQL_USER) -p$(MYSQL_PASSWORD) $(MYSQL_DATABASE)

migrate: up
	python manage.py migrate	
