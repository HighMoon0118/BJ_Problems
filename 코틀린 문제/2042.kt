


fun main() {

    val br = System.`in`.bufferedReader()

    val (n, m, k) = br.readLine().split(" ").map { it.toInt() }
    val tree = Array(n + 1) { 0L }


    fun sum(idx: Int): Long {
        var result = 0L
        var i = idx
        while(i > 0) {
            result += tree[i]
            i -= i.and(-i)
        }
        return result
    }

    fun update(idx: Int, value: Long) {
        var i = idx
        while (i <= n) {
            tree[i] += value
            i += i.and(-i)
        }
    }

    (1..n).forEach {
        val number = br.readLine().toLong()
        update(it, number)
    }

    val sb = StringBuilder()
    repeat (m + k) {
        val (a, b, c) = br.readLine().split(" ").map { it.toLong() }
        if (a == 1L) {
            val num = sum(b.toInt()) - sum(b.toInt() - 1)
            update(b.toInt(), c - num)
        } else if (a == 2L) {
            sb.append(sum(c.toInt()) - sum(b.toInt() - 1)).append('\n')
        }
    }
    print(sb.toString())
}