def formatHTML(htmlText,encoding='utf8'):
    """
    @function: formatHTML
    @parameters:
    #htmlText: html text to format

    @author: Roy Zuo
    @email: roy.zuo@gmail.com
    @date: Jun. 28, 2011
    """
    import re

#    try:
#        htmlText = htmlText.decode(encoding)
#    except:
#        pass

    # Case lower
    htmlText = htmlText.strip().lower()

    # Remove return symbols
    htmlText = htmlText.replace('\r','').replace('\n','')

    # Replace tab symbol to blank space
    p = re.compile(r'[\t\s]+', re.IGNORECASE)
    htmlText = p.sub(' ',htmlText)

    # Remove blank space in html tags
    p = re.compile(r'<\s+', re.IGNORECASE)
    htmlText = p.sub(r'<', htmlText)
    p = re.compile(r'\s+>', re.IGNORECASE)
    htmlText = p.sub(r'>', htmlText)
##
    # Got useful parts
    p = re.compile(r'(<html.*?</html.*?>)', re.IGNORECASE)
    m = p.search(htmlText)
    if m:
        htmlText = m.group(1)
##
    # Remove script content
    p = re.compile(r'<script.*?</script.*?>', re.IGNORECASE)
    htmlText = p.sub('',htmlText)
##
    # Remove css content
    p = re.compile(r'<style.*?/style>', re.IGNORECASE)
    p = re.compile(r'<([^>]*)style="[^"]*"', re.IGNORECASE)
    htmlText = p.sub(r'<\1',htmlText)
    p = re.compile(r"<([^>]*)style='[^']*'", re.IGNORECASE)
    htmlText = p.sub(r'<\1',htmlText)

    # Remove comments
    p = re.compile(r'<\!\-\-.*?\-\->', re.IGNORECASE)
    htmlText = p.sub('',htmlText)
##
    # Remove extra blank space
    p = re.compile(r'>\s+', re.IGNORECASE)
    htmlText = p.sub('>', htmlText)
    p = re.compile(r'\s+<', re.IGNORECASE)
    htmlText = p.sub('<', htmlText)
    p = re.compile(r'>([^\s]+)\s+([^\s]+)<', re.IGNORECASE)
    htmlText = p.sub(r'>\1 \2<',htmlText)

    # Remove malformed tag
    p = re.compile(r'<span style=MARGIN-RIGHT: 6px><IMG height=9 src=/web/images/arrow1_032.gif width=9></span>',re.IGNORECASE)
    htmlText = p.sub(' ',htmlText)

#    try:
#        htmlText = htmlText.encoding(encoding)
#        print "==="
#    except:
#        pass

    return htmlText