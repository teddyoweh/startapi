# Change Log

## [2.0.2] 2022-06-06
### Improvements

- Use generated version
  - Timestamp: `2022-06-06 13:25`
  - Build ID: `f365bee7-40fc-4fe2-819c-086a7e06c88b`

## [2.0.1] 2022-06-06

- Tag latest `manual` coded version 

## [2.0.0] 2022-01-17
### Improvements

- Dependencies update (all packages) 
  - Flask==2.0.2 (latest stable version)
  - flask_wtf==1.0.0
  - jinja2==3.0.3
  - flask-restx==0.5.1

## [1.0.7] 2021-09-16
### Improvements

- Rename model `User` to `Users` to avoid name conflict with ORACLE DBMS
  - Impacted files:
    - `app/{model.py, util.py, viewws.py}`  

## [1.0.6] 2021-09-16
### Improvements & Fixes

- Dependencies update (all packages) 
  - Flask==2.0.1 (latest stable version)
- Better Code formatting
- Improved Files organization
- Optimize imports
- Docker Scripts Update
- Gulp Tooling  (SASS Compilation)
  - Minor fixes
- UI: Pixel Lite (free version)  

## [1.0.5] 2021-05-16
### Dependencies Update

- Freeze used versions in `requirements.txt`
    - jinja2 = 2.11.3

## [1.0.4] 2021-03-18
### Improvements

- Freeze used versions in `requirements.txt`
    - flask_sqlalchemy = 2.4.4
    - sqlalchemy = 1.3.23

## [1.0.3] 2021-01-01
### Improvements

- 2021-01-01 - Registration
    - Hide the form on success

- 2020-06-28 - Update the UI Kit
    - Quick UI KIt by Webpixels

- 2020-06-22 - Added HEROKU support. Impacted files:
    - runtime.txt - Bump the Python version to 3.6.10
    - README added new section for HEROKU deployment

## [1.0.2] 2020-06-18
### Improvements

- The password storage is now Bcrypt.hashed
- Added deploy scripts: Docker, Gunicorn
- Added `.env`
- Added `python-decouple` in `requirements.txt`
- Update Sample UI Kit - [Neumorphism UI](https://themesberg.com/product/ui-kits/neumorphism-ui) by Themesberg

## [1.0.1] 2020-05-30
### Improvements

- Update Licensing information
- Add CHANGELOG.md to track all changes
- Minor update in README

## [1.0.0] 2020-02-07
### Initial Release
