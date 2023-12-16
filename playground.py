from utils.scrape import webscrape
import pandas as pd

website = "https://www.privateproperty.co.za"
url = 'https://www.privateproperty.co.za/for-sale/eastern-cape/jeffreys-bay-to-tsitsikamma/jeffreys-bay/64'
container = {'a': "listingResult row"}

obj = webscrape(url, container)

html, items = obj.scraper_items(True)

data = {'title': 'div',
        'priceDescription': 'div',
        'propertyType': 'div',
        'suburb': 'div',
        'address': 'div'
        }
dict = obj.scraper_dict(data)
# find a way to get the listing unique id from json string somehow?
'''------------------------------------------------------------------------------------------------------------------'''
from utils.websites import privateproperty

provinces = {'western-cape': '4'}
areas = privateproperty().get_area_links(provinces=provinces)
final_dataframe = privateproperty().listing_aggregations({'western-cape': [areas['western-cape'][11]]})

'''------------------------------------------------------------------------------------------------------------------'''

