fun main() {
    val br = System.`in`.bufferedReader()

    val (R, C, M) = br.readLine().split(" ").map { it.toInt() }
    var sharks = arrayListOf<Shark>()

    val rRotation = R*2 - 2
    val cRotation = C*2 - 2

    fun Int.getMod(value: Int): Int =
            if (value == 0) 0
            else this % value


    repeat(M) {
        val (r, c, s, d, z) = br.readLine().split(" ").map { it.toInt() }
        val move = if (d in 1..2) {
            s.getMod(rRotation)
        } else {
            s.getMod(cRotation)
        }
        val dist = when (d) {
            1 -> { rRotation - (r - 1) }
            2 -> { r - 1 }
            3 -> { c - 1 }
            4 -> { cRotation - (c - 1)}
            else -> { 0 }
        }
        sharks.add(Shark(r - 1, c - 1, d, move, z, dist))
    }

    var ans = 0

    fun killShark(idx: Int) {
        sharks.filter { it.col == idx }.minByOrNull { it.row }?.also { shark ->
            sharks.remove(shark)
            ans += shark.z
        }
    }
    fun moveShark() {
        val board = Array(R) { Array<Shark?>(C) { null } }

        sharks.forEach { shark ->
            when (shark.d) {
                1, 2 -> { // 위, 아래
                    val dist = (shark.dist + shark.s).getMod(rRotation)
                    shark.dist = dist
                    shark.row = if (dist >= R) rRotation - dist else dist
                }
                3, 4 -> { // 오른쪽, 왼쪽
                    val dist = (shark.dist + shark.s).getMod(cRotation)
                    shark.dist = dist
                    shark.col = if (dist >= C) cRotation - dist else dist
                }
            }
            if (board[shark.row][shark.col] == null) {
                board[shark.row][shark.col] = shark
            } else {
                if (board[shark.row][shark.col]!!.z < shark.z) {
                    board[shark.row][shark.col] = shark
                }
            }
        }
        val tmpList = arrayListOf<Shark>()
        (0 until R).forEach { r ->
            (0 until C).forEach { c ->
                if (board[r][c] != null) tmpList.add(board[r][c]!!)
            }
        }
        sharks = tmpList
    }
    fun eatShark() {
        val sharkSet = arrayListOf<Shark>()
        sharks.forEach { shark ->
            if (!sharkSet.contains(shark)) {
                sharkSet.add(sharks.filter { it == shark }.maxBy { it.z })
            }
        }
        sharks = sharkSet.toCollection(ArrayList())
    }

    (0 until C).forEach {
        killShark(it)
        moveShark()
//        eatShark()
    }

    print(ans)
}

data class Shark(
        var row: Int,
        var col: Int,
        val d: Int,
        val s: Int,
        val z: Int,
        var dist: Int
) {
    override fun equals(other: Any?): Boolean {
        if (other is Shark) {
            return other.row == this.row && other.col == this.col
        }
        return false
    }
    override fun toString() = "shark >> row = $row / col = $col"
}