import numpy as np
# from bokeh.plotting import figure, show, output_notebook

def generate_maze(n, m):
    # maze skeleton
    maze = np.tile([[1, 2], [2, 0]], (n // 2 + 1, m // 2 + 1))
    maze = maze[:-1, :-1]

    cells = {(i, j): (i, j) for i, j in np.argwhere(maze == 1)}
    walls = np.argwhere(maze == 2)

    # union-find
    def find(p, q):
        if p != cells[p] or q != cells[q]:
            cells[p], cells[q] = find(cells[p], cells[q])
        return cells[p], cells[q]

    # find spanning tree
    np.random.shuffle(walls)
    for wi, wj in walls:
        if wi % 2:
            p, q = find((wi - 1, wj), (wi + 1, wj))
        else:
            p, q = find((wi, wj - 1), (wi, wj + 1))

        maze[wi, wj] = p != q
        if p != q:
            cells[p] = q

    return maze


maze = generate_maze(4, 8)

print("Maze generated \n {}".format(maze))

# output_notebook()
#
# plot = figure(x_range=(0, 1), y_range=(0, 1),
#               plot_height=410, plot_width=810)
# plot.axis.visible = False
# plot.outline_line_color = '#ffffff'
# plot.image([maze], x=0, y=0, dw=1, dh=1, palette=['#228B22', '#ffffff'])
#
# show(plot)
