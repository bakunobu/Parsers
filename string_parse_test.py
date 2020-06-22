import numpy as np


test_string = 'птица,х х,160963 322229,156 975,118 952 597 1075,22 26,118 40'

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
        preprocessed = [test_string[0]]
        test_string = [x for x in test_string if len(x) > 1]
        print(test_string)
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
        print(test_string)
        preprocessed = [test_string[0]]
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
    
    
    print(preprocessed)

string_parser(test_string)