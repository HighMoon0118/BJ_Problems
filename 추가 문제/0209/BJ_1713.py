n = int(input())
vote = int(input())
votes = list(map(int, input().split()))
vote_count = [0 for _ in range(101)]
board = []

for v in votes:
    if vote_count[v]:
        vote_count[v] += 1
    else:
        board.append(v)
        vote_count[v] = 1

    if len(board) > n:
        min_vote = 1001
        for i in range(len(board) - 1):
            if vote_count[board[i]] < min_vote:
                min_vote = vote_count[board[i]]
                who = board[i]
        board.remove(who)
        vote_count[who] = 0
board.sort()
print(*board)