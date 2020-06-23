import numpy as np
import csv


def string_parser(test_string):
    preprocessed = []
    if test_string[:2] == '""':
        print('PASS!')
    
    elif ',,,' in test_string:
        print('too many commas')
    
    elif test_string[:1] == '"':
        test_string = test_string[1:].split('"')
        preprocessed = [test_string[0]]
        for el in test_string[1:-1]:
            if el == ',':
                test_string.remove(',')
            if el == '\n':
                test_string.remove('\n')
            if el == '':
                test_string.remove('')
            el = el.replace(',', '.')
            el = el.split(' ')
            for x in el:
                    # print(el)
                try:
                    x = float(x)
                    preprocessed.append(x)
                except:
                    if x != '.':
                        x = np.NaN
                        preprocessed.append(x)
                    else:
                        pass
    
    elif '"' in test_string:
        if ',х х,,' in test_string:
            test_string = test_string.replace(',х х,,', '",х х,,"')
        test_string = test_string.split('"')
        preprocessed = [test_string[0][:-1]]
        test_string = [x for x in test_string if len(x) > 1]

        for el in test_string[1:-1]:
            if el == ',':
                test_string.remove(',')
            if el == '\n':
                test_string.remove('\n')
            if el == '':
                test_string.remove('')
            el = el.replace(',', '.')
            el = el.split(' ')
            for x in el:
                    # print(el)
                try:
                    x = float(x)
                    preprocessed.append(x)
                except:
                    if el != '.' or el != '':
                        x = np.NaN
                        preprocessed.append(x)
                    else:
                        pass
    
    else:
        if ',х х,,' in test_string:
            test_string = test_string.replace(',х х,,', '",х х,,"')
        test_string = test_string.split(',')
        test_string = [x for x in test_string if len(x) > 1]

        preprocessed = [test_string[0][:-1]]
        for el in test_string[1:-1]:
            el =el.split(' ')
            for x in el:
                    # print(el)
                try:
                    x = float(x)
                    preprocessed.append(x)
                except:
                    if el != '.' or el != '':
                        x = np.NaN
                        preprocessed.append(x)
                    else:
                        pass
    
    return(preprocessed)


results = []

with open('test.csv') as f:
    lines = [line for line in f]
    for line in lines:
        row = string_parser(line)
        if row:
            results.append(row)

columns = ['indicator',
           'all_2006',
           'all_2016',
           'companies_2006',
           'companies_2016',
           'farmers_and_IE_2006',
           'farmers_and_IE_2016', 
           'farmers_2006',
           'farmers_2016',
           'IE_2006',
           'IE_2016',
           'personal_2006',
           'personal_2016',
           'non_profit_2006',
           'non_profit_2016']


with open('main_results.csv', 'a+') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = columns)
    writer.st.pywriteheader()

with open('main_results.csv', 'a+') as csvfile:
    rowwriter = csv.writer(csvfile, delimiter=',')
    for result in results:
        rowwriter.writerow(result)
