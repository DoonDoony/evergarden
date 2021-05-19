# Evergarden: HTTP API that converts Markdown to HTML

**The project name 'evergarden' is taken from the
animation [Violet Evergarden](https://www.netflix.com/kr-en/title/80182123)*

## 🙇‍♂️ Built with

- [Serverless Framework](https://github.com/serverless/serverless)
- [FastAPI](https://github.com/tiangolo/fastapi)

## 🎁 Prerequisites

- Python 3.8.x
- [Poetry](https://github.com/python-poetry/poetry)
- NodeJS (ANY)
- (Optional) [direnv](https://github.com/direnv/direnv)
- (Optional) [gitmoji](https://github.com/carloscuesta/gitmoji-cli)

## 🔖 How to start

```bash
# 🐍 Setup Python virtualenv
$ pyenv virtualenv evergarden 3.8.x

# 🐍 Or, use Anaconda
$ conda create --no-default-packages --name evergarden python=3.8.x

# Use virtualenv automatically (Anaconda)
$ echo 'layout anaconda evergarden' > .envrc

# Use virtualenv automatically (pyenv-virtualenv)
$ echo 'export PYENV_VIRTUAL_ENV=evergarden' > .envrc

# Install NPM Packages
$ npm install

# If there is no "Poetry" ...
$ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -

# Install Python dependencies
$ poetry install --no-root

# Setup pre-commit hooks
$ poetry run pre-commit install

# Setup .env file
$ cp .env.sample .env
$ cp .env.sample .env.dev

# 🚀 Run
$ make runserver

# 🚀 Deploy
$ make <stage>-deploy

# e.g,.
$ make dev-deploy
```

## ✅ Todo
- [ ] Wrap project into Docker
