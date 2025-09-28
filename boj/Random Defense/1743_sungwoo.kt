// 풀이 시간: 21분
// 풀이 방법: BFS로 풀이함.

data class Point(val x: Int, val y: Int)

val dx = arrayOf(0, 0, 1, -1)   // x, y 축 상하좌우 이동을 위한 배열
val dy = arrayOf(1, -1, 0, 0)

// BFS 탐색을 통해 연결된 쓰레기 크기를 구 함수
fun bfsForWasteCount(graph: Array<BooleanArray>, r: Int, c: Int, n: Int, m: Int): Int {
    val queue: ArrayDeque<Point> = ArrayDeque()
    queue.add(Point(r, c))
    graph[r][c] = false
    var visitedCount = 1

    while (queue.isNotEmpty()) {
        val point = queue.removeFirst()

        for (i in 0 until 4) {
            val nx = point.x + dx[i]
            val ny = point.y + dy[i]

            if (nx in 0 until n && ny in 0 until m && graph[nx][ny]) {
                queue.add(Point(nx, ny))
                visitedCount++
                graph[nx][ny] = false
            }
        }
    }
    return visitedCount
}

fun main() {
    val (n, m, k) = readln().split(" ").map { it.toInt() }
    val graph = Array(n) { BooleanArray(m) }

    repeat(k) {
        val (r, c) = readln().split(" ").map { it.toInt() }
        graph[r - 1][c - 1] = true
    }

    var maxWaste = 0

    for (r in 0 until n) {
        for (c in 0 until m) {
            if (graph[r][c]) {
                maxWaste = maxOf(maxWaste, bfsForWasteCount(graph, r, c, n, m))
            }
        }
    }

    println(maxWaste)
}
