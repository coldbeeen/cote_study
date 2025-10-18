fun main() {
    val roomNumber = readln()
    val count = IntArray(10)

    // 각 숫자 카운트
    for (ch in roomNumber) {
        val digit = ch - '0'
        count[digit]++
    }

    // 6과 9 합쳐서 세트 계산
    val sixNineSet = (count[6] + count[9] + 1) / 2

    // 6과 9는 제외하고 나머지 숫자 중 최대값 찾기
    var maxCount = sixNineSet
    for (i in 0..9) {
        if (i == 6 || i == 9) continue
        maxCount = maxOf(maxCount, count[i])
    }

    println(maxCount)
}