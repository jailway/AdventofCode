def load_data(file: str):
    """
    Loads tree nodes description from input file

    :return: set of tree nodes descriptions
    """
    with open(file, 'r') as f:
        ini = f.readline().lstrip("initial state: ").strip()
        f.readline()
        inst = dict()
        for s in f.readlines():
            cond, res = s.split(" => ")
            inst[cond] = res.strip()

    return ini, inst


def step(state: str, offset: int, instr: {str, str}) -> (str, int):
    s = '...' + state + '...'
    sout = list('.' * len(s))
    for i in range(2, len(s) - 2):
        pattern = s[i - 2:i + 3]
        if pattern in instr.keys() and instr[pattern] == "#":
            sout[i] = "#"
    # clean output string of zeros at ends

    first = 0
    while first < len(sout):
        if sout[first] == ".":
            first += 1
        else:
            break

    last = len(sout) - 1
    while i > 0:
        if sout[last] == ".":
            last -= 1
        else:
            break

    return ''.join(sout[first:last + 1]), offset + first - 3


def calcpoints(state: str, offset: int) -> int:
    points = 0
    for i in range(0, len(state)):
        if state[i] == "#":
            points += i + offset
    return points


if __name__ == "__main__":
    state, instruct = load_data("input.txt")
    print(state)
    print(instruct)
    offset = 0
    for i in range(0, 200):
        (state, offset) = step(state, offset, instruct)
        print(state, offset, i)

    print(calcpoints(state, offset +50000000000 - 200))
