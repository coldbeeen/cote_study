// 풀이 시간: 25분
// 풀이 방법: 재귀를 통해 연쇄적인 split을 수행하며 만족하는 조건을 체크하며 white와 blue를 카운팅한다.

var white = 0
var blue = 0

fun check(square: Array<IntArray>, n: Int, x: Int, y: Int): Boolean {  // (x, y) 위치부터 n만큼의 정사각형 체크
    for (i in 0 until n) {
        for (j in 0 until n) {
            if (square[x + i][y + j] != square[x][y]) {
                return false  // 하나라도 다른 게 있다면 false 리턴 (추가적인 split 필요)
            }
        }
    }

    if (square[x][y] == 0) {  // 전부 같고, 0이라면 white 증가
        white++
    } else {  // 1이라면 blue 증가
        blue++
    }
    return true  // 전부 같다면 true 리턴 (더 이상 split하지 않음)
}

fun split(square: Array<IntArray>, n: Int, x: Int, y: Int) {  // 4개의 정사각형으로 나누어 check (재귀 함수)
    val half = n / 2
    for (i in 0 until n step half) {
        for (j in 0 until n step half) {
            if (!check(square, half, x + i, y + j)) {
                split(square, half, x + i, y + j)
            }
        }
    }
}

fun main() {
    val n = readln().toInt()
    val square = Array(n) { readln().split(" ").map { it.toInt() }.toIntArray() }

    if (!check(square, n, 0, 0)) {  // split 전에 check 먼저 수행 (split이 필요하다면 수행)
        split(square, n, 0, 0)
    }

    println(white)
    println(blue)
}
