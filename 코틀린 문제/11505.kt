import java.lang.StringBuilder
import java.util.StringTokenizer

fun main() {
    val br = System.`in`.bufferedReader()
    val bw = System.`out`.bufferedWriter()
    var st = StringTokenizer(br.readLine())
    val (N, M, K) = List(3) { st.nextToken().toInt() }

    val num = Array(N) { br.readLine().toLong() }

    val h = Math.ceil(Math.log(N.toDouble()) / Math.log(2.0)) + 1
    val len = 1 shl(h.toInt())

    val tree = Array(len) { 1L }

    fun makeTree(idx: Int, from: Int = 0, to: Int = N-1): Long {
        if (from == to) tree[idx] = num[from]
        else {
            val mid = (from + to) / 2
            tree[idx] = makeTree(idx*2, from, mid) * makeTree(idx*2+1, mid+1, to) % 1000000007
        }
        return tree[idx]
    }
    fun multi(idx: Int, left: Int, right:Int, from:Int = 0, to: Int = N-1): Long {
        if (right < from || to < left) return 1L
        if (left <= from && to <= right) return tree[idx]
        else {
            val mid = (from + to) / 2
            return multi(idx*2, left, right, from, mid) * multi(idx*2 + 1, left, right, mid+1, to) % 1000000007
        }
    }
    fun update(idx: Int, node: Int, value: Long, from: Int = 0, to: Int = N-1) {
        if (node < from || to < node) return
        if (from == to) {
            tree[idx] = value
        } else {
            val mid = (from + to) / 2
            update(idx * 2, node, value, from, mid)
            update(idx * 2 + 1, node, value, mid + 1, to)
            tree[idx] = tree[idx*2] * tree[idx*2+1] % 1000000007
        }
    }

    makeTree(1)
    val sb = StringBuilder()
    repeat(M + K) {
        st = StringTokenizer(br.readLine())
        val (a, b, c) = List(3) { st.nextToken().toInt() }
        if (a == 1) {
            update(1, b-1, c.toLong())
        } else if (a == 2) {
            sb.append(multi(1, b-1, c-1)).append('\n')
        }
    }
    bw.write(sb.toString())
    bw.flush()
}