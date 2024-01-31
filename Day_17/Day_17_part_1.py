from Advent_Utils.utils import load_data
from math import inf
from typing import Optional


class Position(tuple[int, int]):
    # noinspection PyUnusedLocal
    def __init__(self, *args):
        super().__init__()

    def __sub__(self, other: "Position"):
        return Position((self[0] - other[0], self[1] - other[1]))

    def __rsub__(self, other: "Position"):
        return Position((other[0] - self[0], other[1] - self[1]))

    def __str__(self):
        return super().__str__()


data: list[list[int]] = []
shortest_path_data: list[list[list[int, list[list[Optional[Position]]]]]] = []
available_nodes: set[Position] = set()
nodes_with_value: set[Position] = set()
forbidden_path_sequences: tuple[Position, Position, Position, Position] = (Position((-3, 0)),
                                                                           Position((3, 0)),
                                                                           Position((0, 3)),
                                                                           Position((0, -3)))


def check_positions_list(node: Position, prev_3_positions_list: list[list[Optional[Position]]]) -> bool:
    for prev_3_positions in prev_3_positions_list:
        if (node - prev_3_positions[0]) not in forbidden_path_sequences:
            return True
    return False


def get_node_connections(node: Position, prev_3_positions_list: list[list[Optional[Position]]]) -> list[Position]:
    connections = []
    for offset in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        new_position = Position((node[0] + offset[0], node[1] + offset[1]))
        if new_position in available_nodes:
            if None in [ppl[0] for ppl in prev_3_positions_list]:
                connections.append(new_position)
            elif check_positions_list(node, prev_3_positions_list):
                connections.append(new_position)
    return connections


def cleanup_last_3_list(node: Position) -> None:
    global shortest_path_data
    encountered = []
    to_pop = []
    # noinspection PyTypeChecker
    for i, l3 in enumerate(shortest_path_data[node[0]][node[1]][1]):
        if l3 in encountered:
            to_pop.append(i)
        else:
            encountered.append(l3)

    for i in to_pop:
        shortest_path_data[node[0]][node[1]][1].pop(i)


def do_all_paths_from_node(node: Position) -> None:
    global shortest_path_data
    cleanup_last_3_list(node)
    # noinspection PyTypeChecker
    current_3_previous_positions_list: list[list[Optional[Position]]] = shortest_path_data[node[0]][node[1]][1].copy()
    available_nodes.remove(node)
    connections = get_node_connections(node, current_3_previous_positions_list)
    if not connections:
        return
    for path in connections:
        nodes_with_value.add(path)
        path_length = shortest_path_data[node[0]][node[1]][0] + data[path[0]][path[1]]
        if shortest_path_data[path[0]][path[1]][0] > path_length:
            shortest_path_data[path[0]][path[1]][0] = path_length
            # noinspection PyTypeChecker
            for i in range(len(current_3_previous_positions_list)):
                try:
                    shortest_path_data[path[0]][path[1]][1][i] = list((current_3_previous_positions_list[i][1],
                                                                       current_3_previous_positions_list[i][2],
                                                                       node))
                except IndexError:
                    shortest_path_data[path[0]][path[1]][1].append(list((current_3_previous_positions_list[i][1],
                                                                         current_3_previous_positions_list[i][2],
                                                                         node)))
        elif shortest_path_data[path[0]][path[1]][0] == path_length:
            for prev_3_pos in current_3_previous_positions_list:
                shortest_path_data[path[0]][path[1]][1].append(prev_3_pos.copy())


def get_node_with_lowest_path_length() -> Position:
    return_node = available_nodes.intersection(nodes_with_value).pop()
    current_shortest_path = shortest_path_data[return_node[0]][return_node[1]][0]
    for node in available_nodes.intersection(nodes_with_value):
        if shortest_path_data[node[0]][node[1]][0] < current_shortest_path:
            return_node = node
            current_shortest_path = shortest_path_data[return_node[0]][return_node[1]][0]
    return return_node


def main():
    global data, shortest_path_data
    data = load_data(17, 2023, False)
    for i, line in enumerate(data):
        data[i] = []
        for j, char in enumerate(line):
            data[i].append(int(char))
            available_nodes.add(Position((i, j)))
    for i in range(len(data)):
        shortest_path_data.append([])
        for j in range(len(data[0])):
            # noinspection PyTypeChecker
            shortest_path_data[i].append([inf, [[None, None, None], ]])
    shortest_path_data[0][0][0] = data[0][0]
    nodes_with_value.add(Position((0, 0)))
    while available_nodes:
        try:
            do_all_paths_from_node(get_node_with_lowest_path_length())
        except KeyError:
            break
    return shortest_path_data[-1][-1][0]


if __name__ == '__main__':
    print(main())
