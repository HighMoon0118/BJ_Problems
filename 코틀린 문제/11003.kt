import java.util.*
import kotlin.collections.ArrayDeque

fun main() {
    val br = System.`in`.bufferedReader()
    val bw = System.`out`.bufferedWriter()

    val (N, L) = br.readLine().split(" ").map { it.toInt() }
    val st = StringTokenizer(br.readLine(), " ")
    val num = IntArray(N) { st.nextToken().toInt() }

    val deque = ArrayDeque<Int>(L)

    repeat(N) { i ->
        while (deque.isNotEmpty() && deque.first() <= i - L) deque.removeFirst()
        while (deque.isNotEmpty() && num[deque.last()] >= num[i]) deque.removeLast()
        deque.add(i)
        bw.write("${num[deque.first()]} ")
    }
    bw.flush()
}