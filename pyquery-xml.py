from pyquery import PyQuery as pq
import re

if __name__ == '__main__':
    # reading file
    xmlFile = open('sitemap.xml', 'r').read()

    # creating PyQuery object using parser 'html'
    urlHtml = pq(xmlFile, parser='html')

    print("Children Length: ", urlHtml.children().__len__())
    print("First child: ", urlHtml.children().eq(0))
    print("Inner Child/First child: ", urlHtml.children().children().eq(0))

    dataSet = list()
    for url in urlHtml.children().find('loc:contains("blog")').items():
        dataSet.append(url.text())
    
    print("Length of dataSet: ", len(dataSet))
    #print(dataSet)

    # creating PyQuery object using parser 'xml'
    urlXml = pq(xmlFile, parser='xml')

    print("Children Length: ", urlXml.children().__len__())
    print("First Children: ", urlXml.children().eq(0))
    print("Inner Child/First Children: ", urlXml.children().children().eq(0))

    dataSet2 = list()
    for url in urlXml.remove_namespaces().children().find('loc:contains("blog")').items():
        dataSet2.append(url.text())
    
    print("Length of dataSet2: ", len(dataSet2))
    # print(dataSet2)

    # making use of regular expressions instead
    # print("URLs using children: ", urlXml.children().text())
    # print("URLs using children: ", urlXml.children().children().text())
    # print("URLs using children: ", urlXml.text())

    blogXml = re.split(r'\s', urlXml.children().text())
    print("Length of blogXml: ", len(blogXml))

    # filter(), filters URLs from blogXml that match string 'blog'
    dataSet3 = list(filter(lambda blogXml: re.findall(r'blog', blogXml), blogXml))
    print("Length of dataSet: ", len(dataSet))
    print("Blog Urls: ", dataSet)