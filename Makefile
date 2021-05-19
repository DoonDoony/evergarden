.PHONY: runserver
runserver:
	poetry run uvicorn evergarden.main:app --reload

.PHONY: dev-deploy
dev-deploy:
	npx sls deploy --stage dev
