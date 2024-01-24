from Advent_Utils.utils import load_data
from math import inf

data = []
shortest_path_data = []
available_nodes: set[tuple[int, int]] = set()
nodes_with_value: set[tuple[int, int]] = set()


def get_node_connections(node: tuple[int, int]) -> list[tuple[int, int]]:
    connections = []
    for offset in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        new_position = (node[0] + offset[0], node[1] + offset[1])
        if new_position in available_nodes:
            connections.append(new_position)
    return connections


def do_all_paths_from_node(node: tuple[int, int]) -> None:
    global shortest_path_data
    # TODO add logic so that len of straight path <= 3
    available_nodes.remove(node)
    connections = get_node_connections(node)
    if not connections:
        return
    for path in connections:
        nodes_with_value.add(path)
        path_length = shortest_path_data[node[0]][node[1]] + data[path[0]][path[1]]
        if shortest_path_data[path[0]][path[1]] > path_length:
            shortest_path_data[path[0]][path[1]] = path_length


def main():
    global data, shortest_path_data
    data = load_data(17, 2023, False)
    for i, line in enumerate(data):
        data[i] = []
        for j, char in enumerate(line):
            data[i].append(int(char))
            available_nodes.add((i, j))
    shortest_path_data = [[inf]*len(data[0])]*len(data)


if __name__ == '__main__':
    main()
