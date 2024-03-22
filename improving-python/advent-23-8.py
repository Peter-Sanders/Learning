def get_data(file):

    with open(file , 'r') as f:
        lines = [x.replace('\n', '') for x in f.readlines() if x != '\n']
        instructions = lines [0]
        lines.pop(0)
    return instructions, lines


def build_dict(data):
    node_dict = {}
    for i, node_route in enumerate(data):
        splits = node_route.split('=')
        node = splits[0].strip()
        route = [x.strip() for x in splits[1].strip().replace('(', '').replace(')', '').split(',')]
        node_dict[node] = route
        if i == 0:
            start_node = node
    return node_dict, start_node


def traverse_node(step, current_node, instructions, instructions_dir, node_dict):
    for inst in instructions:
        current_node = node_dict.get(current_node)[instructions_dir.get(inst)]
        step += 1
    return step, current_node


def solution(file, instructions_dir, target_node):
    instructions, data = get_data(file)
    node_dict, start_node = build_dict(data)

    step = 0
    while start_node != target_node:
        step, start_node = traverse_node(step, start_node, instructions, instructions_dir, node_dict)
    return step


if __name__ == "__main__":
    instructions_dir = {
            'R':1,
            'L':0,
            }
    file = 'advent-storage/advent-23-8.txt'
    target_node = 'ZZZ'
    print(solution(file, instructions_dir, target_node))
