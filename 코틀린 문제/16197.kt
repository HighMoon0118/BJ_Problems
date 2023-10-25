import java.util.*

fun main() {
    val br = System.`in`.bufferedReader()

    val (N, M) = br.readLine().split(" ").map { it.toInt() }
    val board = Array(N) { Array(M) { '.' } }

    val coinList = ArrayList<Int>()

    repeat(N) { row ->
        br.readLine().forEachIndexed { col, c ->
            board[row][col] = if (c == 'o') {
                coinList.add(row * M + col)
                '.'
            } else {
                c
            }
        }
    }

    val que = LinkedList<Pair<Int, ArrayList<Int>>>()
    que.add(1 to coinList)

    val dR = listOf(0, 1, 0, -1)
    val dC = listOf(1, 0, -1, 0)

    var ans = -1

    hi@while (que.isNotEmpty()) {
        val (cnt, currentList) = que.poll()

        if (cnt > 10) break

        for (i in 0 until 4) {
            val tmpList = arrayListOf<Int>()

            for (num in currentList) {
                val row = num / M
                val col = num % M

                val nR = row + dR[i]
                val nC = col + dC[i]

                if (nR in 0 until N && nC in 0 until M) {
                    tmpList.add(if (board[nR][nC] == '#') num else nR*M + nC)
                }
            }
            if (tmpList.size == 1) {
                ans = cnt
                break@hi
            } else if (tmpList.size == 2) {
                que.add(cnt + 1 to tmpList)
            }
        }
    }
    /**
     * queue가 비어서 끝날경우(둘 다 떨어진 경우)를 고려하지 않음
     * row, col 위치를 하나의 숫자로 표현할 땐 row * M + col (나는 아무생각없이 N을 곱했다.)
     */

    print(ans)
}