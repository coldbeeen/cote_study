// 풀이 시간: 16분
// 풀이 방법: 앞에서부터 시작해, 사람 위치 인덱스 i에서 i-k ~ i+k 까지 순회하며 햄버거를 Get!

fun main() {
    val (n, k) = readln().split(" ").map { it.toInt() }
    var chArr = readln().toCharArray()
    var result = 0

    for (i in 0 until n) {
        if (chArr[i] == 'P') {  // i 인덱스 값이 사람인 경우
            for (j in (i - k)..(i + k)) {  // i-k ~ i+k 순회
                if (j in 0 until n && chArr[j] == 'H') {  // 햄버거 Get !
                    result++  // result 증가
                    chArr[j] = 'X'  // 햄버거 표시를 H -> X로 수정 (중복 Get 방지)
                    break
                }
            }
        }
    }

    println(result)
}