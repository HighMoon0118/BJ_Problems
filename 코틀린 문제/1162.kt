
import java.util.PriorityQueue

fun main() {

    val br = System.`in`.bufferedReader()
    val (N, M, K) = br.readLine().split(" ").map { it.toInt() }

    val road = Array(N) { ArrayList<Pair<Int, Int>>() }
    repeat(M) {
        val (a, b, time) = br.readLine().split(" ").map { it.toInt() }
        road[a - 1].add(b - 1 to time)
        road[b - 1].add(a - 1 to time)
    }

    val dp = Array(N) { Array(K + 1) { Long.MAX_VALUE } }

    val que = PriorityQueue(compareBy<Triple<Int, Int, Long>> { it.third }.thenBy { it.second })
    que.add(Triple(0, 0, 0))
    repeat(K) { dp[0][it] = 0 }

    var ans = Long.MAX_VALUE

    while (que.isNotEmpty()) {
        val (city, k, time) = que.poll()
        if (ans <= time || dp[city][k] < time) continue
        if (city == N - 1) {
            ans = Math.min(ans, time)
            continue
        }
        for (r in road[city]) {
            val nextCity = r.first
            val nextTime = r.second + time

            if (dp[nextCity][k] > nextTime) {
                dp[nextCity][k] = nextTime
                que.add(Triple(nextCity, k, nextTime))
            }
            if (k < K && dp[nextCity][k + 1] > time) {
                dp[nextCity][k + 1] = time
                que.add(Triple(nextCity, k + 1, time))
            }
        }
    }

    print(ans)
}