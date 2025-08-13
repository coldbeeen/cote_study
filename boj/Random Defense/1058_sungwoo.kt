// 풀이 시간: 30분
// 풀이 방법: BFS를 이용해 각 사람의 2-친구 수를 구하고 최댓값을 찾음

import java.util.*

fun bfs(graph: List<List<Int>>, n: Int, v: Int): Int {  // 2-친구 수를 리턴하는 BFS 메서드

    val q = LinkedList<Pair<Int, Int>>()  // BFS 수행을 위한 큐 구현체 생성 (노드번호, 거리)
    val visited = BooleanArray(n)
    var result = 0  // 2-친구 수

    q.offer(Pair(v, 0))  // 큐 초깃값
    visited[v] = true

    while (q.isNotEmpty()) {

        val (node, count) = q.poll()

        if (count >= 2)  // 2-친구 기준을 만족하지 않으면 continue
            continue

        for (nextNode in graph[node]) {  // 연결된 친구 순회

            if (!visited[nextNode]) {  // 방문하지 않은 노드라면 result 증가 및 큐에 삽입
                result++
                q.offer(Pair(nextNode, count + 1))
                visited[nextNode] = true
            }
        }
    }

    return result
}

fun main() {

    // 1. 입력 및 그래프 생성
    val n = readln().toInt()
    val graph = MutableList<MutableList<Int>>(n) { mutableListOf() }
    for (i in 0 until n)  // 입력받은 문자열에서 'Y'만 필터링한 해당 인덱스 번호 리스트를 graph[i]에 추가
        graph[i].addAll(readln().withIndex().filter { it.value == 'Y' }.map { it.index })

    // 2. 각 노드에서 2-친구 수를 구하는 BFS 수행 후 max 값을 구함
    var answer = (0 until n).maxOf { bfs(graph, n, it) }
    println(answer)  // 최종 결과 출력
}