from bs4 import BeautifulSoup
import requests
import re
from datetime import datetime
import pandas as pd


URL = 'https://www.stoloto.ru/top3/archive/'

pattern = re.compile(r'\d{2}\s*\s\d{4}\s\w\d{2}:\d{2}')

top_3_data = pd.DataFrame(columns=['date', 'num1', 'num2', 'num3'])

def data_converter(my_data:str) -> datetime.date:
    my_data = my_data.replace(':', ' ')
    my_data = my_data.split()
    month_list = {'ноября': '11',
                  'декабря': '12',
                  'января': '01',
                  'февраля': '02',
                  'марта': '03',
                  'апреля': '04',
                  'мая': '05',
                  'июня': '06',
                  'июля': '07',
                  'августа': '08',
                  'сентября': '09',
                  'октября': '10'}
    str_date = list([int(my_data[2]),
                     int(month_list.get(my_data[1])),
                     int(my_data[0]),
                     int(my_data[4]),
                     int(my_data[5]),])
                 
    str_date = datetime(str_date[0], str_date[1], str_date[2],
                        str_date[3], str_date[4])
    return(str_date)


def simple_extractor(URL: str) -> dict:
    html_content = requests.get(URL).text
    bsObj = BeautifulSoup(html_content, 'html.parser')
    for header in bsObj.find_all('h1'):
        date = re.findall(pattern, str(header.text))
        print(date)
    
    num = bsObj.findAll('li', {'class':['number0',
                                    'number1',
                                    'number2',
                                    'number3',
                                    'number4',
                                    'number5',
                                    'number6',
                                    'number7',
                                    'number8',
                                    'number9']})
    nums = [str(i)[-6] for i in num]
    
    data_dict = {'date': data_converter(date),
                 'num1': int(nums[0]),
                 'num2': int(nums[1]),
                 'num3': int(nums[2])}
    
    return(data_dict)


for x in range(1, 100):
    if x % 1748 == 0:
        print(f'{round(x / 174815 * 100, 1)} done!')
    url = URL+str(x)
    my_dict = simple_extractor(url)
    top_3_data = top_3_data.append(my_dict, ignore_index=True)

print(f"{len(top_3_data)} records added")
top_3_data.to_excel('all_lottery_data.xlsx')

    
    



