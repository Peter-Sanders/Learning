from collections import Counter

def get_hand_tier(i, line, hand_rank):
    hand_tier = ''
    data = line.split(' ')
    hand = data[0]
    bid = int(data[1].replace('\n', ''))

    unique_cards = Counter(hand).keys()
    unique_card_count = Counter(hand).values()
    max_unique = max(unique_card_count)

    match len(unique_cards):
        case 1:
            hand_tier = hand_rank.get('Five of a Kind')
        case 2: 
            if max_unique == 4:
                hand_tier = hand_rank.get('Four of a  Kind')
            elif max_unique == 3:
                hand_tier = hand_rank.get('Full House')
        case 3: 
            if max_unique == 3:
                hand_tier = hand_rank.get('Three of a Kind')
            elif max_unique == 2:
                hand_tier = hand_rank.get('Two Pair')
        case 4: 
            hand_tier = hand_rank.get('One Pair')
        case 5:
            hand_tier = hand_rank.get('High Card')
    return hand_tier, {'hand_tier':hand_tier, 'bid':bid}


def get_players_in_rank(rank, player_hands):
    players_in_rank = []
    for i, player in enumerate(player_hands):
        if player == rank:
            players_in_rank.append(i)
    return players_in_rank


def tiebreak(players_in_rank, player_data, lines, top_rank, res, card_rank):
    for i in range(5):
        winning_player = []
        current_card_value = 0
        for plyer in players_in_rank:
            player_value = card_rank.get(lines[plyer][i])
            if player_value > current_card_value:
                current_card_value = player_value
                winning_player = [plyer]
            elif player_value == current_card_value:
                winning_player.append(plyer)
        if len(winning_player) == 1:
            res += top_rank * player_data[winning_player[0]]['bid'] 
            top_rank -= 1
            players_in_rank.pop(players_in_rank.index(winning_player[0]))
            if len(players_in_rank) == 1:
                res += top_rank * player_data[players_in_rank[0]]['bid'] 
                top_rank -= 1
                break
    return top_rank, res


def solution(file, game_data:dict):
    card_rank = game_data.get('card_rank')
    hand_rank = game_data.get('hand_rank')
    res = 0
    with open(file, 'r') as f:
        lines = [x.replace('\n', '') for x in f.readlines()]

        player_data = {}
        player_hands = []
        for i, line in enumerate(lines):
            hand_tier, data = get_hand_tier(i, line, hand_rank)
            player_data[i] = data 
            player_hands.append(hand_tier)
        max_hand = max(player_hands)
        top_rank = len(player_hands)
        for rank in hand_rank.values():
            players_in_rank = get_players_in_rank(rank, player_hands)
            if not players_in_rank:
                pass
            else:
                if len(players_in_rank) == 1:
                    res += top_rank * player_data[players_in_rank[0]]['bid'] 
                    top_rank -= 1
                else:
                    top_rank, res = tiebreak(players_in_rank, player_data, lines, top_rank, res, card_rank)
    return res


if __name__ == "__main__":
    game_data = {
    'card_rank':{
        'A':13,
        'K':12,
        'Q':11,
        'J':10,
        'T':9,
        '9':8,
        '8':7,
        '7':6,
        '6':5,
        '5':4,
        '4':3,
        '3':2,
        '2':1,
        },
    'hand_rank':{
        'Five of a Kind':7,
        'Four of a Kind':6,
        'Full House':5,
        'Three of a Kind':4,
        'Two Pair':3,
        'One Pair':2,
        'High Card':1,
        },
    }
    file = 'advent-storage/advent-23-7.txt' 
    print(solution(file, game_data))
