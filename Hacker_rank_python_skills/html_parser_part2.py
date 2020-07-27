from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_comment(self, comment):
        if '\n' in comment:
            print('>>> Multi-line Comment')
        else:
            print('>>> Single-line Comment')
        print(comment)
    def handle_data(self, data):
        if len(data) > 1:
            print('>>> Data', data, sep='\n')
parser = MyHTMLParser()
html_string = ''
for i in range(int(input())):
    html_string += input().rstrip() + '\n'
parser.feed(html_string)
parser.close()