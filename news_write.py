import news
import platform
import os.path


class NewsWrite:
    def __init__(self, news_feed_urls, file_name):
        self.news_feed_urls = news_feed_urls
        self.file_name = file_name
        self.news_objects = []

    def get_news(self, url):
        news_object = news.News(url)
        news_object.get_rss()
        news_object.parse_xml()
        return news_object

    def get_news_feed(self):
        for news_feed_url in self.news_feed_urls:
            x = self.get_news(news_feed_url)
            self.news_objects.append(x)

        if platform.system() == "Linux":
            path = "/opt/bitnami/apache2/htdocs/mattbauman.com/briefing/"
        else:
            path = "C:/Users/matt/Desktop"

        completeName = os.path.join(path, self.file_name)
        php_out = open(completeName, "w")

        for i in range(5):
            for news_object in self.news_objects:
                php_out.write(
                    "<div class=\"w3-card-4 w3-margin w3-white\">" + news_object.title + ' (' + str(i + 1) + ') \n')
                php_out.write("\t<div class=\"w3-container\">\n")
                php_out.write("\t\t<h5><b><a href=\""
                              + news_object.reel_link[i]
                              + "\" target=\"_blank\">"
                              + news_object.reel_title[i]
                              + "</a></b></h5>\n")
                php_out.write("\t\t<p>" + news_object.reel_description[i] + "</p>\n")
                php_out.write("\t</div>\n")
                php_out.write("</div>\n")
