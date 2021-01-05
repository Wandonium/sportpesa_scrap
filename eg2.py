from lxml import html
from urllib.request import urlopen

link = 'http://httpbin.org/forms/post'
root = html.parse(urlopen(link)).getroot()
tree = html.parse(urlopen(link))

print(type(root))   #<class 'lxml.html.HtmlElement'>
print(type(tree))   #<class 'lxml.etree._ElementTree'>
print(tree)