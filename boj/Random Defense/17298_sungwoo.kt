import java.util.*

fun main() {
    val n = readln().toInt()
    val arr = readln().split(" ").map { it.toInt() }
    val result = IntArray(n) { -1 }
    val stack = Stack<Int>()

    stack.push(arr[n - 1])

    for (i in n - 2 downTo 0) {
        while (stack.isNotEmpty() && arr[i] >= stack.peek()) {  // 현재 값보다 작거나 같은 값은 앞으로 오큰수가 될 수 없음 -> 제거
            stack.pop()
        }

        if (stack.isNotEmpty()) {  // 스택이 비어있지 않다면 top 값이 오큰수
            result[i] = stack.peek()
        }

        stack.push(arr[i])  // 모든 값은 오큰수의 후보가 될 수 있음
    }

    println(result.joinToString(" "))
}