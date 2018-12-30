import news
import platform

# BBCUSEndPoint = "http://feeds.bbci.co.uk/news/rss.xml?edition=us";
# BBCWorldNewsEndPoint = "http://feeds.bbci.co.uk/news/video_and_audio/world/rss.xml";
# ReutersTopNewsEndPoint = "http://feeds.reuters.com/reuters/topNews";
# ReutersWorldNewsEndPoint = "http://feeds.reuters.com/Reuters/worldNews";
# ReutersUSEndPoint = "http://feeds.reuters.com/Reuters/domesticNews";
# NPRWorldNewsEndPoint = "https://www.npr.org/rss/rss.php?id=1004";
# PBSWorldNewsEndPoint = "https://www.pbs.org/newshour/feeds/rss/world";
# StarTribuneLocalNewsEndPoint = "http://www.startribune.com/local/index.rss2";
# NPRBusiness = news.News("https://www.npr.org/rss/rss.php?id=1006")
# BBCBusiness = news.News("http://feeds.bbci.co.uk/news/business/rss.xml")
# ReutersBusiness = news.News("http://feeds.reuters.com/reuters/businessNews")

if platform.system() == "Windows":
    path = "C:/Users/matt/Desktop/mattbauman.com/briefing/"
elif platform.system() == "Linux":
    path = "/opt/bitnami/apache2/htdocs/mattbauman.com/briefing/"
else:
    path = "error"  # project path
print(path)

news_feed_urls = [
    "https://www.npr.org/rss/rss.php?id=1006",
    "http://feeds.bbci.co.uk/news/business/rss.xml",
    "http://feeds.reuters.com/reuters/businessNews"]

news_objects = []


def get_news(url):
    news_object = news.News(url)
    news_object.get_rss()
    news_object.parse_xml()
    return news_object


for news_feed_url in news_feed_urls:
    x = get_news(news_feed_url)
    news_objects.append(x)

for i in range(5):
    for news_object in news_objects:
        print("<div class=\"w3-card-4 w3-margin w3-white\">" + news_object.title + ' (' + str(i + 1) + ') ')
        print("\t<div class=\"w3-container\">")
        print("\t\t<h5><b><a href=\""
              + news_object.reel_link[i]
              + "\" target=\"_blank\">"
              + news_object.reel_title[i]
              + "</a></b></h5>")
        print("\t\t<p>" + news_object.reel_description[i] + "</p>")
        print("\t</div>")
        print("</div>")
