from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd


class webscrape(object):

    def __init__(self, url: str, container: dict):

        """
        :param url: url string of website/page you want to scrape
        :param container: dictionary which contains the main container/html element you want to scrape {element: class name}
        """

        self.url = url
        self.element = list(container.keys())[0]
        self.class_name = container[self.element]

    def request(self):
        request = urlopen(self.url)
        page_html = request.read()
        request.close()
        return page_html

    def scraper_items(self, html_bool=False):
        '''
        :param html_bool: True if you want the beautiful soup html scrape else False
        :return: the html of the desired element with specified class
        '''

        page_html = self.request()
        html_soup = BeautifulSoup(page_html, 'html.parser')
        items = html_soup.find_all(self.element, class_=self.class_name)
        if html_bool:
            return html_soup, items
        else:
            return items

    def scraper_dict(self, data: dict):

        '''
        :param data: takes in dictionary of required elements from webpage
        :return: dictionary populated with individual items and their respective elements
        '''

        dict = {}
        items = self.scraper_items(False)

        for i, item in enumerate(items):
            temp_dict = {}
            for element in data:
                try:
                    if data[element] == 'div':
                        thing = item.find(data[element], class_=element).text
                    else:
                        thing = item.get(element)
                    temp_dict[element] = thing
                except:
                    temp_dict[element] = 'empty html element'

            dict[f'{i}'] = temp_dict

        return dict
