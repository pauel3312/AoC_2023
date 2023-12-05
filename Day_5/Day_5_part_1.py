import threading

file = "input.txt"
path = ["seed", "soil", "fertilizer", "water", "light", "temperature", "humidity", "location"]

maps = {}


def parse_file():
    returns = []
    f = open(file, "r")
    for current_map in (f.read().split("\n\n")):
        returns.append(current_map.split(":"))
    f.close()
    return returns


def get_maps():
    file_contents = parse_file()
    default_map = {}
    threads = []
    for i in range(int(10e15)):
        default_map[str(i)] = str(i)
    for current_map_compressed in file_contents[1:]:
        thread = threading.Thread(target=get_map, args=(default_map, current_map_compressed))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    return maps


def get_map(default_map, current_map_compressed):
    global maps
    final_map = default_map.copy()
    map_name = current_map_compressed[0].split(" ")[0]
    map_amendments = current_map_compressed[1][1:].split("\n")
    for amendment in map_amendments:
        values = amendment.split(" ")
        for i in range(int(values[2])):
            final_map[str(int(values[1])+i)] = str(int(values[0])+i)
    maps[map_name] = final_map


seeds = parse_file()[0][1][1:].split(" ")
Maps = get_maps()
print("maps get")
minimum = 100
s = None
for seed in seeds:
    s = seed
    for index in range(1, len(path)):
        category = path[index]
        map_to_use = f"{path[index-1]}-to-{category}"
        s = Maps[f"{path[index-1]}-to-{category}"][s]
    if minimum > int(s):
        minimum = int(s)

print(minimum)
