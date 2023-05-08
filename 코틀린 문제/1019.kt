import java.util.*
import kotlin.collections.ArrayList
import kotlin.math.pow

fun main() {
    val br = System.`in`.bufferedReader()
    val n = br.readLine()
    val cnt = Array(10) { 0L }

    n.indices.forEach { i ->
        val num = n.substring(i, i+1).toInt()

        val powNum = 10.toDouble().pow(n.length - 1 - i).toLong()
        val back = n.substring(i+1, n.length)
        val front = n.substring(0, i)

        if (back.isNotEmpty()) cnt[num] += back.toLong()
        cnt[num] ++

        (0 until num).forEach { cnt[it] += powNum }

        if (front.isNotEmpty()) (0..9).forEach { cnt[it] += front.toLong() * powNum }
        cnt[0] -= powNum
    }

    val sb = StringBuilder()
    cnt.forEach { sb.append("$it ") }
    println(sb)
}