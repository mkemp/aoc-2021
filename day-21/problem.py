from collections import Counter, defaultdict
from itertools import product

with open('input') as f:
    values = [line for line in f.read().strip().split('\n')]

player_1_idx = int(values[0].partition(': ')[-1])
player_2_idx = int(values[1].partition(': ')[-1])


def mod10(value):
    while value > 10:
        value -= 10
    return value


class PlayerV1(object):
    def __init__(self, idx):
        super(PlayerV1, self).__init__()
        self.idx = idx
        self.score = 0
    def take_turn(self, die):
        roll = sum([die.roll(), die.roll(), die.roll()])
        self.idx + mod10(self.idx + roll)
        self.score += self.idx
    def is_winner(self):
        return 1000 <= self.score


class DeterministicDie(object):
    def __init__(self):
        super(DeterministicDie, self).__init__()
        self.last_roll = 0
        self.total_rolls = 0
    def roll(self):
        self.total_rolls += 1
        self.last_roll += 1
        if self.last_roll > 100:
            self.last_roll -= 100
        return self.last_roll


# Part 1
die = DeterministicDie()
player_1 = PlayerV1(player_1_idx)
player_2 = PlayerV1(player_2_idx)

while True:
    player_1.take_turn(die)
    if player_1.is_winner():
        print(player_2.score * die.total_rolls)
        break
    player_2.take_turn(die)
    if player_2.is_winner():
        print(player_1.score * die.total_rolls)
        break
# 1196172


# Part 2
class PlayerV2(object):
    distribution = Counter(map(sum, product((1, 2, 3), repeat=3)))
    def __init__(self, key, idx, score=0):
        super(PlayerV2, self).__init__()
        self.key = key
        self.idx = idx
        self.score = score
    def __hash__(self):
        return hash(self.significant_attributes())
    def __eq__(self, other):
        return isinstance(other, PlayerV2) and other.significant_attributes() == self.significant_attributes()
    def significant_attributes(self):
        return self.key, self.idx, self.score
    def take_turn(self, roll):
        next_idx = mod10(self.idx + roll)
        return self.__class__(self.key, next_idx, self.score + next_idx)
    def is_winner(self):
        return 21 <= self.score


def play_turns(universes):
    wins = defaultdict(int)
    while universes:
        new_universes = defaultdict(int)
        for (p1, p2), old_count in universes.items():
            for roll, count in PlayerV2.distribution.items():
                new_p1 = p1.take_turn(roll)
                new_count = old_count * count
                if new_p1.is_winner():
                    wins[new_p1.key] += new_count
                else:
                    new_universes[(p2, new_p1)] += new_count
        universes = new_universes
    return wins


wins = play_turns({(PlayerV2(1, player_1_idx), PlayerV2(2, player_2_idx)): 1})
print(max(wins.values()))
# 106768284484217
