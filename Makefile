#!make

test:
	env

up:
	./envfile
	docker-compose up -d

dbshell:
	./envfile
	mysql -h 127.0.0.1 -P 3306 -u $(MYSQL_USER) -p$(MYSQL_PASSWORD) $(MYSQL_DATABASE)

migrate: up
	python manage.py migrate	
