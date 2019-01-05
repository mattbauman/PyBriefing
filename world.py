import briefing

file = "world.php"
urls = [
    "http://feeds.bbci.co.uk/news/video_and_audio/world/rss.xml",
    "http://feeds.reuters.com/Reuters/worldNews",
    "https://www.npr.org/rss/rss.php?id=1004",
    "https://www.pbs.org/newshour/feeds/rss/world"]

business = briefing.Briefing(urls, file)
business.get_news_feed()
