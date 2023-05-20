import kotlin.math.max

fun main() {
    val br = System.`in`.bufferedReader()
    val n = br.readLine().toInt()
    val board = Array(n) { Array(n) {0} }

    (0 until n).forEach { r ->
        br.readLine().toCharArray().forEachIndexed { c, num -> board[r][c] = num - '0' }
    }

    val MAX = 1.shl(n)
    val dp = Array(MAX) { Array(n) { Array(10) { 0 } } }

    fun makeAns(bit: Int, turn: Int, price: Int): Int {
        if (dp[bit][turn][price] > 0) return dp[bit][turn][price]
        var tmp = 0
        (0 until n).forEach { i ->
            if (bit and 1.shl(i) == 0 && price <= board[turn][i]) {
                tmp = max(tmp, 1 + makeAns(bit or 1.shl(i), i, board[turn][i]))
            }
        }
        dp[bit][turn][price] = tmp
        return tmp
    }

    println(makeAns(1, 0, 0) + 1)
}