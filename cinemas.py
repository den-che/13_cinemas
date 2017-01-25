import requests
from bs4 import BeautifulSoup

def fetch_afisha_page():
    response = requests.get('http://www.afisha.ru/msk/schedule_cinema/')
    page =  BeautifulSoup(response.content,'html.parser')
    with open('parse.txt', 'w', encoding ='utf-8') as parse_file:
        parse_file.write("{}".format(page)) 
    return page


def parse_afisha_list(raw_html):
    pass


def fetch_movie_info(movie_title):
    pass


def output_movies_to_console(movies):
    pass


if __name__ == '__main__':
    raw_input = fetch_afisha_page()

