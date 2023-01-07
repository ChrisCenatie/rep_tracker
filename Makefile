migrations:
	docker-compose run --rm rep-tracker bash -c "python ./manage.py migrate"

create_superuser:
	docker-compose run --rm rep-tracker bash -c "python ./manage.py createsuperuser"

dev_server:
	docker-compose run --rm --service-ports rep-tracker

runtests:
	docker-compose run --rm rep-tracker bash -c "python ./manage.py test"

.PHONY: migrations create_superuser dev_server runtests
