#!/usr/bin/python

import threading
import time
import psycopg2

exitFlag = 0
connections = [{'server':'dw-rsm-010','db':'dwrsm010'}]
for connection in connections:
        print "Starting connection string "
        conn_string = "host='%s.cv63a8urwqge.us-east-1.redshift.amazonaws.com' dbname='%s' user='dw_rs_admin' password='Adm1n001' port='8192'" % (connection['server'],connection['db'])

for i in range(0,2):
         try:
                 print "Getting conn varialble "
                 conn = psycopg2.connect(conn_string)
         except:
                 continue
         break

cursor = conn.cursor()
conn.set_isolation_level( psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT )


class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print "Starting " + self.name
        if self.threadID == 1:
                print "I am polling thread"
                connect_db(self.name, self.counter, 5)
        if self.threadID == 2:
                print "I am deep copy thread to print time"
                deep_copy(self.name, self.counter, 5)
        print "Exiting " + self.name

def print_time(threadName, delay, counter):
    while (exitFlag == 0):
        print "%s:exitFlag " % (exitFlag)
        if exitFlag:
            thread.exit()
        time.sleep(delay)
        print "%s:Inside wile loop %s" % (threadName, time.ctime(time.time()))
        counter -= 1

def connect_db(threadName, delay, counter):
                cursor.execute("set query_group to 'superuser'")
                print "Inside connect_db"
                while (exitFlag == 0):
                        print "%s:exitFlag " % (exitFlag)
                        if exitFlag:
                                        thread.exit()
                        time.sleep(delay)
                        cursor.execute("select 'thread13_try2'||sysdate")
                        records = cursor.fetchall()
                        if cursor.rowcount==0:
                                print "Nothing to CANCEL in %s database" % connection['db']
                        else:
                                for pid in records:
                                         print 'On database: '+connection['db']+", sysdate : " + str(pid[0])
                print "%s:exitFlag " % (exitFlag)

def deep_copy(threadName, delay, counter):
                print "Inside deep copy module "
                cursor.execute("set query_group to 'superuser'")
                cursor.execute("select sysdate")
                records = cursor.fetchall()
                if cursor.rowcount==0:
                        print "Nothing to CANCEL in %s database" % connection['db']
                else:
                        for pid in records:
                                print 'On database: '+connection['db']+", sysdate : " + str(pid[0])
                print "Inside the deep_copy module.. waiting "
                time.sleep(12);
                try:
                        conn.set_isolation_level( psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT )
                        print "Executing insert into booker.vacuum_d_daily_buyer_effectiveness (select * from booker.d_daily_buyer_effectiveness)"
                        cursor.execute("insert into booker.vacuum_d_daily_buyer_effectiveness (select * from booker.d_daily_buyer_effectiveness)")
#                       print "Executing create table booker.vacuum_ddbe ( like booker.d_daily_buyer_effectiveness)"
#                       cursor.execute("create table booker.vacuum_ddbe ( like booker.d_daily_buyer_effectiveness)")
#                       print "Done insert into booker.vacuum_d_daily_buyer_effectiveness (select * from booker.d_daily_buyer_effectiveness)"
                        time.sleep(12);
                        global exitFlag
                        exitFlag = 1
                        print "%s:exitFlag " % (exitFlag)
                except:
                        print "Exception"
                        global exitFlag
                        exitFlag = 1

# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread1.setDaemon(True)
thread2 = myThread(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()
