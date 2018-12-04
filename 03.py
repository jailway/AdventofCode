import pandas

data = pandas.read_csv('c:\\temp\\advent\\input_3_1.csv', header=None, sep='[#@,:x ]', usecols=[1, 4, 5, 7, 8]) #, index_col= 0 )
#print(data.head())

fabric = [[0]*1000]*1000

for index, row in data.iterrows():
    for y in range(row[5], row[5] + row[8]):
        for x in range(row[4], row[4] + row[7]):
            fabric[y][x] += 1

cnt = 0
for x in range(0, 999):
    for y in range(0,999):
        if fabric [y][x] >=2: cnt+=1

print(cnt)


