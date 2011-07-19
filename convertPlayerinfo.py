import formatDate

def convertPlayerinfo(playerinfo):
    playerinfo = playerinfo
    if not playerinfo:
        return {}



    default = { 'name':"",\
                'firstname':"",\
                'lastname':"",\
                'chinesename':"",\
                'alias':"",\
                'nationality':"",\
                'birthday':"0000-00-00",\
                'age':"-1",\
                'homeland':"",\
                'motherland':"",\
                'position':"",\
                'height':"-1",\
                'weight':"-1",\
                'preferredfoot':"",\
                'photo':""\
                }
    #Key of dict above map
    map = {     'first name':"firstname",\
                'last name':"lastname",\
                'chinese name':"chinese name",\
                'alias':"alias",\
                'nationality':"nationality",\
                'date of birth':"birthday",\
                'age':"age",\
                'country of birth':"motherland",\
                'position':"position",\
                'height':"height",\
                'weight':"weight",\
                'foot':"preferredfoot",\
                'place of birth':"homeland"\
                }

    value_map = {'right':'R','left':'L','both':'R,L'}

    default['photo'] = playerinfo[-1]

    for name in playerinfo[:-1]:
        if name in map.keys():
            default[map[name]] = playerinfo[playerinfo.index(name) + 1]

    if default['preferredfoot']:
        default['preferredfoot'] = value_map[default['preferredfoot']]

    if default['birthday']:
        default['birthday'] = formatDate.formatDate(default['birthday'])

    if default['weight']:
#        print default['weight'],type(default['weight'])
        default['weight'] = default['weight'].split(' ')[0]


    if default['height']:
        default['height'] = default['height'].split(' ')[0]

    if default['age'] == 'deceased':
        default['age'] = '0'

    default['name'] = default['firstname'] +' ' + default['lastname']


    return default





