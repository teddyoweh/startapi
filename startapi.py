from numpy import str_
import huepy
from huepy import red
from huepy import green
from huepy import yellow
import argparse
import requests, zipfile, io
import shutil
import os
 
# - @author: teddyoweh
# - @website: https://teddyoweh.net:
# - @github: https://github.com/teddyoweh
# - @twitter: https://twitter.com/tedddyoweh
# - @mail: teddy@teddyoweh.net
# - @message: reach out for contributions or questions ;)!

 
    

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
       
        if self.framework.lower() == 'flask':
            print(f'-[#] Building {yelapp} FLASK API CodeBase')
            self._build('flaskboilerplate ')
            print(f'-[+] Building {yelapp} FLASK API CodeBase Complete')
            
            
            
             
            
        elif self.framework.lower() =='fastapi': 
            print(f'-[#] Building {yelapp} FASTAPI CodeBase')
            self._build('fastapiboilerplate')
            print(f'-[+] Building {yelapp} FASTAPI CodeBase Complete')
            
            
    def args(self):
        parser = argparse.ArgumentParser("startapi")

        parser.add_argument("--a", dest='appname', help="API Service Name .", type=str)
        parser.add_argument("--f", dest='framework',help="API Framework to use [Flask, FastAPI].",default='Flask', type=str)
        args = parser.parse_args()
        self.apiname=args.appname
        self.framework= args.framework
    def _build(self,name):
        self.mainurl='https://github.com/teddyoweh/{}/archive/refs/heads/main.zip'.format(name)
        
        r = requests.get(self.mainurl)
        z = zipfile.ZipFile(io.BytesIO(r.content))
        z.extractall(self.apiname)
        os.chdir(self.apiname)
      
        newname = '{}-main'.format(name)
        nedwname = self.apiname
        bix =f'ren {newname} {nedwname}'
        print(bix)
        os.system(bix)
     
        
 

        
    
        
        
        
startAPI()