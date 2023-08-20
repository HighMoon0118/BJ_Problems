import java.util.HashMap
import java.util.PriorityQueue

fun main() {
    val br = System.`in`.bufferedReader()

    val (N, M) = br.readLine().split(" ").map { it.toInt() }

    val treeMap = Array(N) { HashMap<Int, Int>() }

    repeat(M) {
        val (a, b, c) = br.readLine().split(" ").map { it.toInt() }

        val cost = minOf(treeMap[a - 1][b - 1] ?: Int.MAX_VALUE, c)
        treeMap[a - 1][b - 1] = cost
        treeMap[b - 1][a - 1] = cost
    }

    val tree = treeMap.map { it.toList() }

    val que = PriorityQueue( compareBy<Pair<Int, Int>> { it.second } )
    que.add(0 to 0)

    val dp = Array(N) { Int.MAX_VALUE }

    while (que.isNotEmpty()) {
        val (node, cow) = que.poll()
        if (dp[node] <= cow) continue
        dp[node] = cow

        if (node == N - 1) continue

        tree[node].forEach { (nNode, nCow) ->
            val nextCow = cow + nCow
            if (dp[nNode] > nextCow) {
                que.add(nNode to nextCow)
            }
        }
    }
    print(dp[N - 1])
}