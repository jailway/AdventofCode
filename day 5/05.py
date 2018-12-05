def load_data():
    with open('05_input.txt', 'r') as f:
        return f.read().strip()


data = list(load_data())

i = 0
while i < len(data) - 2:
    if abs(ord(data[i]) - ord(data[i+1])) == 32:
        data.pop(i+1)
        data.pop(i)
        i -= 1
    else:
        i += 1

print('Answer to star 1 is: ', len(data))

