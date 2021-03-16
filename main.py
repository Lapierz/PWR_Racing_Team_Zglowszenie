from path_color_enum import Color
import numpy as np

# Graph
vertices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

edges = [[1, 2, Color.GREEN, 5.0], [1, 4, Color.GREEN, 2.2],
         [2, 3, Color.YELLOW, 5.0], [2, 6, Color.RED, 3.3],
         [3, 8, Color.YELLOW, 3.5],
         [4, 5, Color.YELLOW, 1.7], [4, 13, Color.RED, 7.8],
         [5, 6, Color.GREEN, 3.7], [5, 11, Color.YELLOW, 4.2],
         [6, 7, Color.RED, 1.3], [7, 8, Color.YELLOW, 3.8], [7, 9, Color.RED, 2.0],
         [9, 10, Color.RED, 3.8], [9, 11, Color.GREEN, 3.5],
         [10, 12, Color.RED, 3.0],
         [11, 12, Color.YELLOW, 7.5], [11, 13, Color.GREEN, 4.5],
         [12, 14, Color.YELLOW, 2.0],
         [13, 14, Color.GREEN, 10.0]]


def take_real_positive_number_input(text):
    while True:
        value = input(text)
        try:
            parsed_value = float(value)
            if parsed_value < 0:
                print("Entered value was less than 0!")
            else:
                return parsed_value
        except ValueError:
            print("Entered value was not a number!")


def get_weights():
    red_weight = take_real_positive_number_input("Enter red path weight: ")
    yellow_weight = take_real_positive_number_input("Enter yellow path weight: ")
    green_weight = take_real_positive_number_input("Enter green path weight: ")

    return red_weight, yellow_weight, green_weight


def prepare_adj_matrix(number_of_vertices, e):
    adj_matrix = np.ones(shape=(number_of_vertices, number_of_vertices))
    adj_matrix = adj_matrix * -1

    red_weight, yellow_weight, green_weight = get_weights()

    for edge in e:
        first_vertex = edge[0] - 1
        second_vertex = edge[1] - 1
        road_color = edge[2]

        if road_color == Color.RED:
            color_weight = red_weight
        elif road_color == Color.YELLOW:
            color_weight = yellow_weight
        else:
            color_weight = green_weight

        weight = edge[3] * color_weight
        adj_matrix[first_vertex][second_vertex] = weight
        adj_matrix[second_vertex][first_vertex] = weight

    return adj_matrix


def compute_dijkstra_array(v, adj_matrix, index_of_start_vertex):
    unvisited = v

    vertices_length = len(v)
    visitation_matrix = np.zeros(shape=(vertices_length, 3))

    for i in range(0, vertices_length):
        visitation_matrix[i][0] = v[i]
        visitation_matrix[i][1] = -1

    visitation_matrix[index_of_start_vertex][1] = 0

    while len(unvisited) > 0:
        smallest_unvisited_path = min([i[1] for i in visitation_matrix if i[1] >= 0 and i[0] in unvisited])
        vertex_with_smallest_path = [i for i in visitation_matrix if i[1] == smallest_unvisited_path and i[0] in unvisited]

        unvisited.remove(vertex_with_smallest_path[0][0])
        index = int(vertex_with_smallest_path[0][0] - 1)

        for idx, weight in enumerate(adj_matrix[index]):
            if weight >= 0:
                if visitation_matrix[idx][1] == -1 or visitation_matrix[idx][1] > visitation_matrix[index][1] + weight:
                    visitation_matrix[idx][1] = visitation_matrix[index][1] + weight
                    visitation_matrix[idx][2] = index + 1

    return visitation_matrix


def compute_shortest_path(v, e, start_vertex_index, end_vertex_index):
    adj_matrix = prepare_adj_matrix(len(v), e)
    visitation_matrix = compute_dijkstra_array(v, adj_matrix, start_vertex_index)

    path = ""
    path_cost = visitation_matrix[end_vertex_index][1]
    current_index = int(end_vertex_index)

    while current_index != start_vertex_index:
        path += str(current_index + 1) + "<-"
        current_index = int(visitation_matrix[current_index][2]) - 1

    path += str(start_vertex_index + 1)

    print("\nMinimum traversal cost:")
    print(path_cost)
    print("\nTraversal path:")
    print(path)


compute_shortest_path(vertices, edges, 13, 1)
