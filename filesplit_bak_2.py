import types
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

        self.data = ""
        self.cache = []
        self.result = []

        if type(fileobject) == types.FileType \
            and type(splitmark) == types.StringType:
            self.data = fileobject.read()
            self.mark = splitmark
        else:
            print "Arguments type is not correct."
            return None

        ##
        print splitmark
        ##
        self.position = (0,0)   #The row number of the record.

        for line in self.data:
            if line.strip() == self.mark:
                self.result.append(self.cache)
                self.cache = []
            else:
                self.cache.append(line)


    def next(self):
        pass

    def read(self):
        return self.result







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









