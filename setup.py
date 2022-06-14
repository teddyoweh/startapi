from setuptools import setup
import pathlib
 
HERE = pathlib.Path(__file__).parent

 
README = (HERE / "README.md").read_text()

setup(
  name = 'startapi',         
  packages = ['startapi'],    
  version = '0.1', 
  description = 'A command line interface aplication to create boilerplate code for developing APIs',    
  long_description=README,
  long_description_content_type="text/markdown",     
  license='MIT',       

  author = 'teddyoweh',                    
  author_email = 'teddy@teddyoweh.net',       
  url = 'https://github.com/teddy/startapi',   
  download_url = 'https://github.com/teddyoweh/startapi/archive/refs/tags/api.zip',     
  keywords = ['startapi', 'FastAPI', 'FlaskAPI','API BOILERPLATE'],    
 
  classifiers=[
    'Development Status :: 3 - Alpha',       
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',    
    'Programming Language :: Python :: 3',       
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)