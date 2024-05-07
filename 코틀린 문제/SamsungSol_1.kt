fun main() {
    val br = System.`in`.bufferedReader()

    val cost = br.readLine().split(" ").map { it.toInt() }
    val MAX_COUNT = br.readLine().toInt()
    val dp = Array(cost.size) { Array(MAX_COUNT + 1) { Array<Int?>(1001) { null } } }

    /**
     * count 번을 무조건 사고 팔지 않아도 되는 경우
     * 500 * 1000 * 1000 = 500000000
     */
    fun makeAnswer1(idx: Int, cnt: Int, buy: Int): Int {
        if (idx == cost.size || cnt == MAX_COUNT) return 0

        if (dp[idx][cnt][buy] != null) return dp[idx][cnt][buy]!!


        dp[idx][cnt][buy] = if (buy == 0) {
            maxOf(
                    makeAnswer1(idx + 1, cnt, 0),
                    makeAnswer1(idx + 1, cnt, cost[idx])
            )
        } else {
            maxOf(
                    cost[idx] - buy + makeAnswer1(idx + 1, cnt + 1, 0),
                    makeAnswer1(idx + 1, cnt, buy)
            )
        }

        return dp[idx][cnt][buy]!!
    }

    print(maxOf(makeAnswer1(0, 0, 0), makeAnswer1(0, 0, cost[0])))
}