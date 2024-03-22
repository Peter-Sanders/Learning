import math

def solution(file:str):
    with open(file, 'r') as f:
        lines = f.readlines()
        times = [x for x in lines[0].split(':')[1].strip().split(' ') if x]
        dists = [x for x in lines[1].split(':')[1].strip().split(' ') if x]

        races = []
        for i in range(len(times)):
            val = 0
            time = int(times[i])
            dist = int(dists[i])

            for s in range(time):
                race_dist = s * (time - s)
                if race_dist > dist:
                    val += 1
            races.append(val)

    return math.prod(races)
    

if __name__ == "__main__":
    file = 'advent-storage/advent-23-6.txt'
    print(solution(file))

