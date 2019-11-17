import os
import io

def coordinate_parser(pos, width):
    p_row = pos//width
    p_col = pos%width
    return {"row": p_row, "col": p_col}

def calc_neigbors(point, graph, height, width):
    neigbors = 0

    # check only point
    if graph[point]:
        if point <= height * (width - 1):
            pos_down = point + width
            if graph[pos_down] and point > width:
                neigbors += 1

        if point > width:
            pos_up = point - width
            if graph[pos_up]:
                neigbors += 1

        if point%width > 0:
            pos_right = point + 1
            if graph[pos_right]:
                neigbors += 1

        if point%width > 1:
            pos_left = point - 1
            if graph[pos_left]:
                neigbors += 1

    return neigbors

def is_vertex(graph, point, level):
    # check only point
    if graph[point]:
        # this is not a Vertex only when having only 2 neigbors
        if level == 2:
            return False
        else:
            return True

def edge_member(point, edge_list):
    connections = 0
    if connections == 2:
        return True
    else:
        return False

def graph_serializer(line, row_index, width):
    ser_line = {}
    init_col = 1
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
            start_pos = int (line_data)
        elif row_index == height + 3 :
            exit_pos = int (line_data)
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
    g_height = (file.get("height"))
    g_width = (file.get("width"))
    source = (file.get("start_pos"))
    target = (file.get("exit_pos"))
    edge_list = []
    vertices_list = []
    for point in graph.keys():
        level = calc_neigbors(point, graph, g_height, g_width)
        print("Point {} : level {}".format(point, level))
        if is_vertex(graph, point, level):
            vertices_list.append(point)
            # print("position {}={}".format(point, graph[point]))
    print("vertices_list : {}".format(vertices_list))
if __name__ == '__main__':
    main()
