from math import floor

def solution(file):
    with open (file, 'r') as f:
        winnings = 0
        for line in f.readlines():
            colon = line.split(':')

            card_num = colon[0]
            card_data = colon[1]

            data = card_data.split('|')
            winning_nums = set(data[0].strip().split(' '))
            card_nums = set(data[1].strip().split(' '))

            wins = len(list(winning_nums.intersection(card_nums)))
            win_value = floor(1 * (2**(wins-1)))
            winnings += win_value
    return winnings


if __name__ == "__main__":
    file = 'advent-storage/advent-23-4.txt'
    print(solution(file))
