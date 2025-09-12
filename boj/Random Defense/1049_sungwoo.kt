// 풀이 시간: 15분
// 풀이 방법: 가장 싼 패키지 가격 및 낱개 가격을 구해 조건 분기

fun main() {
    val (n, m) = readln().split(" ").map { it.toInt() }
    var minPackageCost = Int.MAX_VALUE
    var minCost = Int.MAX_VALUE

    repeat(m) {
        val (pc, c) = readln().split(" ").map { it.toInt() }
        minPackageCost = minOf(minPackageCost, pc)
        minCost = minOf(minCost, c)
    }

    val result = minOf(
        (n / 6) * minPackageCost + minOf(minPackageCost, (n % 6) * minCost),
        n * minCost
    )
    println(result)
}