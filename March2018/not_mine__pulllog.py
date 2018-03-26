#!/usr/bin/python
## Script  generates the list of user those requested simple binds per day
## Reports is based on dated access file data
## Author : Santosh Kumar Swarnkar
## Date: 11 Nov 2017
import glob
import time
import re
import sys
import subprocess
p = subprocess.Popen(["/oem1/home/odcagent/scripts/dsadm-show-access-log"],stdout=subprocess.PIPE)
p.wait()
log_time = time.strftime('%d/%m/%y:%H:%M:%S', time.localtime())
#print 'em_result= %s' %(log_time)
uid_count = {}
with open('/u01/app/oracle/product/ds/ora-nis-nl/txnlogs/show-access-log.log', 'r') as line_of_files:
        for line in line_of_files:
                line = line.split('BIND')
                if len(line) > 1:
                        list = line[1]
                        #print list
                        m = re.search('uid=(\w+)', list)
                        if m:
                                string_list = (m.group(1))
                                uid_list = string_list.split()
                                #print uid_list
                                for uid in uid_list:
                                        if uid in uid_count:
                                                uid_count[uid] = uid_count[uid] + 1
                                        else:
                                                uid_count[uid] = 1
for key in uid_count:
        print 'em_result= %s %s %s %s %d'  %(log_time,"|", key, "|", uid_count[key])
total = sum(uid_count.values())
print 'em_result= %s %s %s %s %d' %(log_time, "|",'Total',"|",total)
