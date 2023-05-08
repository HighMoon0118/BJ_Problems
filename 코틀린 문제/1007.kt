import java.util.*
import java.io.*
import java.lang.Math.pow
import java.lang.StringBuilder
import kotlin.math.min
import kotlin.math.pow
import kotlin.math.sqrt

fun main() {
    val br = System.`in`.bufferedReader()
    val sb = StringBuilder()

    repeat (br.readLine().toInt()) {
        val n = br.readLine().toInt()
        val dot = Array(n) { StringTokenizer(br.readLine()).run { nextToken().toInt() to nextToken().toInt() }}

        val sumX = dot.sumOf { it.first }.toLong()
        val sumY = dot.sumOf { it.second }.toLong()

        var ans: Double = Double.MAX_VALUE

        fun calDist(a: Long, b: Long) = sqrt((a * a + b * b).toDouble())

        fun selectDot(cnt: Int, idx: Int, x: Long, y: Long) {  // n개에서 정확히 n/2개를 뽑는 경우의 수 계산
            if (idx == n) {
                ans = min(ans, calDist(x, y))
                return
            }

            if (cnt < n / 2) {
                selectDot(cnt + 1, idx + 1, x - 2 * dot[idx].first, y - 2 * dot[idx].second)
                if (n - idx + cnt > n / 2) selectDot(cnt, idx + 1, x, y)
            } else {
                selectDot(cnt, idx + 1, x, y)
            }
        }

        selectDot(0, 0, sumX, sumY)
        sb.append(String.format("%.6f", ans)).append("\n")
    }
    println(sb.toString())
}