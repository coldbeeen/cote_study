fun main() {

    val t = readln().toInt()

    repeat(t) {

        val n = readln().toInt()
        val dpTable = IntArray(n + 1) { 1 }  // DP 테이블 생성 (1로만 더하는 방법(1개)로 구성)

        for (i in 2..n)  // 2를 더하는 방법의 수 추가
            dpTable[i] += dpTable[i - 2]

        for (i in 3..n)  // 3을 더하는 방법의 수 추가
            dpTable[i] += dpTable[i - 3]

        println(dpTable[n])  // n을 만드는 방법의 수 출력
    }
}

// 하나의 점화식으로 도출하려다보니 잘 풀리지 않아 어려웠네요.
// 1, 2, 3을 더하는 방법의 수를 순차적으로 DP를 수행해 답을 구해내는 문제... 재밌었습니다...람쥐