# What is Django?

Django - is a old wild western fiction film from 1960's.
This repository contains all my experimental work with web framework.

# Running Guide

Okay, it's not so difficult. Just install all packages from
`requirements.txt` by using:
```python
pip install -r requirements.txt
```
Also, don't forget setup the shell variables. You can do it by `.env` with next content:
```bash
DADATA_API_KEY=your-api-key-there
REDIS_URL=redis://localhost:6379/0 # or another URL

TELEGRAM_BOT_TOKEN=you-bot-token-api
```

Okay, good. Now you should setup redis server as a brocker for Celery (idk, should i use another alternatives, but in tutorials, mosly, redis is used):
```bash
# Run redis or another brocker
redis-server
```

Setup celery, by using this:
```bash
# Celery
celery -A stts_site worker --loglevel=info
```

And run the server!
```bash
# Run the project in dev mode.
py manage.py runserver
```

## NixOS

For nix users you would be use `shell.nix` as dev environment.
Just use `nix-shell` or something else what can virtualize your's env :woozy_face:.

## TODO:

Well, i don't think it is important, but `run.sh` should be writed as universal solution for the manage project (i don't like python scripts lol).