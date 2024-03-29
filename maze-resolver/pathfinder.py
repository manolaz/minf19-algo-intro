# from itertools import izip
import traceback
from heapq import heappush, heappop
import numpy as np
import networkx as nx

# import matplotlib.pyplot as plt

# from networkx.drawing.nx_pydot import write_dot


def follow_path(start, stop, graph, width, virtuals):
    weight = 0
    destination = start
    if graph.get(destination) == 123:
        weight += 1
        while graph.get(start) is True:
            destination += 1
    if graph.get(destination) == 129:
        weight -= 1
        while graph.get(destination) is True:
            destination -= 1
    if graph.get(destination) == 63:
        weight += weight
        while graph.get(destination) is True:
            destination += width
    if graph.get(destination) == 69:
        weight -= weight
        while graph.get(destination) is True:
            destination -= width
    # Recursive call
    if destination == stop:
        return {destination, weight}
    else:
        return None


def weight_calculate(start, stop, width):
    weight = 0
    start = coordinate_parser(start, width)
    stop = coordinate_parser(stop, width)
    # two verticle on same row
    if start["row"] == stop["row"]:
        weight = stop["col"] - start["col"]
    # two verticle on same column
    elif start["col"] == stop["col"]:
        weight = stop["row"] - start["row"]
    edge = (stop, weight)
    return edge


def coordinate_parser(pos, width):
    p_row = pos // width
    p_col = pos % width
    return {"row": p_row, "col": p_col}


def is_vertex(height, width, point, graph, start, stop):
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

        if point % width > 0:
            pos_right = point + 1
            if graph[pos_right]:
                level += 1

        if point % width > 1:
            pos_left = point - 1
            if graph[pos_left]:
                level += 1

        # this is not a Vertex only when having only 2 neigbors
        if level == 2:
            # exception when this point was chosen as SOURCE or TARGET
            if point == start or point == stop:
                return True

            # find virtual Vertex
            # identifier as Watch face directions
            if (point > width) and graph[pos_up]:
                if (point % width > 1) and graph[pos_left]:
                    return 129
                if (point % width > 0) and graph[pos_right]:
                    return 123
            if (point <= (height * (width - 1) - 1)) and graph[pos_down]:
                if (point % width > 1) and graph[pos_left]:
                    return 69
                if (point % width > 0) and graph[pos_right]:
                    return 63
        # IF level is not 2
        if level != 2:
            if level != 0:
                return True
            else:
                return False
    else:
        return False


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
        if row_index == 0:
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
        elif row_index == height + 3:
            exit_pos = int(line_data)
        row_index += 1
    f.close()
    return {
        "height": height,
        "width": width,
        "start_pos": start_pos,
        "exit_pos": exit_pos,
        "graph": graph,
    }


def build_adjacency_list(vertices, virtuals, width, height):
    adjacent_list = []
    for vertex in vertices:
        links = [vertex]
        for another in vertices.remove(vertex):
            print("Checking path for {} to {} ".format(vertex, another))
            link_weight = weight_calculate(vertex, another, width)
            if link_weight != 0:
                v = {another, link_weight}
                links.append(v)
        adjacent_list.append(links)
    return adjacent_list


def main():
    file = graph_load()
    graph = file.get("graph")
    g_height = int(file.get("height"))
    g_width = int(file.get("width"))
    source = file.get("start_pos")
    target = file.get("exit_pos")
    # edge_list = []
    # angles = []
    vertices_list = []
    virtual_vertices = []

    print("width {}".format(g_width))
    print("Height {}".format(g_height))
    for point in graph.keys():
        try:
            vertex = is_vertex(g_height, g_width, point, graph, source, target)
        except Exception as e:
            print(e)
            traceback.print_exc()

        if vertex is True:
            vertices_list.append(point)
        elif vertex in [123, 129, 63, 69]:
            print("POINT {} , virtual moving {}".format(point, vertex))
            virtual_vertices.append(point)
            # print("position {}={}".format(point, graph[point]))
    print("REAL vertices_list : {}".format(vertices_list))
    print("VIRTUAL vertices : {}".format(virtual_vertices))

    w = weight_calculate(virtual_vertices[0], virtual_vertices[1], g_width)
    print(w)
    # for one in virtual_vertices:
    #     for two in virtual_vertices.remove(one):
    #         w = weight_calculate(one, two, g_width)
    #         print(w)


if __name__ == "__main__":
    main()
