import urllib.request
import xml.etree.ElementTree


class News:
    def __init__(self, end_point):
        self.endPoint = end_point
        self.rss = ""
        self.title = ""
        self.link = ""
        self.reel_title = []
        self.reel_description = []
        self.reel_link = []



    def parse_xml(self):
        xml_tree = xml.etree.ElementTree.fromstring(self.rss)
        for xml_element in xml_tree:
            if xml_element.tag == 'channel':
                channel = xml_element
                for channel_element in channel:
                    if channel_element.tag == "title":
                        self.title = channel_element.text
                    if channel_element.tag == "link":
                        self.link = channel_element.text
                    if channel_element.tag == "item":
                        item = channel_element
                        for item_element in item:
                            if item_element.tag == "title":
                                self.reel_title.append(item_element.text)
                            elif item_element.tag == "description":
                                feedflare_loc = item_element.text.find("<div class=\"feedflare\">")  # look for beginning of feedflare (Reuters)
                                if feedflare_loc > 0:
                                    self.reel_description.append(item_element.text[0:feedflare_loc])
                                else:
                                    self.reel_description.append(item_element.text)
                            elif item_element.tag == "link":
                                self.reel_link.append(item_element.text)
