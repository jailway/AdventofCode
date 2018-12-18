def power_level(x: int, y: int, serial: int) -> int:
    rack_id = x + 10
    power_level = rack_id * y
    power_level += serial
    power_level *= rack_id
    return int(str(power_level)[-3]) - 5


def power_grid(size_x: int, size_y: int, serial: int) -> [int, int]:
    grid = [[0 for x in range(0, size_x)] for y in range(0, size_y)]

    for x in range(1, size_x + 1):
        for y in range(1, size_y + 1):
            grid[x - 1][y - 1] = power_level(x, y, serial)

    return grid


def find_max_subgrid(grid: [int, int], subgrid_size: int = 3) -> [int, int, int]:
    max_value = -5 * subgrid_size ^ 2
    max_x = 0
    max_y = 0

    gridsize = len(grid)

    for big_x in range(0, gridsize - subgrid_size + 1):
        for big_y in range(0, gridsize - subgrid_size + 1):
            val = sum(
                [grid[small_x][small_y] for small_x in range(big_x, big_x + subgrid_size) for small_y in
                 range(big_y, big_y + subgrid_size)])
            if val > max_value:
                max_value = val
                max_x, max_y = big_x, big_y

    return max_x + 1, max_y + 1, max_value


def find_max_subrid_anysize(grid: [int, int]) -> [int, int, int]:
    gridsize = len(grid)
    max_val = 0
    max_size = 0
    max_x = 0
    max_y = 0
    for s in range(1, gridsize + 1):
        x, y, val = find_max_subgrid(grid, s)
        if val > max_val:
            max_x, max_y, max_size, max_val = x, y, s, val
    return max_x, max_y, max_size, max_val


if __name__ == "__main__":
    grid = power_grid(300, 300, 1788)
    print(find_max_subgrid(grid, 3))
    print(find_max_subrid_anysize(grid))

