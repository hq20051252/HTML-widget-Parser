from guolv  import formatHTML
from html_parser import MyHTMLParser
import tool


def operater(pageQueue,resultQueue):

    data = pageQueue.get(block = True)
    playerid = '/'.join(tool.getplayerid(data[0]))
    htmltext = data[1]

    html = formatHTML(html)

    hc = MyHTMLParser()
    hc.feed(html)

    playerinfo = hc.get_playerinfo()
    career = hc.get_career()

    playerinfo = tool.addkeytodict(playerinfo,'player_id',playerid)
    career = tool.addkeytodict(career,'player_id',playerid)

    resultQueue.put((playerinfo,career),block = True)

