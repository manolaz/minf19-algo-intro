import os
import io

# algorithm start from here
# 1.make graph diagram.txt

def coordinate_parser(pos, len_col):
    p_row = pos//col
    p_col = pos%col
    return {"row": p_row, "col": p_col}

def is_vertex(point, len_row):
    position = point.get('position')
    neigbors = 0
    pos_up = position - len_row
    pos_down = position + len_row
    pos_left = position - 1
    pos_right = position + 1

def is_point(pos, matrix):
    neigbors = 0
    is_point = False
    return is_point


def edge_member(point, edge_list):
    connections = 0
    if connections == 2:
        return True
    else:
        return False

def graph_serialiser(line, row_index, len_row):
    ser_line = []
    init_col = 1
    for i in line:
        pos = row_index * len_row + init_col
        # make this point is walkable
        if i == ".":
            point = True
        else:
            point = False
        point = {pos:point}
        ser_line.append(point)
        # increase the column index
        init_col += 1
    return ser_line


# 2. Find the shortest path

def graph_load():
    num_row = 0
    len_row = 0
    start_pos = -1
    exit_pos = -1
    matrix = []
    file_path = input("File path :") + ".txt"
    print(file_path)
    f = open(file_path, "r")
    row_index = 0
    maze_row = 0
    for line in f:
        line_data = line.rstrip()
        if row_index == 0 :
            num_row = int(line_data)
            print(num_row)
        elif row_index == 1:
            len_row = int(line_data)
        elif row_index < num_row + 2:
            row = graph_serialiser(line_data, maze_row, len_row)
            matrix.append(row)
            maze_row += 1
        elif row_index == num_row + 2:
            start_pos = int (line_data)
        elif row_index == num_row + 3 :
            exit_pos = int (line_data)
        row_index += 1
    f.close()
    return {"num_row" :num_row,
    "len_row": len_row,
    "start_pos": start_pos,
    "exit_pos": exit_pos,
    "graph": matrix}


def main():
    # Get data
    file = graph_load()
    graph = file.get("graph")
    print(file.get("num_row"))
    print(file.get("len_row"))
    print(file.get("start_pos"))
    print(file.get("exit_pos"))
    for line in graph:
        print(line)

if __name__ == '__main__':
    main()
