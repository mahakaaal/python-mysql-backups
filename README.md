# python-mysql-backups
Backup scripts to backup mysql databases using Python



#Daily Backups

This script makes the backup of all mysql databses in individual folders with date

I usually run it every few hours like this

`21 1,8,11,15,19,21 * * 0,1,2,3,4,5,6 /usr/bin/python /cronjobs/daily-backups.py`

It creates folders like this

```/BACKUPS/mysql/daily/Feb-07-2015/daily_php_site1_Feb-07-2015_0321PM.sql.gz
/BACKUPS/mysql/daily/Feb-07-2015/daily_php_site1_Feb-07-2015_0721PM.sql.gz
/BACKUPS/mysql/daily/Feb-07-2015/daily_php_site1_Feb-07-2015_0821AM.sql.gz
/BACKUPS/mysql/daily/Feb-07-2015/daily_php_site1_Feb-07-2015_0921PM.sql.gz
