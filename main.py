from utils.websites import privateproperty
import brian
import datetime


def main():
    provinces = {'western-cape': '4'}
    areas = privateproperty().get_area_links(provinces=provinces)
    final_dataframe = privateproperty().listing_aggregations(areas)
    return final_dataframe


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    config = {'for-sale': {'data_dict': {'title': 'div',
                                         'priceDescription': 'div',
                                         'propertyType': 'div',
                                         'suburb': 'div',
                                         'address': 'div',
                                         'href': 'href'
                                         }
                           },
              'to-rent': {'data_dict': {'title': 'div',
                                        'priceDescription': 'div',
                                        'priceAdditionalDescriptor': 'div',
                                        'propertyType': 'div',
                                        'suburb': 'div',
                                        'address': 'div',
                                        'href': 'href'
                                        }
                          }
              }

    output = brian.mitdata(property_config=config)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
