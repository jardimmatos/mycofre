COMMAND = python manage.py

collectstatic:
	$(COMMAND) collectstatic

run:
	$(COMMAND) runserver

first-migrations:
	$(COMMAND) makemigrations && \
	$(COMMAND) migrate users && \
	$(COMMAND) migrate cofre && \
	$(COMMAND) migrate sites && \
	$(COMMAND) migrate

migrations:
	$(COMMAND) makemigrations && $(COMMAND) migrate

super:
	$(COMMAND) createsuperuser

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  run             Para execução do runserver"
	@echo "  first-migrations Para gerar e aplicar migrações iniciais"
	@echo "  migrations  	 Para gerar e aplicar migrações"
	@echo "  collectstatic   Para obter os arquivos estáticos"
	@echo "  super           Criar um superusuário"
