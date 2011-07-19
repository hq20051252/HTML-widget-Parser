from guolv  import formatHTML
from html_parser import MyHTMLParser
import tool


def operater(pageQueue,resultQueue):
    while True:

        data = pageQueue.get(block = True)
        if not data:
            continue

        playerid = '/'.join(tool.getplayerid(data[0]))
        htmltext = data[1]
#        print htmltext,"at:operater"

        html = formatHTML(htmltext)

        hc = MyHTMLParser()
        hc.feed(html)

        playerinfo = hc.get_playerinfo()
        career = hc.get_career()

        if playerinfo:
            playerinfo = tool.addkeytodict(playerinfo,'player_id',playerid)
        if career:
            career = tool.addkeytodict(career,'player_id',playerid)

        if playerinfo:
            resultQueue.put((playerinfo,career),block = True)
            print "resultQueue have more record!"
            print playerinfo
            print career

        print "I am working ,boss."

