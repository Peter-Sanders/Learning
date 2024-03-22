def get_data(file):
    with open(file, 'r') as f:
        data = [x.strip('\n') for x in f.readlines()]
    return data 

def solution(file):
    data = get_data(file)
    print(data)

    for seq in data:
        oasis = [int(x) for x in seq.split(' ')]
        print(oasis)

        oasis_data = [oasis]
        next_oasis = []
        run_sum = 1
        while run_sum > 0:
            for i, o in enumerate(oasis):
                if i +1 < len(oasis):
                    next_oasis.append(oasis[i+1] - o)
                    oasis_data.append(next_oasis)
            run_sum = sum(next_oasis)
            print(run_sum)
        # print(oasis_data)
        


    return 0


if __name__ == "__main__":
    file = 'advent-storage/advent-23-9.txt'
    print(solution(file))
