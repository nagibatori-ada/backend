DOCKER_COMPOSE_FILE=docker-compose.yml

DOCKER_COMPOSE=docker-compose
DOCKER_BUILDKIT_FLAG=1


.PHONY: build up logs stop fclean


all: build up logs

build:
	DOCKER_BUILDKIT=$(DOCKER_BUILDKIT_FLAG) $(DOCKER_COMPOSE) --file=$(DOCKER_COMPOSE_FILE) build

up:
	$(DOCKER_COMPOSE) --file=$(DOCKER_COMPOSE_FILE) up -d

logs:
	$(DOCKER_COMPOSE) --file=$(DOCKER_COMPOSE_FILE) logs -f

stop:
	$(DOCKER_COMPOSE) --file=$(DOCKER_COMPOSE_FILE) stop

fclean:
	$(DOCKER_COMPOSE) --file=$(DOCKER_COMPOSE_FILE) down -v
