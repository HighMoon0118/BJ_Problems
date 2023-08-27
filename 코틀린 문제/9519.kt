

fun main() {

    val br = System.`in`.bufferedReader()
    val x = br.readLine().toInt()
    var word = br.readLine()

    val wordMap = HashMap<Int, String>()
    var cycle = 0

    while (!wordMap.containsValue(word)) {
        wordMap[cycle++] = word

        val mid = (word.length / 2) + 1
        val front = word.substring(0, mid)
        val back = word.substring(mid, word.length)

        val sb = StringBuilder()
        back.reversed().forEachIndexed { i, c -> sb.append(front[i]).append(c) }
        if (word.length % 2 == 0) sb.append(front[mid - 2])
        sb.append(front[mid - 1])

        word = sb.toString()
    }
    wordMap[cycle] = word

    print(wordMap[cycle - (x % cycle)])

    /**
     * 1 2 3 4
     * 1 4 2 3
     *
     * 1 2 3 4 5
     * 1 5 2 4 3
     *
     * 1 2 3 4 5 6
     * 1 6 2 5 3 4
     *
     */
}