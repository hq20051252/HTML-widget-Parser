def formatDate(date):
    print date
    if len(date.split(' ')) != 3:
        return "0000-00-00"

    a = date.split()
    print a
#    print a,type(a[0])

    mounth_map = {  'january':'1',\
                    'february':'2',\
                    'march':'3',\
                    'april':'4',\
                    'may':'5',\
                    'june':'6',\
                    'july':'7',\
                    'august':'8',\
                    'september':'9',\
                    'october':'10',\
                    'november':'11',\
                    'december':'12'\
                    }

    a[1] = mounth_map[a[1]]

    return '-'.join([a[2],a[1],a[0]])

if __name__ == '__main__':
    a = '23 august 1986'
    print formatDate(a)