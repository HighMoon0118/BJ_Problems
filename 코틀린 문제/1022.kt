import java.lang.Math.abs
import java.lang.Math.max
import java.util.*


fun main() {
    val br = System.`in`.bufferedReader()

    var (r1, c1, r2, c2) = br.readLine().split(" ").map { it.toInt() }

    val n = maxOf(abs(r1), abs(c1), abs(r2), abs(c2)) * 2 + 1

    val row = r2 - r1 + 1
    val col = c2 - c1 + 1
    val board = Array(row) { Array(col) { 0 } }

    var num = 1
    var size = 1
    var sR = n / 2
    var sC = n / 2
    val dR = listOf(1, 0, -1, 0)
    val dC = listOf(0, 1, 0, -1)

    r1 += n / 2
    c1 += n / 2
    r2 += n / 2
    c2 += n / 2

    var maxNum = 0

    (0..(n/2)).forEach {
        (0..3).forEach { i ->
            (0 until size).forEach {
                if (i != 0 || it != 0) {
                    sR += dR[i]
                    sC += dC[i]
                }
                if (sR in r1..r2 && sC in c1..c2) {
                    board[sR - r1][sC - c1] = num
                    maxNum = max(maxNum, num)
                }
                num ++
            }
        }
        sC --
        size += 2
    }

    val maxL = maxNum.toString().length

    val sb = StringBuilder()
    (0 until row).forEach { r ->
        (0 until col).forEach { c ->
            sb.append(" ".repeat(maxL - board[r][c].toString().length + if (c == 0) 0 else 1)).append(board[r][c])
        }
        if (r < row - 1) sb.append('\n')
    }
    print(sb.toString())
}