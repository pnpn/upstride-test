start:
	@docker-compose -f docker/docker-compose.yml --project-directory . up -d --build
stop:
	@docker-compose -f docker/docker-compose.yml --project-directory . down
restart: stop start
