

fun main() {


    val br = System.`in`.bufferedReader()
    val (N, M, T) = br.readLine().split(" ").map { it.toInt() }


    val number = Array(N) { Array(M) { 0 } }
    repeat(N) { r ->
        val line = br.readLine().split(" ").map { it.toInt() }
        repeat(M) { c -> number[r][c] = line[c] }
    }

    val visited = Array(N) { Array(M) { false } }

    fun findSameNum(row: Int, col: Int, isSame: Boolean = false): Boolean {
        val num = number[row][col]
        if (visited[row][col] || num == 0) return false
        var isChanged = isSame
        visited[row][col] = true

        if (row > 0 && num == number[row - 1][col]) isChanged = isChanged or findSameNum(row - 1, col, true)
        if (row < N - 1 && num == number[row + 1][col]) isChanged = isChanged or findSameNum(row + 1, col, true)
        var c = if (col + 1 == M) 0 else col + 1
        if (num == number[row][c]) isChanged = isChanged or findSameNum(row, c, true)
        c = if (col == 0) M - 1 else col - 1
        if (num == number[row][c]) isChanged = isChanged or findSameNum(row, c, true)

        if (isChanged) number[row][col] = 0

        return isChanged
    }

    repeat(T) { t ->
        val (x, d, k) = br.readLine().split(" ").map { it.toInt() }

        var num = x

        while (num <= N) {
            repeat(N) { visited[it] = Array(M) { false } }

            val rotation = number[num - 1] + number[num - 1] + number[num - 1]
            val rotate = if (d == 0) -(k % M) else (k % M)
            repeat(M) { i -> number[num - 1][i] = rotation[M + rotate + i] }
            num += x
        }

        var isChanged = false

        repeat(N) { r ->
            repeat(M) { c ->
                isChanged = isChanged or findSameNum(r, c, false)
            }
        }

        if (!isChanged) {
            val total = number.map { it.sum() }.sum().toFloat()
            val cnt = number.map { it.count { value -> value != 0} }.sum()

            if (cnt != 0) {
                val average = total / cnt

                repeat(N) { r ->
                    repeat(M) { c ->
                        if (number[r][c] > average) number[r][c]--
                        else if (number[r][c] != 0 && number[r][c] < average) number[r][c]++
                    }
                }
            }
        }
    }
    println(number.map { it.sum() }.sum())
}