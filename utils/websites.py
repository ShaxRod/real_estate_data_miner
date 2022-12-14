import pandas as pd

from utils.scrape import webscrape
from utils.general import data_structure_format


class privateproperty:
    '''
    This class is able to pull all relevant data from the privateproperty.co.za website
    '''

    def get_area_links(self):

        '''
        :return: dictionary with all area links of website
        '''
        area_dict = dict()
        provinces = {'eastern-cape': '7',
                     'free-state': '6',
                     'gauteng': '3',
                     'kwazulu-natal': '2',
                     'limpopo': '8',
                     'mpumalanga': '10',
                     'northern-cape': '5',
                     'north-west': '9',
                     'western-cape': '4'}

        area_container = {'div': 'contentHolder'}

        for province in provinces:
            province_url = f'https://www.privateproperty.co.za/for-sale/{province}/{provinces[province]}'
            province_object = webscrape(province_url, area_container)

            items = province_object.scraper_items()
            try:
                areas = items[1].find_all('a', href=True)
                area_list = ['https://www.privateproperty.co.za' + i['href'] for i in areas]
                area_dict[province] = area_list
            except:
                print(f'{province} is tikking')

        return area_dict

    def listing_aggregations(self, area_dict: dict):

        final_df = pd.DataFrame()

        container = {'a': "listingResult row"}
        data = {'title': 'div',
                'priceDescription': 'div',
                'propertyType': 'div',
                'suburb': 'div',
                'address': 'div'
                }
        index_container = {'div': 'pageNumbers'}

        for province in area_dict:
            for permutation in area_dict[province]:
                permutation_items = webscrape(permutation, index_container).scraper_items()

                if len(permutation_items) > 0:
                    links = permutation_items[0].find_all('a', href=True)
                    try:
                        if len(links) == 0:
                            max_index = 1
                        else:
                            max_index_link = links[-2]['href']
                            max_index = int(max_index_link.split('=')[1])

                        for index in range(1, max_index + 1):
                            print(province, permutation, index)
                            if index == 1:
                                url = permutation
                            else:
                                url = f'{permutation}?page={index}'
                            obj = webscrape(url, container)
                            obj_dict = obj.scraper_dict(data)
                            frame = data_structure_format().nest_dict_to_dataframe(obj_dict)
                            final_df = pd.concat([final_df, frame], ignore_index=True)
                            print(len(final_df))
                    except:
                        print(f'{permutation} is tikking')
                else:
                    continue

        return final_df
