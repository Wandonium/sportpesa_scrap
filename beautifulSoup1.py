from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import re

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
<h1>Secret agents</h1>
<ul>
    <li data-id="10784">Jason Walters, 003: Found dead in "A View to a Kill".</li>
    <li data-id="97865">Alex Trevelyan, 006: Agent turned terrorist leader; James' nemesis in "Goldeneye".</li>
    <li data-id="45732">James Bond, 007: The main man; shaken but not stirred.</li>
</ul>
</body>
</html>
"""
tagsA = SoupStrainer("a")
soupA = BeautifulSoup(html_doc, 'lxml', parse_only=tagsA)

#print(type(soupA))
#print(soupA.prettify())
""" using has_attr
print(soupA.a.has_attr('class'))
print(soupA.a.has_attr('name'))"""

""" using find() method
print(soupA.find("a"))
print(soupA.find('a', attrs={'class': 'sister'}))
print(soupA.find('a', attrs={'class': 'sister'}, text="Lacie"))
print(soupA.find("a", attrs={'id': 'link3'}))
print(soupA.find('a', id='link2'))
"""

""" using find_all() method
print(soupA.find_all("a"))  # or print(soupA.find_all(name="a"))
print(soupA.find_all("a", limit=2)) # find all <a> but return only 2 of them
"""

""" using regular expressions with find() and find_all() methods
print(soupA.find("a", text=re.compile(r'cie')))
print(soupA.find_all('a', attrs={'id':re.compile(r'3')}))
print(soupA.find_all(re.compile(r'a')))
"""

soup = BeautifulSoup(html_doc, 'lxml')
""" using find_all() method with class parameters
print(soup.find_all("p", "story")) #class = story
print(soup.find_all("p", "title")) #class = title
print(soup.find_all("p", attrs={'class' : ["title", "story"]}))
print(soup.find_all(["p", "li"]))
"""

""" using find_all() method to search for a particular string
print(soup.find_all(string="Elsie"))
print(soup.find_all(text=re.compile(r'Elsie')))
print(soup.find_all("a", string="Lacie"))
"""

""" iteration:
for li in soup.ul.find_all('li'):
    print(li.name, ' > ', li.get('data-id'), ' > ', li.text)
"""

""" element traversing without find_all()
print(soupA.a)
print(soup.li)
print(soup.p)
print(soup.p.b)
print(soup.ul.find('li', attrs={'data-id': '45732'}))
print(soup.ul.find('li', attrs={'data-id': '45732'}).text)
print(soup.p.text)
print(soup.li.text)
print(soup.p.string)
"""

""" using children, contents and descendants
print(list(soup.find('p', 'story').children))
print(list(soup.find('p', 'story').contents))
print(list(soup.find('p', 'story').descendants))
"""

""" using List Comprehension
print([a.name for a in soup.find('p', 'story').children])
print([{'tag': a.name, 'text': a.text, 'class': a.get('class')} 
        for a in soup.find('p', 'story').children
            if a.name != None
])
print([a.name for a in soup.find('p', 'story').descendants])
print(list(filter(None, [a.name for a in soup.find('p', 'story').descendants])))
"""

""" using findChild() and findChildren()
print(soup.find('p', 'story').findChildren())
print(soup.find('p', 'story').findChild())
"""

""" using parent
# print parent element of <a> with class=sister
print(soup.find('a', 'sister').parent)
print(soup.find('a', 'sister').parent.name)
# print text from parent element of <a> with class=sister
print(soup.find('a', 'sister').parent.text)
"""

""" using parents for iteration
for element in soup.find('a', 'sister').parents:
    print(element.name)
"""

""" using findParent() and findParents()
# find single parent for selected <a> with class = sister
print(soup.find('a', 'sister').findParent())
# find all parents for selected <a> with class = sister
print(soup.find('a', 'sister').findParents())
"""

""" using next and next_element
print(soup.find('p', 'story').next)
print(soup.find('p', 'story').next.next)
print(soup.find('p', 'story').next_element)
print(soup.find('p', 'story').next_element.next_element)
print(soup.find('p', 'story').next_element.next_element.next_element)
"""

""" using previous and previous_element
print(soup.find('p', 'story').previous) # returns empty or new-line
print(soup.find('p', 'story').previous.previous)
print(soup.find('p', 'story').previous_element) # returns empty or new-line
print(soup.find('p', 'story').previous_element.previous_element)
print(soup.find('p', 'story').previous_element.previous_element.previous_element)
"""

""" using both next and previous simultenously
print(soup.find('p', 'title').next.next.previous.previous)
"""

""" using next_elements for iteration
for element in soup.find('ul').next_elements:
    print(element)
"""

""" next and next_element vs find_next()
print(soup.find('p', 'story').next)
print(soup.find('p', 'story').next_element)
print(soup.find('p', 'story').find_next())
print(soup.find('p', 'story').find_next('h1'))
"""

""" find_all_next() function
print(soup.find('p', 'story').find_all_next())
print(soup.find('p', 'story').find_all_next('li', limit=2))
"""

""" using find_previous()
print(soup.find('ul').previous.previous.previous)
print(soup.find('ul').find_previous())
print(soup.find('ul').find_previous('p', 'title'))
"""

""" using find_all_previous()
print(soup.find('ul').find_all_previous('p'))
"""

""" using next_sibling and previous_sibling
print(soup.find('p', 'title').next_sibling) # returns empty or new-line
print(soup.find('p', 'title').next_sibling.next_sibling)
print(soup.find('ul').previous_sibling)  # returns empty or new-line
print(soup.find('ul').previous_sibling.previous_sibling)
"""

""" using next_siblings and previous_siblings for iteration
title = [ele.name for ele in soup.find('p', 'title').next_siblings]
print(list(filter(None, title)))
ul = [ele.name for ele in soup.find('ul').previous_siblings]
print(list(filter(None, ul)))
"""

""" using find_next_sibling() and find_next_siblings()
print(soup.find('p', 'title').find_next_siblings('p'))
print(soup.find('h1').find_next_sibling())
print(soup.find('h1').find_next_sibling('li'))
"""

""" using find_previous_sibling() and find_previous_siblings()
print(soup.find('ul').find_previous_sibling())
print(soup.find('ul').find_previous_siblings())
"""

""" using select()  and select_one() for selecting using css
print(soup.select('li[data-id]'))
print(soup.select('li[data-id]')[1])
print(soup.select_one('li[data-id]'))
"""

""" using css combinators i.e + >
print(soup.select('p.story > a.sister'))
print(soup.select('p b'))
print(soup.select('p + h1'))
print(soup.select('p.story + h1'))
print(soup.select('p.title + h1'))
"""

""" searching for elements using attribute values """
# print(soup.select('a[href*="example.com"]'))
print(soup.select('a[id*="link"]'))