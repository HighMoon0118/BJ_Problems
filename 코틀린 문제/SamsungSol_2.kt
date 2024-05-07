fun main() {

    val br = System.`in`.bufferedReader()
    val numList = br.readLine().split(" ").mapIndexed { i, num -> num.toInt() to i }
    val idxList = numList
            .map { it.first }
            .toSortedSet()
            .map {
                arrayListOf<Num>().apply {
                    for ((num, i) in numList) {
                        if (num == it) add(Num(i, false))
                    }
                }
            }
    val dp = Array(numList.size) { Array(numList.size) { -1 } }

    fun makeAns(idx: Int, order: Int, idx2: Int): Int {
        if (order == numList.size) return 0

        if (dp[idx][order] >= 0) return dp[idx][order]

        var tmp = Int.MAX_VALUE
        for (num in idxList[idx2]) {
            if (!num.visited) {
                num.visited = true
                tmp = minOf(tmp, Math.abs(num.idx - idx) + makeAns(num.idx, order + 1, idx2))
                num.visited = false
            }
        }
        if (tmp == Int.MAX_VALUE) {
            tmp = makeAns(idx, order, idx2+1)
        }
        dp[idx][order] = tmp

        return dp[idx][order]
    }

    var tmp = Int.MAX_VALUE

    for (num in idxList[0]) {
        if (!num.visited) {
            num.visited = true
            tmp = minOf(tmp, num.idx + makeAns(num.idx, 1, 0))
            num.visited = false
        }
    }

    println(tmp)
}

data class Num(
    val idx: Int,
    var visited: Boolean
)