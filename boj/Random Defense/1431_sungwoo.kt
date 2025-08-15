// 풀이시간: 23분

fun main() {

    val n = readln().toInt()
    val serialList = MutableList(n) { readln() }

    serialList.sortWith(  // 문자열 길이, 숫자의 합, 사전 순으로 정렬
        compareBy<String> { it.length }
            .thenBy { it.filter { char -> char.isDigit() }.sumOf { char -> char.digitToInt() } }
            .thenBy { it })

    serialList.forEach { println(it) }
}