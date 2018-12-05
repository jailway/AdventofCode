def load_data():
    with open('05_input.txt', 'r') as f:
        return f.read().strip()

def collapse(data: list) -> list:
    i = 0
    while i < len(data) - 1:
        if abs(ord(data[i]) - ord(data[i + 1])) == 32:
            data.pop(i + 1)
            data.pop(i)
            i = max(i - 1, 0)
        else:
            i += 1
    return data

polymer = list(load_data())

print('Answer to star 1 is: ', len(collapse(polymer)))



