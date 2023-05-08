import java.util.*
import kotlin.math.sqrt

fun main() {

    val br = System.`in`.bufferedReader()

    val (minN, maxN) = StringTokenizer(br.readLine()).run { List(2) { nextToken().toLong() } }

    val gap = (maxN - minN).toInt()
    val check = Array<Boolean>(gap + 1) { false }

    (2..sqrt(maxN.toDouble()).toInt()).forEach { num ->
        val tmp = num.toLong() * num.toLong()

        var from = (minN / tmp) * tmp
        if (from == minN) check[0] = true

        while (from + tmp <= maxN) {
            from += tmp
            check[(from - minN).toInt()] = true
        }
    }

    println(check.count { !it })
}