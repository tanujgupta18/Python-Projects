import pyshorteners

url = input("Enter the URL: ")

def short_url(url):
    s = pyshorteners.Shortener()
    print(s.tinyurl.short(url))

short_url(url)