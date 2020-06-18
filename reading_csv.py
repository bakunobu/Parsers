with open('test.csv', 'r') as f:
    lines = [line for line in f if line[:2] != '""']
    for line in lines[:10]:
        print(line)