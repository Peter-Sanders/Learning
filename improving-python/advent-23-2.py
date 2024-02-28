file = "advent-storage/advent-23-2.txt"
redmax = 12
greenmax=13
bluemax=14

def solution1(file, redmax, greenmax, bluemax):
    with open(file, "r") as f:
        valid_ids = []
        for line in f.readlines():
            colon = line.split(':')
            game = int(colon[0].split(' ')[1])
            redcount = 0
            greencount = 0
            bluecount = 0
            valid = True

            for res in colon[1].split(';'):
                for r in res.split(','):
                    val, color = r.strip().split(' ')
                    val = int(val)
                    if color == 'red':
                        redcount += val
                    elif color == 'blue':
                        bluecount += val 
                    elif color == 'green':
                        greencount += val
                    
                if (redcount > redmax) or (greencount > greenmax) or (bluecount > bluemax):
                    valid = False 
            if valid:
                valid_ids.append(game)

    return sum(valid_ids)

sol1 = solution1(file, redmax, greenmax, bluemax) 

print(sol1)
