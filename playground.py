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


# How do we handle multiple pages? We do a while loop

province_url = f'https://www.privateproperty.co.za/for-sale/gauteng/3'
area_container = {'div': 'contentHolder'}

obj = webscrape(province_url, area_container)
items = obj.scraper_items()

from utils.websites import privateproperty

areas = privateproperty().get_area_links()
final_dataframe = privateproperty().listing_aggregations(areas)
