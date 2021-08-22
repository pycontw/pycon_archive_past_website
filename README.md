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

Here is the reference I made. [Go!!](https://mozixreality.github.io/Blog/featured/D20210503)

## Run Local Server

```
docker-compose -f docker-compose-dev.yml up --build -d
```
