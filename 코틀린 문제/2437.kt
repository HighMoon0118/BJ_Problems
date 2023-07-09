import kotlin.math.min

fun main() {
    val br = System.`in`.bufferedReader()

    val n = br.readLine().toInt()
    val chu = br.readLine().split(" ").map { it.toInt() }.sorted()

    var ans = chu.sum() + 1
    var sum = 0

    for (i in chu.indices) {
        if (sum + 1 < chu[i]) {
            ans = sum + 1
            break
        } else {
            sum += chu[i]
        }
    }
    println(ans)
}