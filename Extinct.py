# _*_ coding:utf-8 _*_
#version 1.0
#ChangeLog
#added logging with time/date stamp



#Imports
import os
import shutil
import time
from distutils.dir_util import copy_tree
#Strips permisions on file if needed
os.chmod('filename', 0o777)


#logging
import logging

logging.basicConfig(
filename='Location\\backup.log\\' ,
level=logging.INFO,
)

#Appends Date/Time to a text file
logging.info("%s %s"%(time.strftime("%a, %d %b %Y %H:%M:%S"), 'Files have been backed up'))

#Copy folder to new location
fromDirectory = "SRC"
toDirectory = "DST"


#Copy Actions
copy_tree("SRC" , "DST"  )
