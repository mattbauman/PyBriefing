import urllib.request
import re
import time


def parse_content(x):
    content = x
    # Date Time
    data_time_string = 'data-time="'
    data_time_string_len = data_time_string.__len__()
    data_time_beg = content.find(data_time_string)
    dt = content[data_time_beg + data_time_string_len:]
    dt = dt[:10]
    if dt.__len__() > 0:
        dt_int = int(dt)
        dt_ts = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(dt_int))
    else:
        dt_ts = dt
    # Tweet Content
    js_tweet_text_container_start = content.find('<div class="js-tweet-text-container">')
    js_tweet_text_container = content[js_tweet_text_container_start:]
    paragraph_start = js_tweet_text_container.find('<p')
    paragraph = js_tweet_text_container[paragraph_start:]
    tweet_start = paragraph.find('>') + 1
    tweet = paragraph[tweet_start:]
    tweet_end = tweet.find('</p>')
    tweet = tweet[:tweet_end]
    return dt_ts, tweet


twitter_users = ['realDonaldTrump', 'ZenEssentials']
for twitter_user in twitter_users:
    request_urlopen = urllib.request.urlopen("https://twitter.com/" + twitter_user + "?lang=en")
    response = request_urlopen.read().decode("utf-8")
    response = response.replace('\n', '')
    tweets = []
    for div_class_content in re.finditer('<div class="content">', response):
        div_class_content_start = int(div_class_content.start())
        div_class_content_end = response[div_class_content_start + 1:].find('<div class="content">')  # next tag
        div_class_content_end = div_class_content_start + div_class_content_end
        content_str = response[div_class_content_start:div_class_content_end]
        tweet = parse_content(content_str)
        tweets.append(tweet)
    for x in tweets:
        print('<span>')
        print(twitter_user)
        print('<i>' + x[0] + '</i>')
        print('<p>' + x[1] + '</p>')
        print('</span>')
        print('<br/>')
