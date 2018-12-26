import urllib.request
import xml.etree.ElementTree

class News:
    rss=""
    title=""
    link=""
    reel_length = 5
    reel_title = ["" for x in range(reel_length)]
    reel_description = ["" for x in range(reel_length)]
    reel_link = ["" for x in range(reel_length)]

    def __init__(self, endPoint):
        self.endPoint = endPoint
    def get_rss(self):
        request = urllib.request.urlopen(self.endPoint)
        response = request.read().decode("utf-8")
        self.rss=response
    def parse_xml(self):
        xml_tree = xml.etree.ElementTree.fromstring(self.rss)
        i = 0
        for xml_element in xml_tree:
            if xml_element.tag=='channel':
                channel=xml_element
                for channel_element in channel:
                    if channel_element.tag=="title":
                        self.title=channel_element.text
                    if channel_element.tag=="link":
                        self.link=channel_element.text
                    if channel_element.tag=="item" and i<self.reel_length:
                        item=channel_element
                        for item_element in item:
                            if item_element.tag=="title":
                                self.reel_title[i]=item_element.text
                            elif item_element.tag=="description":
                                feedflare_loc = item_element.text.find("<") ##look for beginning of feedflare (Reuters)
                                if feedflare_loc>0:
                                    self.reel_description[i] = item_element.text[0:feedflare_loc]
                                else:
                                    self.reel_description[i] = item_element.text
                            elif item_element.tag=="link":
                                self.reel_link[i] = item_element.text
                        i+=1
    def print(self):
        for i in range(self.reel_length):
            print(self.title + ' (' + str(i+1) + ')')
            print(self.link)
            print(self.reel_title[i])
            print(self.reel_description[i])
            print(self.reel_link[i])
            print()
            i+=1

NPRBusiness = News("https://www.npr.org/rss/rss.php?id=1006")
NPRBusiness.get_rss()
NPRBusiness.parse_xml()
NPRBusiness.print()

BBCBusiness = News("http://feeds.bbci.co.uk/news/business/rss.xml")
BBCBusiness.get_rss()
BBCBusiness.parse_xml()
BBCBusiness.print()

ReutersBusiness = News("http://feeds.reuters.com/reuters/businessNews")
ReutersBusiness.get_rss()
ReutersBusiness.parse_xml()
ReutersBusiness.print()