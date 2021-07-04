def solution(board, moves):
    n = len(board)
    rowOf = [0]*n
    for c in range(n):
        for r in range(n):
            if board[r][c] > 0:
                rowOf[c] = r
                break
    st = []
    ans = 0
    for move in moves:
        r = rowOf[move-1]
        c = move-1
        if r == n: continue
        elif not st or st[-1] != board[r][c]:
            st.append(board[r][c])
        else:
            st.pop()
            ans += 2
        rowOf[c] += 1
    return ans