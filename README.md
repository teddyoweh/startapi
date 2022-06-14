# StartApi
 A command line interface aplication to create boilerplate code for developing APIs Using either of the two most popular python modules, Flask and FastAPI 

## Installation
```sh
$ pip install startapi
```
## Usage
```py 
from startapi import startapi
startapi()
```
##### Save the python file, eg (makeapi.py)
### Running

### Using Arguments 
```sh
usage: startapi [-h] [--a APPNAME] [--f FRAMEWORK]

options:
  -h, --help     show this help message and exit
  --a APPNAME    API Service Name .
  --f FRAMEWORK  API Framework to use [Flask, FastAPI].
```


```sh
$ python3 makeapi.py --a myapi --f fastapi
```
