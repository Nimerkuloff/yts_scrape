from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

def main():
    for i in range(5,30):
        url='https://yts.mx/api/v2/list_movies.json?quality=1080p&genre=thriller&minimum_rating=6&sort_by=peers&limit=800&page='+str(i)

        req = Request(url, headers={'User-Agent': 'XYZ/3.0'})
        html = urlopen(req, timeout=10).read()

        soup = BeautifulSoup(html, 'html.parser')
        with open("test.txt", "a") as myfile:
            myfile.write(soup.text)
        #TODO: implement nested dict search. Used sublime with (.*\n.*\n) this time
if __name__ == "__main__":
    main()
