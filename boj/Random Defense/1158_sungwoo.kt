// 풀이 시간: 30분 이상
// 풀이 방법: 1 ~ N까지의 번호를 연결리스트에 저장한 뒤, N번 동안 K번째 사람을 제거하며 result에 삽입

import java.util.*

fun main() {

    // 0. 입력
    val (n, k) = readln().split(" ").map { it.toInt() }

    // 1. 연결리스트 1 ~ N로 초기화
    val list = LinkedList<Int>((1..n).toList())

    // 2. curIdx를 활용해 매 반복에서 K번째 사람을 제거
    val result = mutableListOf<Int>()  // 제거한 번호를 삽입할 리스트
    var curIdx = 0
    while (list.isNotEmpty()) {
        curIdx = (curIdx + (k - 1)) % list.size  // curIdx에서 k번째 인덱스를 curIdx로 갱신
        result.add(list.removeAt(curIdx))  // curIdx번 인덱스 값 삭제 후 result에 삽입 (연결리스트이므로 인덱스 기반 remove은 O(n))
    }

    // 3. 최종 출력
    println("<${result.joinToString(", ")}>")
}

// nlog(n) 풀이를 고민하다가 포기함.
// 문제 조건을 보고 당연히 n^2은 시간 초과라고 예상했는데
// n^2 풀이가 답이었음(?)
// 그래서 기존 n^2 아이디어로 풀이함.
// 그리고 링크드리스트, 큐, 리스트 어떤 풀이로 해도 O(n^2)인데? 사실상 다 가능한 풀이 방범임.