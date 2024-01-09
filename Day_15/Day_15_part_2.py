from Advent_Utils.utils import load_data
from Day_15_part_1 import hash_str


def get_label(input_str: str) -> str:
    if "=" in input_str:
        str_to_hash = input_str.split("=")[0]
    else:
        str_to_hash = input_str.split("-")[0]
    return str_to_hash


def get_box_focussing_power(box_index, box, box_order):
    box_multiplier = box_index+1
    box_power = 0
    for lens in box.items():
        box_power += box_multiplier * int(lens[1]) * box_order.index(lens[0])

    return box_power


def main():
    data = load_data()[0].split(',')
    boxes = []
    boxes_orders = []
    for i in range(256):
        boxes.append({})
        boxes_orders.append([])
    for elem in data:
        label = get_label(elem)
        box_index = hash_str(label)
        if "=" in elem:
            if label not in boxes_orders[box_index]:
                boxes_orders[box_index].append(label)
            boxes[box_index][label] = elem.split("=")[1]
        else:
            if label in boxes[box_index].keys():
                boxes[box_index].pop(label)
                boxes_orders[box_index].remove(label)

    total_focussing_power = 0
    for i in range(256):
        total_focussing_power += get_box_focussing_power(i, boxes[i], boxes_orders[i])

    return total_focussing_power


if __name__ == '__main__':
    print(main())
