.PHONY: runserver
runserver:
	poetry run uvicorn evergarden.main:app

.PHONY: dev-deploy
dev-deploy:
	npx sls deploy --stage dev
