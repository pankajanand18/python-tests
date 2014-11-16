__author__ = 'pankaj'

class control:
    def __enter__(self):

        return "Enter data"

    def __exit__(self, exc_type, exc_val, exc_tb):
        print "exit"


with control() as str:
    print str
    print 'hello world'

