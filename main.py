from utils.websites import privateproperty
import datetime


def main():
    provinces = {'western-cape': '4'}
    areas = privateproperty().get_area_links(provinces=provinces)
    final_dataframe = privateproperty().listing_aggregations(areas)
    return final_dataframe


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    output = main()
    main_dir = r'C:\Users\User\OneDrive\Documents\brian'
    output.to_excel(f'{main_dir}/MIT_data{datetime.date.today()}')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
