fun main() {
    val br = System.`in`.bufferedReader()

    val board = Array(10) { Array(10) { 0 } }

    repeat(10) { r ->
        val line = br.readLine().split(" ").map { it.toInt() }
        repeat(10) { c ->
            board[r][c] = line[c]
        }
    }

    val cntArray = arrayOf(0, 5, 5, 5, 5, 5)

    fun checkBoard(row: Int, col: Int, size: Int): Boolean {
        if (cntArray[size] == 0) return false

        repeat(size) { dr ->
            repeat(size) { dc->
                if (row + dr >= 10 || col + dc >= 10 || board[row + dr][col + dc] == 0) return false
            }
        }
        return true
    }

    fun changeBoard(row: Int, col: Int, size: Int, value: Int) {
        cntArray[size] += if (value == 0) -1 else 1

        repeat(size) { dr ->
            repeat(size) { dc->
                board[row + dr][col + dc] = value
            }
        }
    }

    var ans = 26

    fun makeAns(r: Int, c: Int, cnt: Int) {
        if (cnt >= ans) return

        if (r == 9 && c == 10) {
            ans = Math.min(ans, cnt)
            return
        }

        val row = if (c == 10) r + 1 else r
        val col = if (c == 10) 0 else c

        if (board[row][col] == 0) {
            makeAns(row, col + 1, cnt)
        } else {
            repeat(5) {
                val size = 5 - it
                if (checkBoard(row, col, size)) {
                    changeBoard(row, col, size, 0)
                    makeAns(row, col + 1, cnt + 1)
                    changeBoard(row, col, size, 1)
                }
            }
        }
    }

    makeAns(0, 0, 0)

    println(if(ans == 26) -1 else ans)
}