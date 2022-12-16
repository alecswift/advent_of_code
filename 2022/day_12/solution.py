from typing import TextIO
from string import ascii_letters
from itertools import product
from collections import deque

class Node:

    def __init__(self, data):
        location, height = data
        self.location = location
        self.height = height
        self.neighbors = []
        self.parent = None
        self.visited = False

    def add_neightbors(self):
        pass


def parse(input_file: str):
    in_file: TextIO = open(input_file, "r", encoding="utf-8")
    with open(input_file, encoding="utf-8") as in_file:
        input_data: str = in_file.read()
    split_lines = input_data.split("\n")
    split_chars = [list(line) for line in split_lines]
    return split_chars


def build_nodes(input_file):
    input_data = parse(input_file)
    nodes = {}
    for row_num, row in enumerate(input_data):
        for column_num, height in enumerate(row):
            node = Node(((row_num, column_num), ascii_letters.index(height)))
            nodes[(row_num, column_num)] = node
    return nodes


def start_end(nodes):
    for node in nodes.values():
        if node.height == 44:
            node.height = 0
            start = node
        if node.height == 30:
            node.height = 25
            end = node
    return (start, end)


def add_neighbors(nodes):
    cart_product = list(product(nodes, nodes))
    for location_1, location_2  in cart_product:
        row_1, column_1 = location_1
        row_2, column_2 = location_2
        if (
                not ((row_2 - row_1) ** 2 + (column_2 - column_1) ** 2) ** 0.5 - 1
            ):
            if nodes[location_1].height >= (nodes[location_2].height - 1):
                nodes[location_1].neighbors.append(nodes[location_2])

def search(start_and_end):
    start, end = start_and_end
    neighbor_queue = deque([start])
    current_node = start
    while current_node.location != end.location:
        current_node.visited = True
        for neighbor in current_node.neighbors:
            # test out de morgans
            if (neighbor not in neighbor_queue) and (not neighbor.visited):
                neighbor.parent = current_node
                neighbor_queue.append(neighbor)
        neighbor_queue.popleft()
        current_node = neighbor_queue[0]

def shortest_path(end):
    node = end
    count = 0
    while node.parent:
        node = node.parent
        count += 1
    return count
            


test_nodes = build_nodes('2022/day_12/input.txt')
start_1, end_1 = start_end(test_nodes)
add_neighbors(test_nodes)
search((start_1, end_1))
print(shortest_path(end_1))

