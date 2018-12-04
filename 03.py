import pandas

data = pandas.read_csv('03_data.txt', header=None, sep='[#@,:x ]', usecols=[1, 4, 5, 7, 8], names=['i', 'x', 'y', 'w', 'h']) #, index_col= 0 )
#print(data.head())

fabric = [[0 for x in range(1000)] for y in range(1000)]

for index, row in data.iterrows():
    for y in range(row['y'], row['y'] + row['h']):
        for x in range(row['x'], row['x'] + row['w']):
            fabric[x][y] += 1

cnt = 0
for x in range(0, 1000):
    for y in range(0,1000):
        if fabric [y][x] >=2: cnt+=1

print('answer to star 1 is ' + str(cnt))

for index1, square1 in data.iterrows():
    overlaps = 0
    for index2, square2 in data.iterrows():
        if square1['i'] != square2['i']:
            if square1['x'] <= square2['x'] + square2['w'] and square2['x'] <= square1['x'] + square1['w']:
                if square1['y'] <= square2['y'] + square2['h'] and square2['y'] <= square1['y'] + square1['h']:
                    overlaps += 1
    if overlaps == 0:
        print('answer to star 2 is ' + str(square1['i']))
