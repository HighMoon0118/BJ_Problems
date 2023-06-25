import java.lang.Math.abs
import java.util.LinkedList

fun main() {

    val br = System.`in`.bufferedReader()

    val (N, M, F) = br.readLine().split(" ").map { it.toInt() }

    val board = Array(N) { Array<Item>(N) { Nothing() } }
    repeat(N) { r ->
        val line = br.readLine().split(" ").map { it.toInt() }
        repeat(N) { c ->
            if (line[c] == 1) {
                board[r][c] = Wall()
            }
        }
    }

    var (sR, sC) = br.readLine().split(" ").map { it.toInt() - 1 }

    val dR = listOf(-1, 0, 0, 1)
    val dC = listOf(0, -1, 1, 0)

    fun findRoute(r: Int, c: Int, toR: Int, toC: Int): Int {
        val visited = Array(N) { Array(N) { false } }
        val que = LinkedList<Triple<Int, Int, Int>>()

        que.add(Triple(r, c, 0))
        visited[r][c] = true

        while (que.isNotEmpty()) {
            val (row, col, dist) = que.poll()
            if (row == toR && col == toC) {
                return dist
            }
            repeat(4) {
                val nR = row + dR[it]
                val nC = col + dC[it]
                if (nR in (0 until N) && nC in (0 until N) && board[nR][nC] !is Wall && !visited[nR][nC]) {
                    visited[nR][nC] = true
                    que.add(Triple(nR, nC, dist + 1))
                }
            }
        }
        return -1
    }

    repeat(M) {
        val (r, c, eR, eC) = br.readLine().split(" ").map { it.toInt() - 1 }
        board[r][c] = Guest(r, c, eR, eC)
    }

    fun chooseGuest(row: Int, col: Int): Item {
        val visited = Array(N) { Array(N) { false } }
        val que = LinkedList<Triple<Int, Int, Int>>()

        val guestList = arrayListOf<Guest>()
        var guestDist = 0

        que.add(Triple(row, col, 0))
        visited[row][col] = true

        while (que.isNotEmpty()) {
            val (r, c, d) = que.poll()

            if (guestList.isNotEmpty() && guestDist < d) break

            val item = board[r][c]
            if (item is Guest) {
                guestList.add(item)
                guestDist = d
            }

            repeat(4) {
                val nR = r + dR[it]
                val nC = c + dC[it]
                if (nR in (0 until N) && nC in (0 until N) && board[nR][nC] !is Wall && !visited[nR][nC]) {
                    visited[nR][nC] = true
                    que.add(Triple(nR, nC, d + 1))
                }
            }
        }
        return if (guestList.isNotEmpty()) guestList.sortedWith(compareBy( { it.sR }, { it.sC }))[0].apply { dist = guestDist } else Nothing()
    }
    var ans = F
    for (i in 0 until M) {
        val guest = chooseGuest(sR, sC)

        if (guest is Guest) {
            val route = findRoute(guest.sR, guest.sC, guest.eR, guest.eC)

            if (route == -1 || ans < route + guest.dist) {
                ans = -1
                break
            } else {
                ans += route - guest.dist
                board[guest.sR][guest.sC] = Nothing()
                sR = guest.eR
                sC = guest.eC
            }
        } else {
            ans = -1
            break
        }
    }
    print(ans)
}

interface Item
class Guest (
        val sR: Int, val sC: Int,
        val eR: Int, val eC: Int,
        var dist: Int = 0
) : Item
class Nothing : Item
class Wall : Item