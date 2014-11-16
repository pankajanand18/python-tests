__author__ = 'pankaj'

import threading
import time
import psycopg2


conn= psycopg2.connect(dbname='devikadb', user='devikatest1', password='asdf1234',host='localhost')
cur=conn.cursor()


exit_thread=0
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
                do_poll(self.name, self.counter, 5)
        if self.threadID == 2:
                print "I am deep copy"
                deep_copy(self.name, self.counter, 5)
        print "Exiting " + self.name


def do_poll(name,counter,int):
    global  exit_thread
    global conn
    cursor=conn.cursor()

    while exit_thread==0:
        print 'do poll %s'%exit_thread
        cursor.execute("select * from test limit 1");
    print 'poll value %s'%exit_thread



def deep_copy(name,counter,int):
    global  conn
    print 'drop table'
    cur.execute("DROP TABLE test3")
    conn.commit()
    print 'creating table'
    cur.execute("CREATE TABLE test3 (id serial PRIMARY KEY, num integer, data varchar);")
    conn.commit()
    print 'Thread Deep Copy : starting copy'
    cur.execute("insert into test3 (select * from test)")
    print 'Thread Deep Copy : copy finished'
    conn.commit()
    print 'Thread Deep Copy : commit finised'
    global  exit_thread
    exit_thread=1



thread1 = myThread(1, "Thread-1", 1)
#thread1.setDaemon(True)
thread2 = myThread(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()


# thread1.join()
# thread2.join()
#exit_thread=1




