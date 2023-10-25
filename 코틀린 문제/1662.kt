import java.util.*

fun main() {
    val br = System.`in`.bufferedReader()

    val line = br.readLine()

    fun makeAns(word: String): Int {
        var ans = 0
        var i = 0
        var num = -1

        while (i < word.length) {
            when (word[i]) {
                '(' -> {
                    var j = ++i

                    var cnt = 1
                    while (j < word.length) {
                        if (word[j] == '(') cnt ++
                        else if (word[j] == ')') cnt --

                        if (cnt == 0) break
                        j ++
                    }

                    val childWord = makeAns(word.substring(i, j))
                    if (num >= 0) {
                        ans += childWord * num
                        num = -1
                    }
                    i = j + 1
                }
                else -> {
                    if (num >= 0) ans ++

                    num = word[i].toString().toInt()
                    i ++
                }
            }
        }
        if (num >= 0) ans ++
        return ans
    }

    /**
     * ++i 와 i++ 를 제대로 쓰자
     *
     * 괄호안에 있는 문자를 substring할 때 ')'의 전 인덱스까지 해야되는데
     * ')'의 다음 인덱스까지 해버렸다.
     * 실수좀 줄이자
     *
     * 최종 문자열을 직접 만드니까 메모리 초과가 났다. 주의하자.
     */

    print(makeAns(line))
}