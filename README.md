<<<<<<< HEAD
![logo](https://github.com/ChicoState/WhatToWatch/blob/master/Logo.JPG)
=======
![logo](https://github.com/ChicoState/WhatToWatch/blob/master/Logo.JPG) 
>>>>>>> e2d40d6... Update README.md
# What To Watch [![Build Status](https://travis-ci.com/chodges7/WhatToWatch.svg?branch=master)](https://travis-ci.com/chodges7/WhatToWatch)

## Developers
* Product Owner: Christian Hodges, [chodges7](https://github.com/chodges7)
* Scrum Master: Lukas Pecson, [lpecson](https://github.com/lpecson)
* Developer: Vidit Dhaka, [vdhaka](https://github.com/vdhaka)

## Entrepreneurs
* Matthew Martell
* Nate Rehm
* Nicholas Whitley

## Getting started
### Dependancies that you need:
* pip
* python3

### How to get it running
* boot up the virtual enviornment by running the command  
Mac: ```source bin/activate```  
Windows: ```whattowatch/bin/activate```  
* next install the requirements  
```pip install -r requirements.txt```
* there also might be some migrations that need to happen in the database so run this command  
Mac: ```python3 manage.py migrate```  
Windows: ```py manage.py migrate```  
* finally, boot up the local server  
Mac: ```python3 manage.py runserver```  
Windows: ```py manage.py runserver```

The website should be avalible on the local host website [http://127.0.0.1:8000](http://127.0.0.1:8000)
