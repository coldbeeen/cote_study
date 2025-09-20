// 풀이 시간: 40분
// 풀이 방법:
// 곰곰히 생각해본 결과, 최적의 M개의 치킨집을 찾는 방법으로
// 브루트포스가 아닌 방법은 떠오르지 않았다.
// 힌트 참고하여 브루트포스라는 것을 알고 브루트포스로 풀이하였다.

data class Point(val x: Int, val y: Int) {  // 좌표 클래스
    companion object {
        fun distance(a: Point, b: Point): Int =  // 맨하탄 거리 계산 정적 메서드
            kotlin.math.abs(a.x - b.x) + kotlin.math.abs(a.y - b.y)
    }
}

fun combinationFunc(combinationList: MutableList<Point>, k: Int, m: Int) {  // 치킨집 좌표 조합을 생성하는 메서드
    if (combinationList.size == m) {  // M개로 이루어진 조합 완성 시
        var cityChickenDist = 0

        for (homePoint in homePoints) {  // 모든 집으로부터 각각 모든 치킨집을 순회하며 최소 치킨거리를 구해 도시치킨거리에 누적
            var minChickenDist = Int.MAX_VALUE
            for (chickenPoint in combinationList) {
                minChickenDist = minOf(minChickenDist, Point.distance(homePoint, chickenPoint))
            }
            cityChickenDist += minChickenDist

            if (cityChickenDist >= minCityChickenDist) {  // 여기서 이미 최소 도시치킨거리 이상인 경우 메서드 종료
                return
            }
        }

        minCityChickenDist = minOf(minCityChickenDist, cityChickenDist)  // 최소 도시치킨거리 업데이트
        return
    }

    for (i in k until chickenPoints.size) {  // 치킨집 좌표를 순회하며 재귀적으로 조합을 생성
        combinationList.add(chickenPoints[i])
        combinationFunc(combinationList, i + 1, m)
        combinationList.removeAt(combinationList.size - 1)
    }
}

var homePoints = mutableListOf<Point>()  // 집 좌표
var chickenPoints = mutableListOf<Point>()  // 치킨집 좌표
var minCityChickenDist = Int.MAX_VALUE  // 최소 도시치킨거리

fun main() {
    val (n, m) = readln().split(" ").map { it.toInt() }
    val graph = Array(n) { readln().split(" ").map { it.toInt() } }

    for (i in 0 until n) {
        for (j in 0 until n) {
            when (graph[i][j]) {
                1 -> homePoints.add(Point(i, j))  // 집 좌표 추가
                2 -> chickenPoints.add(Point(i, j))  // 치킨집 좌표 추가
            }
        }
    }

    combinationFunc(mutableListOf(), 0, m)  // 조합 생성 및 최소 도시치킨거리 계산

    println(minCityChickenDist)
}
