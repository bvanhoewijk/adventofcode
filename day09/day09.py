from collections import deque, defaultdict

# https://stackoverflow.com/questions/4151320/efficient-circular-buffer
def marble_game(players, last_marble):
    circle = deque([0])
    scores = defaultdict(int)
    for i in range(1, last_marble-1):
        player = ((i - 1) % players) + 1
        if i % 23 == 0:
            circle.rotate(7)
            scores[player] += i + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(i)
    print(max(scores.values()))

if __name__ == "__main__":
    marble_game(468, 71843)
    # 385820
    marble_game(468, 71843*100)
    # 3156297594
    

