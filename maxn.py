import copy

class Grid:
    def __init__(self, grid_size) -> None:
        self.size = grid_size
        self.blank_grid = [[0 for i in range(grid_size)] for j in range(grid_size)]
        self.grid = self.init_grid(copy.deepcopy(self.blank_grid), grid_size)
        self.nummax = 0
        self.xmax = []
        self.ymax = []
        
    def init_grid(self, grid, n):
        iloc = n // 2
        # 2
        grid[iloc - 1][iloc-1], grid[iloc + 1][iloc + 1] = 1, 1
        # 3
        #grid[iloc - 1][iloc-1], grid[iloc + 1][iloc + 1], grid[iloc + 2][iloc - 3] = 1, 1, 1
        gprint("Starting Position", grid)
        return grid


def gprint(title, grid):
    g = len(grid[0])*3 - 1
    print(f'{" " + title + " ":+^{g}}')
    for i in grid:
        print(" ".join([f"{j:02d}" for j in i]).replace("00",".."))


def reduce_grid(grid):
    igrid = [[grid[j][i] for j,_ in enumerate(grid)] for i,_ in enumerate(grid)]
    c = []
    for g in (grid, igrid):
        for line, line_data in enumerate(g):
            if [i for i in line_data if i != 0]:
                lower_limit = int(line)
                break
        for line, line_data in enumerate(g[::-1]):
            if [i for i in line_data if i != 0]:
                upper_limit = len(grid) - int(line)
                break
        c.append((lower_limit, upper_limit))

    new_grid = [[grid[c[0][0]+i][c[1][0]+j] for j,_ in enumerate(grid[c[1][0]:c[1][1]])] for i,_ in enumerate(grid[c[0][0]:c[0][1]])]
    return new_grid, len(new_grid), len(new_grid[0])

def valid_squares(grid, next):
    G.ogrid = copy.deepcopy(G.blank_grid)
    result = []
    for x in range(1, G.size-1):
        for y in range(1, G.size-1):
            if grid[y][x] == 0:
                s = 0
                for i in range(x-1, x+2):
                    for j in range(y-1, y+2):
                        if (i,j) != (x,y):
                            s += grid[j][i]
                if s == next:
                    result.append((x,y))
                G.ogrid[y][x] = s
    return result


def solve(grid, n):
    for opt in valid_squares(grid, n):
        grid[opt[1]][opt[0]] = n
        solve(grid, n+1)
        if n > G.nummax:
            G.nummax = int(n)
            G.final_grid = copy.deepcopy(grid)
        _, xmax, ymax = reduce_grid(grid)
        G.xmax.append(xmax)
        G.ymax.append(ymax)
        grid[opt[1]][opt[0]] = 0

G = Grid(11)
solve(G.grid, 2)
print(f"\nMax N: {G.nummax} -- Max Grid Size: {max(G.xmax)},{max(G.ymax)}")
gprint("Best Result", reduce_grid(G.final_grid)[0])