import java.lang.StringBuilder
import java.util.*
import kotlin.collections.ArrayList

fun main() {

    val br = System.`in`.bufferedReader()
    val line = br.readLine()

    fun ArrayList<String>.toWord(): String {
        var tmp = this[0]
        (1 until this.size step 2).forEach { idx ->
            tmp += "${this[idx+1]}${this[idx]}"
        }
        return tmp
    }

    fun String.findGroup(startIdx: Int): Int {
        var cnt = 1
        var idx = startIdx
        while (idx+1 < this.length) {
            idx ++
            if (this[idx] == '(') cnt ++
            else if (this[idx] == ')') cnt --
            if (cnt == 0) break
        }
        return idx
    }
    fun makeAns(word: String): String {
        val list = arrayListOf<String>()
        var i = 0
        val tmpList = arrayListOf<String>()
        while (i < word.length) {
            when (word[i]) {
                in 'A'..'Z', '*', '/' -> {
                    tmpList.add(word[i].toString())
                }
                '+', '-' -> {
                    if (tmpList.isNotEmpty()) list.add(tmpList.toWord())
                    tmpList.clear()
                    list.add(word[i].toString())
                }
                '(' -> {
                    val idx = word.findGroup(i)
                    tmpList.add(makeAns(word.substring(i+1, idx)))
                    i = idx
                }
            }
            i ++
            if (i == word.length) list.add(tmpList.toWord())
        }

        return list.toWord()
    }

    print(makeAns(line))
}