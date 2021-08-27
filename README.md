# PyCon TW Archived Websites

## Usage

To get the specific pycon web, try typing the command

```
    python3 main.py -y year --base [Your LOCAL SERVER HOST]
```

where year can just in 2016 - 2020

## Setup Development Environment
- Installing dependencies
```
    pipenv install
```

## Build Testing Server

### Prerequsite
- npx

For serving scraped static pages, you could execute following command in the root foler of this project:
```bash
npx serve
```

## Run Local Server

```
docker-compose -f docker-compose-dev.yml up --build -d
```
