#!/usr/bin/make

include dev.env

run-docker-compsoe-dev:
	docker compose -f docker-compose.app.yaml up -d

stop-docker-compsoe-dev:
	docker compose -f docker-compose.app.yaml down

run-database:
	docker compose -f docker-compose.app.yaml up -d db

stop-database:
	docker compose -f docker-compose.app.yaml down db

run-app:
	uvicorn app.main:app --reload --port $(APP_PORT)
