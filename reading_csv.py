import numpy as np


with open('test.csv', 'r') as f:
    lines = [line for line in f]
    for line in lines[:10]:
        if line[:2] == '""':
            print('skipping')
        elif line[0] == '"':
            line = line[1:].split('"')
            line.remove('\n')
            while ',' in line:
                line.remove(',')
            preprocessed = [line[0]]
            for el in line[1:]:
                el = el.replace(',', '.')
                el = el.split()
                for x in el:
                    print(type(x))
                    x.replace(',', '.')
                    print(x)
                    try:
                        i = float(x)
                        preprocessed.append(i)
                    except:
                        if x == ',,':
                            pass
                        else:
                            preprocessed.append(np.NaN)
    print(preprocessed)
                
            


'''
with open('test.csv', 'r') as f:
    lines = [line for line in f if line[:2] != '""']
    for line in lines:
        if line[0] ==  '"':
            line.replace('\n', '')
            data = line.split('"')
            data.pop(0)
            data.pop()
            prepared_data = [data[0]]
            for x in data[1:]:
                if ',х х,,' in x:
                    for i in range(2):
                        prepared_data.append(np.NaN)
                elif x == ',':
                    pass
                else:
                    x.replace(',', '.')
                    x.split(' ')
                    for i in range(2):
                        prepared_data.append(int(x[i]))
        print(* prepared_data)
'''