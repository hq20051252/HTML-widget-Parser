class filesplit(object):

    __version__ = "alpha1.0"

    def __init__(self,fileobject,splitmark):
        '''This class wraps a file object,which is a codec_wrapped_file.
        It has two method,read(),readall().The previous method returns
        one record.The next one return all records as a list.'''

        #######################################################
        # In this block , we need a check funtion to check the argument.
        # The fileobject must be wrapped by codecs.
        #######################################################

        self.file = fileobject
        self.mark = splitmark
        ##
        print splitmark
        ##
        self.position = (0,0)   #The row number of the record.

    def read(self):
        mark = 0
        cache = []
        linecache = ""

        while True:
            try:
                linecache = self.file.next().strip()

            except StopIteration:
                if cache:
                    ##
                    print "OK,you got me!"
                    ##

                    return ''.join(cache)
                else:
                    #Here we raise a exception to tell the invoker
                    #that there's no record now.
                    raise StopIteration

            if self.mark == linecache:
                ##
                print "OK,you got me!"
                ##
                return ' '.join(cache)
            else:
                cache.append(linecache)
                ##
                print "Look,more line!"
                ##

##test
if __name__ == '__main__':
#    import codecs
#    fd = codecs.open("test.html",'rb','utf-8')
    fd = open('test.txt','r')
    fds = filesplit(fd,u'@newpage@')
    while True:
        try:
            print "I'm here,are you find me ?"
            print fds.read()
        except StopIteration:
            break









