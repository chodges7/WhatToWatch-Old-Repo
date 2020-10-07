# What To Watch [![Build Status](https://travis-ci.com/chodges7/WhatToWatch.svg?branch=master)](https://travis-ci.com/chodges7/WhatToWatch)

## Developers
* Product Owner: Christian Hodges, [chodges7](https://github.com/chodges7)
* Scrum Master: Lukas Pecson, [lpecson](https://github.com/lpecson)
* Developer: Vidit Dhaka, [vdhaka](https://github.com/vdhaka)

## Entrepreneur
* Matthew Martell
* Nate Rehm
* Nicholas Whitley

## Getting started
### Dependancies that you need:
* pip
* python3

### How to get it running
* boot up the virtual enviornment by running the command
```source bin/activate```
* next install the requirements
```pip install -r requirements.txt```
* there also might be some migrations that need to happen in the database so run this command
```python3 manage.py migrate```
* finally, boot up the local server
```python3 manage.py runserver```

The website should be avalible on the local host website [http://127.0.0.1:8000](http://127.0.0.1:8000)
