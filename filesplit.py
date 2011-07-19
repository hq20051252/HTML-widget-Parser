import types

def filesplit(fileobject,splitmark):


    #######################################################
    # In this block , we need a check funtion to check the argument.
    # The fileobject must be wrapped by codecs.
    #######################################################
    cache = []
    result = []

    if type(fileobject) == types.FileType \
        and type(splitmark) == types.StringType:
        data = fileobject.readlines()
        mark = splitmark
    else:
        print "Arguments type is not correct."
        return None

    ##
    print splitmark
    ##
    print len(data)

    for line in data:
        if line.strip() == mark:
            result.append(cache)
            cache = []
        else:
            cache.append(line)

    print len(result)

    return result








###test
#if __name__ == '__main__':
##    import codecs
##    fd = codecs.open("test.html",'rb','utf-8')
#    fd = open('test.txt','r')
#    fds = filesplit(fd,u'@newpage@')
#    while True:
#        try:
#            print "I'm here,are you find me ?"
#            print fds.read()
#        except StopIteration:
#            break
#
#







