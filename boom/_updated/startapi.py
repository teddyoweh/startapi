from numpy import str_
import huepy
from huepy import red
from huepy import green
from huepy import yellow
import argparse


 
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
        
        if self.framework == 'Flask':self._buildflask()
        else: self.buildfastapi()
            
    def args(self):
        parser = argparse.ArgumentParser("startapi")

        parser.add_argument("--a", dest='appname', help="API Service Name .", type=str)
        parser.add_argument("--f", dest='framework',help="API Framework to use [Flask, FastAPI].",default='Flask', type=str)
        args = parser.parse_args()
        self.apiname=args.appname
        self.framework= args.framework
 
    def _buildflask(self):
        os.mkdir(self.apiname)
        os.mkdir(self.apiname+'/'+'api')
        os.mkdir(self.apiname+'/'+'app')
        os.mkdir(self.apiname+'/'+'config')
        os.mkdir(self.apiname+'/'+'tests')
        open(self.apiname+'/run.py','w').write(self.runpy)
        print('flask')
        pass
 
    def _buildfastapi(self):
        print('fastapi')
    def _codes(self):
        
        self.runpy ="""from app import create_app\napp = create_app('config.development')\nif __name__ == '__main__':\tapp.run()
        """
    def __repr__(self):
        pass
        
    
        
        
        
startAPI()