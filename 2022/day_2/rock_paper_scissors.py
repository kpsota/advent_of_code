rules_1 = [
    {
        'player_1': 'A',
        'player_2': 'X',
        'result': 'draw'
    },
    {
        'player_1': 'A',
        'player_2': 'Y',
        'result': 'win'
    },
    {
        'player_1': 'A',
        'player_2': 'Z',
        'result': 'loss'
    },
    {
        'player_1': 'B',
        'player_2': 'X',
        'result': 'loss'
    },
    {
        'player_1': 'B',
        'player_2': 'Y',
        'result': 'draw'
    },
    {
        'player_1': 'B',
        'player_2': 'Z',
        'result': 'win'
    },
    {
        'player_1': 'C',
        'player_2': 'X',
        'result': 'win'
    },
    {
        'player_1': 'C',
        'player_2': 'Y',
        'result': 'loss'
    },
    {
        'player_1': 'C',
        'player_2': 'Z',
        'result': 'draw'
    }
]

rules_2 = [
    {
        'player_1': 'A',
        'player_2': 'X',
        'result': 'loss'
    },
    {
        'player_1': 'A',
        'player_2': 'Y',
        'result': 'draw'
    },
    {
        'player_1': 'A',
        'player_2': 'Z',
        'result': 'win'
    },
    {
        'player_1': 'B',
        'player_2': 'X',
        'result': 'loss'
    },
    {
        'player_1': 'B',
        'player_2': 'Y',
        'result': 'draw'
    },
    {
        'player_1': 'B',
        'player_2': 'Z',
        'result': 'win'
    },
    {
        'player_1': 'C',
        'player_2': 'X',
        'result': 'loss'
    },
    {
        'player_1': 'C',
        'player_2': 'Y',
        'result': 'draw'
    },
    {
        'player_1': 'C',
        'player_2': 'Z',
        'result': 'win'
    }
]

scores = {
    'loss': 0,
    'draw': 3,
    'win': 6,
    'X': 1,
    'Y': 2,
    'Z': 3
}

def get_player_score_1(player_1, player_2):

    result = [rule for rule in rules_1 if rule['player_1'] == player_1 and rule['player_2'] == player_2][0]['result']
    result_score = scores[result]
    player_2_choice_score = scores[player_2]

    player_2_total_score = result_score + player_2_choice_score

    return player_2_total_score


def get_player_score_2(player_1, player_2):

    result = [rule for rule in rules_2 if rule['player_1'] == player_1 and rule['player_2'] == player_2][0]['result']

    player_2_choice = [rule for rule in rules_1 if rule['player_1'] == player_1 and rule['result'] == result][0]['player_2']

    result_score = scores[result]
    player_2_choice_score = scores[player_2_choice]

    player_2_total_score = result_score + player_2_choice_score

    return player_2_total_score

def main():

    with open('data/sample.txt') as inf:

        player_total_score_1 = 0
        player_total_score_2 = 0
        for r in inf:
            r_split = r.split(' ')
            player_1 = r_split[0].strip()
            player_2 = r_split[1].strip()

            player_score_1 = get_player_score_1(player_1, player_2)
            player_score_2 = get_player_score_2(player_1, player_2)

            player_total_score_1 = player_total_score_1 + player_score_1
            player_total_score_2 = player_total_score_2 + player_score_2

        print('Score 1: {}'.format(player_total_score_1))
        print('Score 2: {}'.format(player_total_score_2))

main()
