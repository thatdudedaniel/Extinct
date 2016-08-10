# _*_ coding:utf-8 _*_
#version 1.0
#ChangeLog
#added logging with time/date stamp
#added backup of the writting folder

#version 1.0.0.1
#added backup of outlook files, there big so the script will  take a while to run
#close any programs that may be using files you are trying to backup or the script will error out



#Imports
import os
import shutil
import time
from distutils.dir_util import copy_tree
#Strips permisions on file
os.chmod('U:\\Stylesheets\\XML\\Testing\\Bureau manuals\\Master_Main_Mapping_ RevB.pdf', 0o777)


#logging
import logging

logging.basicConfig(
filename='U:\\Stylesheets\\backup.log\\' ,
level=logging.INFO,
)

logging.info("%s %s"%(time.strftime("%a, %d %b %Y %H:%M:%S"), 'Files have been backed up'))

#Copy folder to new location
fromDirectory = "C:\\Users\\daniel\\Documents\\Testing\\"
toDirectory = "U:\\Stylesheets\\XML\Testing\\"
#Second Folder
fromFolder = "C:\\Users\daniel\\Desktop\\Random XMl"
toFolder = "U:\\Stylesheets\\XMl\\RandomXML\\"
#Writing Folder
fromLocation  = "C:\\Users\daniel\\Desktop\\Writing\\"
ToLocation ="U:\\Writing\\"
#outlook Archive PST
Fromarchive ="C:\\Users\\daniel\\Documents\\Outlook Files\\"
Toarchive ="U:\\Outlook\\"
#Outlook Data Files
Fromoutlook ="C:\\Users\\daniel\\AppData\\Local\\Microsoft\\Outlook\\"
Tooutlook ="U:\\Outlook\\"

#Copy Actions
copy_tree("C:\\Users\\daniel\\Documents\\Testing\\" , "U:\\Stylesheets\\XML\Testing\\"  )

copy_tree("C:\\Users\daniel\\Desktop\\Random XMl", "U:\\Stylesheets\\XMl\\RandomXML\\")

copy_tree("C:\\Users\daniel\\Desktop\\Writing\\",  "U:\\Writing\\")

copy_tree("C:\\Users\\daniel\\Documents\\Outlook Files\\", "U:\\Outlook\\")

copy_tree("C:\\Users\\daniel\\AppData\\Local\\Microsoft\\Outlook\\", "U:\\Outlook\\")
