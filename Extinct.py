# _*_ coding:utf-8 _*_
#version 1.0
#ChangeLog
#added logging with time/date stamp
#version 1.0.0.1
#added error logging 
#minor reformating 

#Imports
import os
import shutil
import time
import logging
from distutils.dir_util import copy_tree
#Strips permisions on file if needed
os.chmod('filename', 0o777)


#logging
logging.basicConfig(
filename='...\\backup.log\\' ,
level=logging.DEBUG
)

#Appends Date/Time to a text file
logging.info("%s %s"%(time.strftime("%a, %d %b %Y %H:%M:%S"), 'Files have been backed up'))

try:
  #Copy folder to new location
  fromDirectory = "SRC"
  toDirectory = "DST"

  
  #Copy Actions
  copy_tree("SRC" , "DST"  )
  
except:
    logging.exception('Seems something is broken')
