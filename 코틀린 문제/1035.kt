import java.lang.Math.abs

fun main() {

    val br = System.`in`.bufferedReader()
    val board = Array(5) { Array(5) { '.' } }
    val star = ArrayList<Pair<Int, Int>>()

    (0..4).forEach { r ->
        br.readLine().forEachIndexed { c, char ->
            if (char == '*') {
                board[r][c] = char
                star.add(r to c)
            }
        }
    }

    fun Pair<Int, Int>.isNearBy(next: Pair<Int, Int>) =
            (first == next.first && abs(second - next.second) == 1) ||
                    (second == next.second && abs(first - next.first) == 1)

    fun checkBoard(): Boolean {
        val tmpList = arrayListOf(star[0])
        for (a in star) {
            if (tmpList.contains(a)) continue
            var isNearBy = false
            for (b in tmpList) {
                if (b.isNearBy(a)) {
                    isNearBy = true
                    break
                }
            }
            if (!isNearBy) return false
            tmpList.add(a)
        }
        return true
    }

    val dr = listOf(0, 0, 1, 0, -1)
    val dc = listOf(0, 1, 0, -1, 0)

    var MAX = 40
    fun makeAns(idx: Int, count: Int, move: Int) {
        if (move == 12 || count == MAX) return
        if (checkBoard()) {
            MAX = count
            return
        }
        val turn = if (idx == star.size) 0 else idx

        val (r, c) = star[turn]
        (0..4).forEach { i ->
            val nr = r + dr[i]
            val nc = c + dc[i]
            if (nr in (0..4) && nc in (0..4) &&
                    (i == 0 || board[nr][nc] != '*')) {
                star[turn] = nr to nc
                board[nr][nc] = '*'
                makeAns(turn + 1, count + if (i == 0) 0 else 1, move + 1)
                star[turn] = r to c
                board[nr][nc] = if (i == 0) '*' else '.'
            }
        }
    }

    makeAns(0, 0, 0)
    print(MAX)
}