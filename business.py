import briefing

file = "business.php"
urls = [
    "https://www.npr.org/rss/rss.php?id=1006",
    "http://feeds.bbci.co.uk/news/business/rss.xml",
    "http://feeds.reuters.com/reuters/businessNews"]

business = briefing.Briefing(urls, file)
business.get_news_feed()
