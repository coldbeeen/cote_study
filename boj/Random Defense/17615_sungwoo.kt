// 풀이 시간: 20분
// 풀이 방법:
// 1. 앞에서부터 시작해 R 뒤로 옮기기
// 2. 앞에서부터 시작해 B 뒤로 옮기기
// 3. 뒤에서부터 시작해 R 뒤로 옮기기
// 4. 뒤에서부터 시작해 B 뒤로 옮기기

private const val RED = 'R'   // 빨간 공
private const val BLUE = 'B'  // 파란 공

// 특정 공(ch)을 모두 "뒤로" 옮기기 위해 필요한 최소 이동 횟수를 계산
fun moveCharToRear(ballList: List<Char>, ch: Char): Int {
    var result = 0
    val lastIndexOfNotChar = ballList.lastIndexOf(if (ch == RED) BLUE else RED)  // ch와 다른 공의 마지막 위치를 찾음

    for (i in 0 until lastIndexOfNotChar) {  // 해당 위치까지 순회하며 ch가 나타나면 이동 횟수 증가
        if (ballList[i] == ch)
            result++
    }
    return result
}

// 특정 공(ch)을 모두 "앞으로" 옮기기 위해 필요한 최소 이동 횟수를 계산
fun moveCharToFront(ballList: List<Char>, ch: Char): Int {
    var result = 0
    val firstIndexOfNotChar = ballList.indexOf(if (ch == RED) BLUE else RED)

    for (i in ballList.size - 1 downTo firstIndexOfNotChar + 1) {  // 뒤에서부터 순회하며 ch가 나타나면 이동 횟수 증가
        if (ballList[i] == ch)
            result++
    }
    return result
}

fun main() {
    val n = readln().toInt()
    val balls = readln()
    val ballList = balls.toList()

    var minResult = Int.MAX_VALUE

    minResult = minOf(minResult, moveCharToRear(ballList, RED))   // R을 뒤로
    minResult = minOf(minResult, moveCharToRear(ballList, BLUE))  // B를 뒤로
    minResult = minOf(minResult, moveCharToFront(ballList, RED))  // R을 앞으로
    minResult = minOf(minResult, moveCharToFront(ballList, BLUE)) // B를 앞으로

    println(minResult)  // 최소 이동 횟수 출력
}
