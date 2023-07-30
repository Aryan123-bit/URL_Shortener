import pyshorteners

url = input("enter the URL")

def shortenurl(url):
    s = pyshorteners.Shortener()
    print(s.tinyurl.short(url))


shortenurl(url)