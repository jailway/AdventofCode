import re

def load_games(file: str) -> [(int, int)]:
    regex = re.compile(r'([0-9]+) players; last marble is worth ([0-9]+) points')
    result = []
    with open(file, 'r') as f:
        for line in f.readlines():
            r = regex.match(line)
            if not r:
                raise Exception('Cannot parse line "%s"' % line)

            result.append((int(r.group(1)), int(r.group(2))))
    return result


def play(players: int, last_marble: int) -> int:
    circle = [0]
    player = 0
    scores = [0] * players
    current_marble = 0
    for i in range(1, last_marble + 1):
        if (i % 23) != 0:
            current_marble = (current_marble + 1) % len(circle) + 1
            circle.insert(current_marble, i)
        else:
            current_marble = (current_marble - 7) % len(circle)
            scores[player] += i + circle.pop(current_marble)
            current_marble = current_marble % len(circle)
        player = (player + 1) % players
    return max(scores)


if __name__ == "__main__":
    sets = load_games('09_input.txt')
    for s in sets:
        print(s[0], ' players; last marble is worth ', s[1]*100, ' points: high score is ', play(s[0], s[1]*100))
