fun main() {
    val dx = arrayOf(1, 0, -1, 0)  // 방향에 따른 x 변화량
    val dy = arrayOf(0, -1, 0, 1)  // 방향에 따른 y 변화량

    fun updateRange(range: IntArray, n: Int) {  // n의 범위를 업데이트
        range[0] = minOf(range[0], n)
        range[1] = maxOf(range[1], n)
    }

    val N = readln().toInt()
    val note = readln().toCharArray()

    val pointList = mutableListOf(intArrayOf(0, 0))  // 좌표 리스트 생성
    val xRange = intArrayOf(0, 0) // x 범위
    val yRange = intArrayOf(0, 0) // y 범위

    var x = 0
    var y = 0
    var d = 0

    for (c in note) {
        when (c) {
            'F' -> {
                x += dx[d]  // d 방향으로 전진
                y += dy[d]
                pointList.add(intArrayOf(x, y))  // 해당 좌표 추가
                updateRange(xRange, x)  // 범위 업데이트
                updateRange(yRange, y)
            }
            'R' -> d = (d + 1) % 4
            'L' -> d = (4 + d - 1) % 4
        }
    }

    val r = xRange[1] - xRange[0] + 1  // 행 높이 구하기
    val c = yRange[1] - yRange[0] + 1  // 열 너비 구하기
    val map = Array(r) { CharArray(c) { '#' } }  // 맵 생성

    for (point in pointList)  // pointList에 표시된 위치에 '.' 표시
        map[point[0] - xRange[0]][point[1] - yRange[0]] = '.'

    for (row in map)
        println(row.joinToString(""))
}
