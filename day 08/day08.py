def load_data(file: str) -> [int]:
    """
    Loads tree nodes description from input file

    :return: set of tree nodes descriptions
    """
    with open(file, 'r') as f:
        return list(int(i) for i in f.read().split(' '))


def read_metadata(input: [int], position: int = 0) -> (int, [int]):
    """
    Reads metadata recursively

    :param input: input list of nodes
    :param position: starting position in the list (default 0)
    :return: tuple (length of the node, list of metadata)
    """
    metalength = input[position + 1]
    metadata = []
    length = 2
    for i in range(0, input[position]):
        l, m = read_metadata(input, position + length)
        length += l
        metadata.extend(m)
    metadata.extend(input[position + length:position + length + metalength])
    length += metalength
    return length, metadata


if __name__ == "__main__":
    data = load_data('08_input.txt')
    x = read_metadata(data)
    print(sum(x[1]))
