# 9
# <head>
# <title>HTML</title>
# </head>
# <object type="application/x-flash"
# data="your-file.swf"
# width="0" height="0">
# <!-- <param name="movie" value="your-file.swf" /> -->
# <param name="quality" value="high"/>
# </object>

# head
# # title
# # object
# # -> type > application/x-flash
# # -> data > your-file.swf
# # -> width > 0
# # -> height > 0
# # param
# # -> name > quality
# # -> value > high


from html.parser import HTMLParser




def value(attrs = None):
    if attrs:
        [print('->', attr, '>', val) for attr, val, in attrs]


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        value(attrs)


    def handle_startendtag(self, tag, attrs):
        print( tag)
        value(attrs)


parser = MyHTMLParser()
html_string = ''
for i in range(int(input())):
    html_string += input().rstrip() + '\n'
parser.feed(html_string)
parser.close()