

fun main() {

    val br = System.`in`.bufferedReader()
    val (n, m) = br.readLine().split(" ").map { it.toInt() }
    val board = Array(n) { Array(m) { "H" } }
    repeat(n) { r ->
        br.readLine().toCharArray().forEachIndexed { c, num ->
            board[r][c] = "$num"
        }
    }

    val dp = Array(n) { Array(m) { Array(4) { -1 } } }
    val (dR, dC) = listOf(listOf(0, 1, 0, -1), listOf(1, 0, -1, 0))
    val visited = Array(n) { Array(m) { false } }
    var isInfinite = false

    fun makeAns(row: Int, col: Int, how: Int): Int {
        if (isInfinite) return 0
        if (board[row][col] == "H") return -1
        if (dp[row][col][how] >= 0) return dp[row][col][how]

        var maxCnt = 1
        repeat(4) { i ->
            val nR = row + dR[i] * board[row][col].toInt()
            val nC = col + dC[i] * board[row][col].toInt()

            if (nR in 0 until n && nC in 0 until m) {
                if (visited[nR][nC]) {
                    isInfinite = true
                } else {
                    visited[nR][nC] = true
                    maxCnt = Math.max(maxCnt, 1 + makeAns(nR, nC, i))
                    visited[nR][nC] = false
                }
            }
        }
        dp[row][col][how] = maxCnt
        return maxCnt
    }

    val ans = makeAns(0, 0, 0)
    if (isInfinite) println(-1)
    else println(ans)
}
