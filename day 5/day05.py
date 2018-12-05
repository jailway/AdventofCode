def load_data():
    """
    Loads data from input file

    :return: Polymer read as string
    """
    with open('05_input.txt', 'r') as f:
        return f.read().strip()


def collapse(polymer: str) -> str:
    """
    Collapses polymer string as per instruction on Day 5

    :param polymer: Input polymer as a string
    :return: Colapsed polymer string according to rules
    >>> collapse('dabAcCaCBAcCcaDA')
    'dabCBAcaDA'

    """
    test = list(polymer)
    i = 0
    while i < len(test) - 1:
        if abs(ord(test[i]) - ord(test[i + 1])) == 32:
            test.pop(i + 1)
            test.pop(i)
            i = max(i - 1, 0)
        else:
            i += 1
    return ''.join(test)


def leave_out(polymer: str) -> dict:
    """
    Tests leaving out individual letters in aplphabet on polymer string input, and collapsing it

    :param polymer: Input polymer as a string
    :return: Dictionary containing results pairs (Input Letter):(Length of reduced polymer)
    """
    res = dict()
    for c in range(ord("a"), ord("z") + 1):
        ch = chr(c)
        res[ch] = len(collapse(polymer.replace(ch, '').replace(ch.upper(), '')))
    return res


if __name__ == "__main__":
    data = load_data()
    print('Answer to star 1 is: ', len(collapse(data)))

    tst = leave_out(data)
    print('Answer to star 2 is: ', min(tst.values()), ' on letter: ', min(tst, key=tst.get))
