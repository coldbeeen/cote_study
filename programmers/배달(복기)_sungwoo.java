// 풀이 시간: 25분
// 풀이 방법: 이번에는 다익스트라를 바로 적용하여 풀어냈다. (기억이 잘 나지 않았으나 머리 쥐어 짜내서 어떻게 잘 풀어냈다)

import java.util.*;

class Solution {

    public int findMinCostIdx(int[] dist, boolean[] visited) {  // 방문하지 않은, 비용이 가장 낮은 인덱스 리턴

        int minIdx = 0;
        for (int i = 1; i < dist.length; i++)
            if (!visited[i] && dist[i] < dist[minIdx])
                minIdx = i;

        return minIdx;
    }

    public int solution(int N, int[][] road, int K) {

        ArrayList<ArrayList<ArrayList<Integer>>> adjList = new ArrayList<>();  // 비용을 포함하는 인접 리스트 (3차원 리스트)

        for (int i = 0; i <= N; i++)  // 내부 리스트 초기화
            adjList.add(new ArrayList<ArrayList<Integer>>());

        for (int[] r: road) {  // 인접 리스트 생성
            adjList.get(r[0]).add(new ArrayList<>(List.of(r[1], r[2])));
            adjList.get(r[1]).add(new ArrayList<>(List.of(r[0], r[2])));
        }

        int[] cost = new int[N + 1];  // 비용 배열
        boolean[] visited = new boolean[N + 1];  // 방문 여부 배열

        for (int i = 0; i < N + 1; i++)  // 모든 비용을 최댓값으로 설정
            cost[i] = Integer.MAX_VALUE;

        cost[1] = 0;  // 1번 마을부터 시작!

        for (int i = 0; i < N - 1; i++) {  // 다익스트라 알고리즘 수행 (1번 마을은 제외되므로 N-1번 반복)

            int from = findMinCostIdx(cost, visited);  // 비용이 가장 적은 마을을 찾음

            for (ArrayList<Integer> adj: adjList.get(from)) {  // 인접한 마을을 순회하며

                int to = adj.get(0), thisCost = adj.get(1);

                if (cost[from] + thisCost < cost[to]) {  // 기존 비용 배열의 값보다 from에서 더 적은 비용으로 방문할 수 있다면
                    cost[to] = cost[from] + thisCost;  // 해당 비용으로 갱신함
                }
            }

            visited[from] = true;  // 방문 처리
        }

        int result = 0;
        for (int i = 1; i < N + 1; i++) {  // K 이하의 마을 카운팅
            if (cost[i] <= K)
                result++;
        }

        return result;
    }
}