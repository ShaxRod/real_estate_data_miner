import pandas as pd

from utils.websites import privateproperty
from utils.scrape import webscrape


def get_main_features(mit_data: pd.DataFrame):
    main_features = dict()
    catch = dict()
    for i, link in enumerate(mit_data['url']):
        try:
            soup_html, _ = webscrape(url=link, container={'div': 'listing-details__main-features'}).scraper_items(True)
            souper = soup_html.find_all('span', {'class' : 'property-features__name-value'})
            if len(souper) !=0:
                temp = {'url' : link}
                for feature in souper:
                    f_list = feature.text.split()
                    if 'Listing' in f_list:
                        temp['listing_number'] = str(f_list[-1])
                    elif ('Erf' and 'size') in f_list:
                        temp['plot_size'] = float(f_list[-2])
                    elif ('Floor' and 'size') in f_list:
                        temp['floor_size'] = float(f_list[-2])
                    elif ('Rates' and 'taxes') in f_list:
                        rates = f_list[4:]
                        cct = ''
                        for j in rates:
                            cct += j
                        temp['rates'] = cct

                for feature in ['listing_number', 'plot_size', 'floor_size', 'rates']:
                    if feature not in temp.keys():
                        temp[feature] = 0
            else:
                temp = {'url': link,
                        'Floor_Area': '0',
                        'Land_Area': '0',
                        'Rates': '0',
                        'Levy': '0'}
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
        scrape_frame = scrape_frame.rename(columns=property_config[property_type]['df_columns'])

        scrape_frame['suburb'] = scrape_frame.apply(lambda x: x['address']
                                                    if x['suburb'] == 'empty html element'
                                                    else x['suburb'], axis=1
                                                    )
        scrape_frame['address'] = scrape_frame.apply(lambda x: x['address'].replace(str(x['suburb']), ''), axis=1)


        woodstock = scrape_frame[scrape_frame['suburb'] == 'Woodstock'].copy(deep=True)
        features, catch = get_main_features(woodstock)
        feature_frame = pd.DataFrame(features)
        feature_frame = feature_frame.transpose()
        final_frame = pd.merge(left=woodstock,
                               right=feature_frame,
                               on='url',
                               how='left')

        final_frame['property_type'] = property_type
        final_frame[['title', 'cost', 'suburb',
                     'address', 'url',
                     'listing_number', 'plot_size', 'rates',
                     'floor_size', 'property_type'
                     ]].to_excel(f'C:/Users/User/OneDrive/Documents/brian/{property_type}_frame.xlsx')
    return

obj = webscrape(url='https://www.privateproperty.co.za/for-sale/western-cape/cape-town/cape-town-city-bowl/tamboerskloof/13-carstens-street/T4607194',
                container={'div': 'listing-details__main-features'})
soup, item = obj.scraper_items(html_bool=True)
