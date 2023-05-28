fun main() {
    val br = System.`in`.bufferedReader()

    val word = br.readLine()
    var ans = "z".repeat(word.length)
    (1..(word.length - 2)).forEach { i ->
        ((i + 1)..(word.length - 1)).forEach { j ->
            ans = minOf(ans, word.substring(0, i).reversed() + word.substring(i, j).reversed() + word.substring(j, word.length).reversed())
        }
    }
    println(ans)
}