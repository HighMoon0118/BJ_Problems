import java.lang.Integer.min

fun main() {

    val br = System.`in`.bufferedReader()
    val (n, m) = br.readLine().split(" ").map { it.toInt() }
    val board = Array(n) { Array(m) { 0 } }

    (0 until n).forEach { r ->
        val line = br.readLine()
        (0 until m).forEach { c ->
            board[r][c] = line[c].toString().toInt()
        }
    }

    val dr = listOf(0, 1, 0, -1)
    val dc = listOf(1, 0, -1, 0)

    var visit = Array(n) { Array(m) { false } }
    var minN = 10
    var num = 1
    var countArray = arrayListOf<Pair<Int, Int>>()

    fun dfs(row: Int, col: Int) {
        if (visit[row][col]) return

        visit[row][col] = true
        countArray.add(row to col)

        (0..3).forEach {
            val nr = row + dr[it]
            val nc = col + dc[it]
            if (nr in 0 until n && nc in 0 until m) {
                if (board[nr][nc] == num) {
                    dfs(nr, nc)
                } else if (board[nr][nc] > num) {
                    minN = min(minN, board[nr][nc])
                } else if (board[nr][nc] < num) {
                    minN = -1
                }
            } else {
                minN = -1
            }
        }
    }

    var ans = 0

    (1..9).forEach {
        num = it
        visit = Array(n) { Array(m) { false } }

        (0 until n).forEach { r ->
            (0 until m).forEach { c ->
                if (board[r][c] == num && !visit[r][c]) {
                    minN = 10
                    countArray = arrayListOf()

                    dfs(r, c)

                    if (minN > num) {
                        countArray.forEach { (row, col) ->
                            board[row][col] = minN
                        }
                        ans += countArray.size * (minN - num)
                    }
                }
            }
        }
    }
    println(ans)
}