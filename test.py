import feedparser


def rss():
    # membaca RSS feed
    rss_url = 'https://rss.nytimes.com/services/xml/rss/nyt/World.xml'
    feed = feedparser.parse(rss_url)

    # menampilkan informasi terbaru dari feed
    for entry in feed.entries:
        print("title :", entry.title)
        print("link", entry.link)
        print("publised", entry.published)
        print('\n')


if __name__ == '__main__':
    rss()
