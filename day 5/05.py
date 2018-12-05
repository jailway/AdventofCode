def load_data():
    with open('05_input.txt', 'r') as f:
        return f.read().strip()


data = list(load_data())

i = 0
while i < len(data) - 2:
    if (data[i].capitalize() == data[i + 1].capitalize()) and (
            data[i].isupper() != data[i + 1].isupper()):
        del data[i:i + 2]
        i -= 1
    else:
        i += 1

print('Answer to star 1 is: ', len(data))

