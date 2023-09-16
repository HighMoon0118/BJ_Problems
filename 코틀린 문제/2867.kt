import java.util.Stack
import kotlin.math.max
import kotlin.math.min
import kotlin.math.pow

fun main() {
    val br = System.`in`.bufferedReader()

    val N = br.readLine().toInt()

    val num = Array(N) { 0L }

    val lMinTo = Array(N) { it }
    val lMaxTo = Array(N) { it }
    val rMinTo = Array(N) { it }
    val rMaxTo = Array(N) { it }

    repeat(N) { i -> num[i] = br.readLine().toLong() }

    repeat(N) { idx ->
        var i = idx
        while (lMinTo[i] > 0 && num[i - 1] > num[idx]) i = lMinTo[i - 1]
        lMinTo[idx] = i

        i = idx
        while (lMaxTo[i] > 0 && num[i - 1] < num[idx]) i = lMaxTo[i - 1]
        lMaxTo[idx] = i

        val idx2 = N - 1 - idx

        i = idx2
        while (rMinTo[i] < N - 1 && num[i + 1] >= num[idx2]) i = rMinTo[i + 1]
        rMinTo[idx2] = i

        i = idx2
        while (rMaxTo[i] < N - 1 && num[i + 1] <= num[idx2]) i = rMaxTo[i + 1]
        rMaxTo[idx2] = i
    }

    var ans = 0L
    repeat(N) { i ->
        ans -= num[i] * (i - lMinTo[i] + 1) * (rMinTo[i] - i + 1)
        ans += num[i] * (i - lMaxTo[i] + 1) * (rMaxTo[i] - i + 1)
    }
    print(ans)
}
