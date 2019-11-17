import os
import io

def coordinate_parser(pos, width):
    p_row = pos//width
    p_col = pos%width
    return {"row": p_row, "col": p_col}


def calc_level(point, graph, height, width):
    level = 0
    # check only point
    if graph[point]:
        if point <= height * (width - 1):
            pos_down = point + width
            if graph[pos_down]:
                level += 1

        if point > width:
            pos_up = point - width
            if graph[pos_up]:
                level += 1

        if point%width > 0:
            pos_right = point + 1
            if graph[pos_right]:
                level += 1

        if point%width > 1:
            pos_left = point - 1
            if graph[pos_left]:
                level += 1
    # level of this point
    return level


def is_vertex(point, level, graph, start , stop):
    # check only point
    if graph[point]:
        # this is not a Vertex only when having only 2 neigbors
        if level == 2:
            # exception when this point was chosen as SOURCE or TARGET
            if point == start or point == stop:
                return True
            else:
                return False
        else:
            return True

def weight_calculate(start, stop):
    weight = 1
    h_start = start//width
    h_stop = stop//width
    col_start = start%
    # two verticle on same row
    if h_start == h_stop:
        weight = stop - start
    else:
        weight = h_stop - h_start
    edge = (stop, weight)
    return edge

# to complete
def to_adjacent_list(vertices_list):
    for vertex in vertices_list:
        coordinate_parser(pow, width)



def graph_serializer(line, row_index, width):
    ser_line = {}
    init_col = 0
    for i in line:
        pos = row_index * width + init_col
        # make this point is walkable
        if i == ".":
            point = True
        else:
            point = False
        ser_line[pos] = point
        # increase the column index
        init_col += 1
    return ser_line


def graph_load():
    height = 0
    width = 0
    start_pos = -1
    exit_pos = -1
    graph = {}
    file_path = input("File path :") + ".txt"
    f = open(file_path, "r")
    row_index = 0
    maze_row = 0
    for line in f:
        line_data = line.rstrip()
        if row_index == 0 :
            height = int(line_data)
        elif row_index == 1:
            width = int(line_data)
        elif row_index < height + 2:
            row = graph_serializer(line_data, maze_row, width)
            # graph.extend(row)
            graph.update(row)
            maze_row += 1
        elif row_index == height + 2:
            start_pos = int(line_data)
        elif row_index == height + 3 :
            exit_pos = int(line_data)
        row_index += 1
    f.close()
    return {
            "height" :height,
            "width": width,
            "start_pos": start_pos,
            "exit_pos": exit_pos,
            "graph": graph
            }


def main():
    file = graph_load()
    graph = file.get("graph")
    g_height = int(file.get("height"))
    g_width = int(file.get("width"))
    source = file.get("start_pos")
    target = file.get("exit_pos")
    edge_list = []
    vertices_list = []
    for point in graph.keys():
        level = calc_level(point, graph, g_height, g_width)
        print("Point {} : level {}".format(point, level))
        if is_vertex(point, level, graph, source, target):
            vertices_list.append(point)
            # print("position {}={}".format(point, graph[point]))
    print("vertices_list : {}".format(vertices_list))
if __name__ == '__main__':
    main()
