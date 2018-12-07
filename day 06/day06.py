def load_data() -> [(int, int)]:
    """
    Loads points coordinates from input file

    :return: Cooordinates array of tuples
    """
    coords = []
    with open('06_input.txt', 'r') as f:
        for l in f.readlines():
            x, y = l.split(", ")
            coords.append((int(x), int(y)))
    return coords


def distance(refpoint: (int, int), destpoint: (int, int)) -> int:
    """
    Calculates Manhattan distance between two points

    :param refpoint: Reference point coordinates as a tuple
    :param destpoint: Distance point coordinates as a tuple
    :return: Integer distance
    """
    return abs(refpoint[0] - destpoint[0]) + abs(refpoint[1] - destpoint[1])


def get_closest(coords: [(int, int)], point: (int, int)):
    """
    Get reference to the index of closest point in coordinates list

    :param coords: List of coordinates
    "param point: Tested point
    :return: Index of the closes point, -1 if a tie or does not exist
    """
    c_dist = -1
    c_i = -1
    tie = False
    for i, c in enumerate(coords):
        dist = distance(point, c)
        if c_dist == -1 or c_dist > dist:
            c_dist = dist
            c_i = i
            tie = False
        elif c_dist == dist:
            tie = True
    if tie:
        return -1
    return c_i


def get_boundary(coords: [(int, int)]) -> [(int, int)]:
    """
    Gets bounding rectangle or the coordinates

    :param coords: Points coordinates list
    :return: Bounding rectangle coordinates
    """
    return [(min([i[0] for i in coords]), min([i[1] for i in coords])),
            (max([i[0] for i in coords]), max([i[1] for i in coords]))]


def grid_of_closest(coords: [(int, int)]):
    """
    Fills a grid with references to the closest point

    :param coords: a list of points coordinates
    :param boundary: a bounding rectangle
    :return: a grid with ID's of closest points
    """
    boundary = get_boundary(coords)
    grid = {}
    for x in range(boundary[0][0], boundary[1][0]+1):
        for y in range(boundary[0][1], boundary[1][1]+1):
            grid[(x, y)] = get_closest(coords, (x, y))
    return grid


def largest_area_size(grid: dict):
    """
    Calculates the size of the largest area in the grid

    :param grid: grid of closest points
    :return: size of the largest area in the grid
    """
    boundary = get_boundary(coords)
    area_sizes = dict()
    ignored = set()
    ignored.add(-1)

    for x in range(boundary[0][0], boundary[1][0]+1):
        for y in range(boundary[0][1], boundary[1][1]+1):

            if x == boundary[0][0] or x == boundary[1][0] or y == boundary[0][1] or y == boundary[1][1]:
                ignored.add(grid[(x, y)])
            if grid[(x, y)] not in area_sizes.keys():
                area_sizes[grid[(x, y)]] = 0

            area_sizes[grid[(x, y)]] += 1

    largest_size = -1
    largest_area = -1
    for area, size in area_sizes.items():
        if size > largest_size and area not in ignored:
            largest_size = size
            largest_area = area

    return largest_size


if __name__ == "__main__":
    coords = load_data()
    print(largest_area_size(grid_of_closest(coords)))
