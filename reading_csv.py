import numpy as np


def read_raw_data(my_file):
    pass


def pair_to_int(pair, my_list):
    
    for x in pair:
        try:
            i = float(x)
            my_list.append(i)
        except:
            if x == ',,':
                pass
            else:
                my_list.append(np.NaN)



with open('test.csv', 'r') as f:
    lines = [line for line in f]
    for line in lines[:50]:
        
        if line[:2] == '""':
            print('skipping')
        
        elif ',,,' in line:
            print('too many commas')
        
        elif line[0] == '"':
            line = line[1:].split('"')
            if '\n' in line:
                line.remove('\n')
            
            while ',' in line:
                line.remove(',')
            preprocessed = [line[0].replace(',', '')]
            
            for el in line[1:]:
                el = el.replace(',', '.')
                el = el.split()
                
                for x in el:
                    
                    try:
                        i = float(x)
                        preprocessed.append(i)
                    
                    except:
                        
                        if x == ',,':
                            pass
                        
                        else:
                            preprocessed.append(np.NaN)

            print(preprocessed)
            
        elif '"' in line:
            line = line.split('"')
            if '\n' in line:
                line.remove('\n')
            
            while ',' in line:
                line.remove(',')
            preprocessed = [line[0].replace(',', '')]
            
            for el in line[1:]:
                el = el.replace(',', '.')
                el = el.split()
                
                for x in el:
                    
                    try:
                        i = float(x)
                        preprocessed.append(i)
                    
                    except:
                        
                        if x == ',,':
                            pass
                        
                        else:
                            preprocessed.append(np.NaN)

            print(preprocessed)
        else:
            line = line.split('"')
            if '\n' in line:
                line.remove('\n')
            preprocessed = [line[0].replace(',', '')]
            for el in line[1:]:
                el = el.split()
                
                for x in el:
                    
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