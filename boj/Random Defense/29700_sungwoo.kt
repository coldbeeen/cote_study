// 풀이 시간: 13분
// 풀이 방법: K 범위 내 front/rear 값만 업데이트하여 예매 가능한 좌석을 찾음 (슬라이딩 윈도우)

fun main() {
    val (n, m, k) = readln().split(" ").map { it.toInt() }
    val seats = List(n) { readln().map { it.digitToInt() } }  // 2차원 int list로 입력

    var result = 0

    for (i in 0 until n) {

        var unavailableCnt = 0  // K 범위 내에서 사용 불가능한 좌석 수

        for (j in 0 until m) {  // i행 모든 좌석 순회

            if (seats[i][j] == 1) {  // 사용 불가능한 좌석이라면
                unavailableCnt++
            }

            if (j >= k - 1) {  // j가 K - 1 이상이라면 (K개의 요소를 보았다면)
                if (unavailableCnt == 0) {  // 현재 윈도우의 unavailableCnt가 0일 때 result 증가
                    result++
                }
                if (seats[i][j - (k - 1)] == 1) {  // 현재 윈도우의 front는 다음 반복에서 고려 X (unavailableCnt 갱신)
                    unavailableCnt--
                }
            }
        }
    }

    println(result)
}