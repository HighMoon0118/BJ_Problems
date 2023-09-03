import java.util.LinkedList

fun main() {
    val br = System.`in`.bufferedReader()
    val (R, C) = br.readLine().split(" ").map { it.toInt() }

    val board = Array(R) { Array(C) { ' ' } }
    repeat(R) { r ->
        br.readLine().forEachIndexed { c, value ->
            board[r][c] = value
        }
    }

    val dr = listOf(0, 1, 0, -1)
    val dc = listOf(1, 0, -1, 0)

    fun lightBoard(row: Int, col: Int, value: Char) {
        val queue = LinkedList<Pair<Int, Int>> ()

        queue.add(row to col)
        board[row][col] = '.'

        while (queue.isNotEmpty()) {
            val (r, c) = queue.poll()
            repeat(4) { i ->
                val nr = r + dr[i]
                val nc = c + dc[i]
                if (nr in (0 until R) && nc in (0 until C) && board[nr][nc] != '.' && board[nr][nc] == value) {
                    board[nr][nc] = '.'
                    queue.add(nr to nc)
                }
            }
        }
    }
    var (Hr, Hc) = br.readLine().split(" ").map { it.toInt() - 1 }
    br.readLine().forEach {
        when (it) {
            'U' -> Hr--
            'D' -> Hr++
            'L' -> Hc--
            'R' -> Hc++
            else -> if (board[Hr][Hc] != '.') lightBoard(Hr, Hc, board[Hr][Hc])
        }
    }
    board[Hr][Hc] = '.'
    repeat(4) { i ->
        val nr = Hr + dr[i]
        val nc = Hc + dc[i]
        if (nr in (0 until R) && nc in (0 until C))
            board[nr][nc] = '.'
    }
    board.forEach { array ->
        println(String(array.map { if(it != '.') '#' else it }.toCharArray()))
    }
}