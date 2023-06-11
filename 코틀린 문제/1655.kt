

fun main() {

    val br = System.`in`.bufferedReader()

    val n = br.readLine().toInt()

    val list = arrayListOf<Int>()
    val sb = StringBuilder()

    fun addNum(num: Int) {
        var l = 0
        var r = list.size - 1

        while (l <= r) {
            val mid = (l + r) / 2
            if (list[mid] < num) {
                l = mid + 1
            } else if (list[mid] > num) {
                r = mid - 1
            } else {
                l = mid
                break
            }
        }

        list.add(l, num)
    }

    repeat(n) {
        addNum(br.readLine().toInt())
        sb.append(list[(list.size - 1) / 2]).append('\n')
    }

    print(sb.toString())
}