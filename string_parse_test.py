import numpy as np


test_string = '"Число организаций (хозяйств) - всего, тыс.",х х,,"59,2 36,0","285,1 174,8","253,1 136,7","32,0 38,0","22799,4 23496,9","80,3 75,9"'
def string_parser(test_string):
    
    if test_string[:2] == '""':
        print('PASS!')
    
    elif test_string[:1] == '"':
        preprocessed = []
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
        print(preprocessed)

string_parser(test_string)