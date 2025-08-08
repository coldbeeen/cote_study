// 풀이 시간: 16분
// 풀이 방법: after를 끝까지 순회하면서 before와 비교해가며 추월한 차를 카운트 -> O(N)으로 해결

fun main() {

    // 0. 입력 받기
    val n = readln().toInt()
    val before = List(n) { readln() }
    val after = List(n) { readln() }

    // 1. after를 끝까지 순회 (before와 비교해가며 추월한 차를 카운트)
    var result = 0  // 추월한 차 대수
    var beforeIdx = 0
    var afterIdx = 0
    val set = mutableSetOf<String>()  // 추월한 차는 before에서 건너뛸 수 있도록 set에 저장해 확인하도록 함

    while (afterIdx < n) {

        if (set.contains(before[beforeIdx])) {  // beforeIdx에 해당하는 차가 이미 추월했던 차인 경우 건너뜀 (순차적으로 O(1)으로 확인하기 위함)
            beforeIdx++
            continue
        }

        if (before[beforeIdx] != after[afterIdx]) {  // 현재 before와 after의 차가 다르다면 afterIdx에 해당하는 차가 추월한 것!
            set.add(after[afterIdx])  // Set에 추가하고 추월 카운트 증가 및 afterIdx 증가
            afterIdx++
            result++
        } else {  // 현재 before와 after의 차가 같다면 afterIdx에 해당하는 차는 추월하지 않은 차임
            beforeIdx++
            afterIdx++
        }
    }

    println(result)
}

// 좋은 예시
// before: Z P R A B
// after:  P B A Z R