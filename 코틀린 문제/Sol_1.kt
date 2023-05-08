import java.lang.StringBuilder
import java.util.*
import kotlin.collections.ArrayList

fun main() {
    val br = System.`in`.bufferedReader()
    val sb = StringBuilder()

    repeat(br.readLine().toInt()) {
        val (n, k) = StringTokenizer(br.readLine()).run { Array(2) { nextToken().toInt() } }
        val timeOf = StringTokenizer(br.readLine()).run { Array(n) { nextToken().toInt() } }
        val childOf = Array(n + 1) { ArrayList<Int>() }
        val parentsOf = Array(n + 1) { 0 }
        repeat(k) {
            val (from, to) = StringTokenizer(br.readLine()).run { Array(2) { nextToken().toInt() } }
            childOf[from].add(to)
            parentsOf[to] ++
        }
        val w = br.readLine().toInt()

//        val dp = Array(n + 1) { -1 }
//        fun dfs(parent: Int): Int {
//            if (dp[parent] >= 0) return dp[parent]
//            dp[parent] = (childOf[parent].maxOfOrNull { dfs(it) } ?: 0) + timeOf[parent - 1]
//            return dp[parent]
//        }
//        sb.append(dfs(w)).append("\n")

        val que = LinkedList<Int>().apply { parentsOf.forEachIndexed { index, num -> if (num == 0) add(index) } }
        val dp = Array(n + 1) { 0 }

        while (que.isNotEmpty()) {
            val p = que.pop()
            if (p == w) break

            for (c in childOf[p]) {
                parentsOf[c] --
                dp[c] = maxOf(dp[c], dp[p] + timeOf[p - 1])
                if (parentsOf[c] == 0) {
                    que.add(c)
                }
            }
        }
        sb.append(dp[w] + timeOf[w - 1]).append("\n")
    }
    print(sb.toString())
}