import requests
import urllib
import json
from os import remove
from PIL import Image
from bs4 import BeautifulSoup

def is_connected():
    try:
        host = socket.gethostbyname('www.google.co.in')
        socket.create_connection((host, 80))
        return True
    except:
        pass
    return False

def take_input():
    name = raw_input("Enter the Title : ")
    name += " imdb"
    return name

def search(name):
    url = 'https://google.com/search?q='
    
    name = urllib.quote_plus(name)
    url += name
    r  = requests.get(url)
    soup = BeautifulSoup(r.text,"lxml")

    for link in soup.find_all('a'):
        if "imdb.com" in str(link.get('href')):
            url = link.get('href')

            start = str(link.get('href')).find('?q=')
            end = str(link.get('href')).find('&')
            url = str(link.get('href'))[start+3:end]
            
            r  = requests.get(url)
            soup = BeautifulSoup(r.text,"lxml")
            return soup
    return None



def get_json(soup):
    for link in soup.find_all('script'):
        if link.get('type'):
            if "application/ld+json" in link.get('type'):
                d = json.loads(link.string)
                return d

def title(jsonOb):
    return jsonOb['name']

def types(jsonOb):
    return jsonOb['@type']

def content(jsonOb):
    return jsonOb['contentRating']

def ratings(jsonOb):
    return jsonOb['aggregateRating']['ratingValue']

def run_time(jsonOb):
    if jsonOb.get('duration'):
        time = jsonOb['duration']
        time = time.replace("PT","")
        time = time.replace("H","Hours ")
        time = time.replace("M","Mins")

        return time
    return "Not Available"

def release_date(soup):
    for link in soup.find_all('a'):
        if link.get('title'):
            if "See more release dates" in link.get('title'):
                date = link.string
                date = date.replace("\n","")

                return date
    return None

def genre(jsonOb):
    genres = jsonOb['genre']
    sentence = ""

    for g in genres:
        sentence += g + ", "
        
    return sentence[:-2]

def director(jsonOb):
    if jsonOb.get('director'):
        return jsonOb['director']['name']
    else:
        sentence = ""
        for c in jsonOb['creator']:
            if c['@type'] == 'Person':
                sentence += c['name'] + ', '
        return sentence[:-2]

def actors(jsonOb):
    actors = jsonOb['actor']
    sentence = ""

    for a in actors:
        sentence += a['name'] + ", "
    return sentence[:-2]

def summary(soup):
    for link in soup.findAll('div'):
        if link.get('class'):
            if "summary_text" in link.get('class'):
                summa = link.string
                summa = summa.replace("\n","")
                summa = summa.replace("  ","")

                return summa
    return None

def print_info(jsonOb,soup):
    print "\nTitle -",title(jsonOb)
    print "Type -",types(jsonOb)
    print "Content Rating -",content(jsonOb)
    print "Run Time -",run_time(jsonOb)
    print "Release Date -",release_date(soup)
    print "Rating -",ratings(jsonOb)
    print "\nGenre -",genre(jsonOb)
    print "Director -",director(jsonOb)
    print "Actors -",actors(jsonOb)
    print "\nSummary -",summary(soup)

def poster(jsonOb):
    show = int(input("\n\nEnter 1 to see the poster : "))
    if show == 1:
        titles = title(jsonOb)
        urllib.urlretrieve(jsonOb['image'], titles+".jpg")
        img = Image.open(titles+".jpg")
        img.show()
        remove(titles+".jpg")

def main():
    name = take_input()
    soup = search(name)
    if soup:
        jsonOb = get_json(soup)
        print_info(jsonOb,soup)
        poster(jsonOb)
    else:
        print "\nNot Found"


main()
