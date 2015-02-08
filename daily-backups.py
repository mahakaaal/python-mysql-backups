#!/usr/bin/env python
import ConfigParser
import os
import time,datetime
import subprocess, shlex


username = "deploy"
password = "*******"
hostname = "localhost"
IGNOREDB = ['icinga_web', 'information_schema', 'performance_schema', 'test', 'mysql']
MYSQL_BCKDIR ="/BACKUPS/mysql/daily"

def datetime_now_in_string():
    return datetime.datetime.now().strftime("%b-%d-%Y_%I%M%p")

DATE_FILENAME = datetime_now_in_string()
DATE = datetime.datetime.now().strftime('%b-%d-%Y')
DATE_FOLDER = os.path.join(MYSQL_BCKDIR, DATE)

if not os.path.exists(DATE_FOLDER):
   os.makedirs(DATE_FOLDER)

# Get a list of databases with :
database_list_command="mysql --silent -N -e 'show databases'"
database_list = [line.strip() for line in os.popen(database_list_command).readlines() if line.strip() not in IGNOREDB]
for database in database_list:
    username1, sitename =  database.split('_', 1)

    filename = DATE_FOLDER+"/daily_"+username1+"_"+sitename+"_"+DATE_FILENAME+".sql"

    pipe = subprocess.Popen("mysqldump -e --opt --skip-lock-tables  --skip-extended-insert -c %s | gzip > %s.gz" % (database, filename), shell=True)
    pipe.wait()
    
