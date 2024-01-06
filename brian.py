import pandas as pd

from utils.websites import privateproperty
from utils.scrape import webscrape


def get_main_features(mit_data: pd.DataFrame):
    main_features = dict()
    catch = dict()
    for i, link in enumerate(mit_data['url']):
        try:
            dimensions = webscrape(url=link, container={'div': 'mainFeatures'}).scraper_items(False)
            print('dimensions: ', len(dimensions))
            if len(dimensions) != 0:
                temp = dict()
                temp['url'] = link
                for dimension in dimensions[0].find_all('span'):
                    dim_list = dimension.text.rsplit()
                    if len(dim_list) > 0:
                        if dim_list[0] == 'Land' or dim_list[0] == 'Floor':
                            temp[f'{dim_list[0]}_{dim_list[1]}'] = dim_list[2]
                        elif dim_list[0] == 'Rates' or dim_list[0] == 'Levy':
                            temp[f'{dim_list[0]}'] = dim_list[2]

                for key in ['url', 'Floor_Area', 'Land_Area', 'Rates', 'Levy']:
                    if key not in temp.keys():
                        temp[key] = '0'
            else:
                temp = {'url': link,
                        'Floor_Area': '0',
                        'Land_Area': '0',
                        'Rates': '0',
                        'Levy': '0'}
            print(temp)
        except:
            print(i, 'tapped out')
            catch[i] = {'index': i,
                        'url': link}
            continue
        main_features[i] = temp

    return main_features, catch


def mitdata(property_config: dict):
    # inputs
    website = "https://www.privateproperty.co.za"
    provinces = {'western-cape': '4'}
    for property_type in property_config:

        areas = privateproperty().get_area_links(provinces=provinces, property_type=property_type)
        scrape_frame = privateproperty().listing_aggregations({'western-cape': [areas['western-cape'][11]]},
                                                              data_dict=property_config[property_type]['data_dict'])
        scrape_frame['url'] = website + scrape_frame['href'].astype('str')
        woodstock = scrape_frame[scrape_frame['suburb'] == 'Woodstock'].copy(deep=True)
        features, catch = get_main_features(woodstock)
        feature_frame = pd.DataFrame(features)
        feature_frame = feature_frame.transpose()
        final_frame = pd.merge(left=woodstock,
                               right=feature_frame,
                               on='url',
                               how='left')
        final_frame['property_type'] = property_type
        final_frame.to_excel(f'C:/Users/User/OneDrive/Documents/brian/{property_type}_frame.xlsx')
    return

