
fun main() {
    val br = System.`in`.bufferedReader()
    val (N, K, M) = br.readLine().split(" ").map { it.toInt() }

    var total = N
    var order = M

    var cnt = 1

    while (true) {
        if (total == 1) break
        var gap = K % total
        if (gap == 0) gap = total

        order = if (gap > order) {
            order - gap + total
        } else if (gap < order){
            order - gap
        } else {
            break
        }
        total --
        cnt ++
    }

    print(cnt)
}