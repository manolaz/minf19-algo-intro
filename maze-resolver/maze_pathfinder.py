import os
import io

def coordinate_parser(pos, len_col):
    p_row = pos//col
    p_col = pos%col
    return {"row": p_row, "col": p_col}

def is_vertex(point, graph, len_row):
    neigbors = 0
    pos_up = point - len_row
    pos_down = point + len_row
    pos_left = point - 1
    pos_right = point + 1

    if graph.get(pos_up):
        neigbors += 1
    if graph.get(pos_down):
        neigbors += 1
    if graph.get(pos_left):
        neigbors += 1
    if graph.get(pos_right):
        neigbors += 1
    # this is not a Vertex only when having only 2 neigbors
    if neigbors == 2:
        return False
    return True


def edge_member(point, edge_list):
    connections = 0
    if connections == 2:
        return True
    else:
        return False

def graph_serializer(line, row_index, len_row):
    ser_line = {}
    init_col = 1
    for i in line:
        pos = row_index * len_row + init_col
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
    num_row = 0
    len_row = 0
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
            num_row = int(line_data)
        elif row_index == 1:
            len_row = int(line_data)
        elif row_index < num_row + 2:
            row = graph_serializer(line_data, maze_row, len_row)
            # graph.extend(row)
            graph.update(row)
            maze_row += 1
        elif row_index == num_row + 2:
            start_pos = int (line_data)
        elif row_index == num_row + 3 :
            exit_pos = int (line_data)
        row_index += 1
    f.close()
    return {
            "num_row" :num_row,
            "len_row": len_row,
            "start_pos": start_pos,
            "exit_pos": exit_pos,
            "graph": graph
            }


def main():
    file = graph_load()
    graph = file.get("graph")
    g_height = (file.get("num_row"))
    g_width = (file.get("len_row"))
    source = (file.get("start_pos"))
    target = (file.get("exit_pos"))
    edge_list = []
    for point in graph.keys():
        if is_vertex(point, graph, g_width):
            edge_list.append(point)
            print("position {}, on path ? = {}".format(point, graph[point]))
if __name__ == '__main__':
    main()
