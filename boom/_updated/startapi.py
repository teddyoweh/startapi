from numpy import str_
import huepy
from huepy import red
from huepy import green
from huepy import yellow
import argparse
import requests, zipfile, io
import shutil
 
# - @author: teddyoweh
# - @website: https://teddyoweh.net:
# - @github: https://github.com/teddyoweh
# - @twitter: https://twitter.com/tedddyoweh
# - @mail: teddy@teddyoweh.net
# - @message: reach out for contributions or questions ;)!
import os
 
    

class startAPI:
    def __init__(self):
        self.args()
        self._codes()
        self.appname='STARTAPI'
        
        self.credits= """
        ==========================================================
        | @author: teddyoweh                                     | 
        | @website: https://teddyoweh.net:                       | 
        | @github: https://github.com/teddyoweh                  | 
        | @twitter: https://twitter.com/tedddyoweh               | 
        | @mail: teddy@teddyoweh.net                             | 
        | @message: reach out for contributions or questions ;)! | 
        ==========================================================
        """
        print('                             # {} # '.format(self.appname))
        print(self.credits)
        self.dest= os.getcwd()
        self.src='template'
        print('\n')
        yelapp= yellow(self.apiname)
        print(f'-[#] Building {yelapp} API CodeBase')
        if self.framework == 'Flask':
           
            self._buildflask()
            os.chdir(self.apiname)
            os.system('dir')
            newname = 'flaskboilerplate-main'
            nedwname = self.apiname
            bix =f'ren {newname} {nedwname}'
            print(bix)
            os.system(bix)
             
            
        else: self.buildfastapi()
        
            
    def args(self):
        parser = argparse.ArgumentParser("startapi")

        parser.add_argument("--a", dest='appname', help="API Service Name .", type=str)
        parser.add_argument("--f", dest='framework',help="API Framework to use [Flask, FastAPI].",default='Flask', type=str)
        args = parser.parse_args()
        self.apiname=args.appname
        self.framework= args.framework
 
    def _buildflask(self):
        self.mainurl='https://github.com/teddyoweh/flaskboilerplate/archive/refs/heads/main.zip'
        
        r = requests.get(self.mainurl)
        z = zipfile.ZipFile(io.BytesIO(r.content))
        z.extractall(self.apiname)
        
 
    def _buildfastapi(self):
        print('fastapi')
    def _codes(self):
        
        self.runpy ="""from app import create_app\napp = create_app('config.development')\nif __name__ == '__main__':\tapp.run()
        """
    def __repr__(self):
        pass
        
    
        
        
        
startAPI()