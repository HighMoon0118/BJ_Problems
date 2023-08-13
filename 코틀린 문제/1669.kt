import java.util.LinkedList
import java.util.PriorityQueue

fun main() {
    val br = System.`in`.bufferedReader()

    val (X, Y) = br.readLine().split(" ").map { it.toInt() }

    /**
     * 1 = 1 (1*1 = 1)
     * 1 1 = 2
     * 1 1 1 = 3
     * 1 2 1 = 4 (2*2 = 4)
     * 1 1 2 1 = 5
     * 1 2 2 1 = 6
     * 1 1 2 2 1 = 7
     * 1 2 2 2 1 = 8
     * 1 2 3 2 1 = 9 (3*3 = 9)
     * 1 1 2 3 2 1 = 10
     * 1 2 2 3 2 1 = 11
     * 1 2 3 3 2 1 = 12
     * 1 1 2 3 3 2 1 = 13
     * 1 2 2 3 3 2 1 = 14
     * 1 2 3 3 3 2 1 = 15
     * 1 2 3 4 3 2 1 = 16 (4*4 = 16)
     */

    val gap = (Y - X).toLong()
    var n = 0L

    while (true) {
        val num = n * n

        if (num > gap) {
            n--
            val day = n*2 - 1
            print(if (n*n + n < gap) day+2 else day+1)
            break
        } else if (num == gap) {
            val day = n*2 - 1
            print(if (day < 0) 0 else day)
            break
        }
        n++
    }
}
