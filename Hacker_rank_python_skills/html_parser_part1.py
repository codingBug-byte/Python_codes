# Start : html
# Start : head
# Start : title
# End   : title
# End   : head
# Start : body
# -> data-modal-target > None
# -> class > 1
# Start : h1
# End   : h1
# Empty : br
# End   : body
# End   : html

# 2
# <html><head><title>HTML Parser - I</title></head>
# <body data-modal-target class='1'><h1>HackerRank</h1><br /></body></html>

from html.parser import HTMLParser
def value(attrs = None):
    if attrs:
        [print('->', attr, '>', val) for attr, val, in attrs]

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        value(attrs)
    def handle_endtag(self, tag):
        print("End :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        value(attrs)


parser = MyHTMLParser()
line = ""
for i in range(int(input())):
    line = "{0}{1}".format(line, input())
parser.feed(line)
