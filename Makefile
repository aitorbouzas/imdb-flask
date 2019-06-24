# SERVER
server.d:
	docker-compose up -d server
server.install:
	docker-compose run --rm server pip install -r requirements.txt --user --upgrade --no-warn-script-location
server.start:
	docker-compose up server
server.stop:
	docker-compose stop
server.logs:
	tail -f server.log
server.test:
	docker-compose run --rm testserver
server.flake8:
	docker-compose run --rm server bash -c "python -m flake8 ./src ./test ./scrap"

# FRONTEND
web.d:
	docker-compose -d up web
web.start:
	docker-compose up web

# DATABASE
database.connect:
	docker-compose exec postgres psql -Upostgres
database.init:
	docker-compose run --rm server python src/manage.py db init
database.migrate:
	docker-compose run --rm server python src/manage.py db migrate
database.upgrade:
	docker-compose run --rm server python src/manage.py db upgrade
database.downgrade:
	docker-compose run --rm server python src/manage.py db downgrade

# SCRAP
scrap.scrap:
	docker-compose run --rm server python scrap/scrap.py
