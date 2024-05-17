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
    property_config = {'for-sale': {
                                    'data_dict': {
                                                    'title': 'div',
                                                     'listing-result__price txt-heading-2': 'div',
                                                     'listing-result__title txt-base-regular': 'div',
                                                     'listing-result__desktop-suburb listing-result__desktop-suburb--has-address txt-base-bold': 'span',
                                                     'listing-result__desktop-suburb  txt-base-bold' : 'span',
                                                     'listing-result__address txt-base-regular': 'span',
                                                     'href': 'href'
                                         },
                                    'df_columns': {
                                                    'listing-result__title txt-base-regular': 'title',
                                                    'listing-result__price txt-heading-2': 'cost',
                                                    'listing-result__desktop-suburb listing-result__desktop-suburb--has-address txt-base-bold': 'suburb',
                                                    'listing-result__address txt-base-regular': 'address',
                                                    'href': 'href'
        }
                           },
                        'to-rent': {
                                    'data_dict': {
                                                    'title': 'div',
                                                    'priceDescription': 'div',
                                                    'priceAdditionalDescriptor': 'div',
                                                    'propertyType': 'div',
                                                    'suburb': 'div',
                                                    'address': 'div',
                                                    'href': 'href'
                                                 },
                                    'df_columns': {
                                                    'listing-result__title txt-base-regular': 'title',
                                                    'listing-result__price txt-heading-2': 'cost',
                                                    'listing-result__desktop-suburb listing-result__desktop-suburb--has-address txt-base-bold': 'suburb',
                                                    'listing-result__address txt-base-regular': 'address',
                                                    'href': 'href'
                                                  }
                          }
              }

    output = brian.mitdata(property_config=property_config)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
