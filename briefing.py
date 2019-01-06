import news_write

file = "world.php"
urls = [
    "http://feeds.bbci.co.uk/news/world/rss.xml",
    "http://feeds.reuters.com/Reuters/worldNews",
    "https://www.npr.org/rss/rss.php?id=1004",
    "https://www.pbs.org/newshour/feeds/rss/world"]
try:
    business = news_write.NewsWrite(urls, file)
    business.get_news_feed()
except:
    print("world news failed")
file = "business.php"
urls = [
    "https://www.npr.org/rss/rss.php?id=1006",
    "http://feeds.bbci.co.uk/news/business/rss.xml",
    "http://feeds.reuters.com/reuters/businessNews"]
try:
    business = news_write.NewsWrite(urls, file)
    business.get_news_feed()
except:
    print("business news failed")
