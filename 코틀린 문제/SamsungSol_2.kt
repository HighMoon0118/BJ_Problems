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
    val dp = Array(idxList.size) { Array(numList.size) { -1 } }

    fun makeAns(i: Int, startIdx: Int): Int {
        if (i == idxList.size) return 0

        if (dp[i][startIdx] >= 0) return dp[i][startIdx]

        var tmp = Int.MAX_VALUE

        for (end in idxList[i]) {
            tmp = minOf(tmp, idxList[i].minDistOf(startIdx, end.idx) + makeAns(i + 1, end.idx))
        }

        dp[i][startIdx] = tmp

        return dp[i][startIdx]
    }

    var tmp = Int.MAX_VALUE

    for (end in idxList[0]) {
        tmp = minOf(tmp, idxList[0].minDistOf(0, end.idx) + makeAns(1, end.idx))
    }

    println(tmp)
}

/**
 * Disk Scheduling - SCAN
 */
fun ArrayList<Num>.minDistOf(startIdx: Int, endIdx: Int): Int {
    val ls = Math.abs(startIdx - first().idx)
    val le = Math.abs(endIdx - first().idx)
    val sr = Math.abs(last().idx - startIdx)
    val er = Math.abs(last().idx - endIdx)
    val lr = Math.abs(last().idx - first().idx)
    /**
     *  s l e r
     *  l s e r
     *  l e s r
     *  l e r s
     */
    if (startIdx < endIdx) {
        return ls + lr + er
    } else {
        return sr + lr + le
    }
}

data class Num(
    val idx: Int,
    var visited: Boolean
)