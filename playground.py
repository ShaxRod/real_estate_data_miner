from utils.scrape import webscrape
import pandas as pd

url = 'https://www.privateproperty.co.za/for-sale/eastern-cape/jeffreys-bay-to-tsitsikamma/jeffreys-bay/64'
#container = {'a': "listingResult row"}
container = {'div': 'pageNumbers'}

obj = webscrape(url, container)

# html, items = obj.scraper_items(True)

data = {'title': 'div',
        'priceDescription': 'div',
        'propertyType': 'div',
        'suburb': 'div',
        'address': 'div'
        }
dict = obj.scraper_dict(data)
# find a way to get the listing unique id from json string somehow?

from utils.websites import privateproperty

areas = privateproperty().get_area_links()
final_dataframe = privateproperty().listing_aggregations(areas)
