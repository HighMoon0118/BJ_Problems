import java.util.PriorityQueue

fun main() {
    val br = System.`in`.bufferedReader()
    val (N, K) = br.readLine().split(" ").map { it.toInt() }

    val jewel = arrayListOf<Pair<Int, Int>>()
    repeat(N) {
        val (m, v) = br.readLine().split(" ").map { it.toInt() }
        jewel.add(m to v)
    }
    jewel.sortBy { it.first }

    val pocket = arrayListOf<Int>()
    repeat(K) {
        val c = br.readLine().toInt()
        pocket.add(c)
    }

    val que = PriorityQueue<Pair<Int, Int>> { a, b -> b.second - a.second }
    var idx = 0
    var ans = 0L
    pocket.sorted().forEach { c ->
        while (idx < jewel.size && jewel[idx].first <= c) {
            que.add(jewel[idx])
            idx ++
        }
        if (que.isNotEmpty()) {
            ans += que.poll().second
        }
    }
    print(ans)
}