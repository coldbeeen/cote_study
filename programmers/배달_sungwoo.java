// 풀이 시간: BFS 35분 + 다익스트라 20분 (구글링)

import java.util.*;

class Solution {

    public int getMinIndex(int[] list, boolean[] visited) {  // 방문하지 않은 곳 중 최솟값을 가지는 인덱스 리턴 (for Dijkstra)

        int min = Integer.MAX_VALUE, minIdx = 0;

        for (int i = 0; i < list.length; i++) {
            if (!visited[i] && list[i] < min) {
                min = list[i];
                minIdx = i;
            }
        }

        return minIdx;
    }

    public int solution(int N, int[][] road, int K) {

        // 1. road를 인접리스트로 표현하기

        ArrayList<ArrayList<ArrayList<Integer>>> roadGraph = new ArrayList<>();
        for(int i = 0; i < N + 1; i++) {
            roadGraph.add(new ArrayList<>());
        }

        for(int[] r: road) {
            int from = r[0], to = r[1], cost = r[2];
            roadGraph.get(from).add(new ArrayList<>(List.of(to, cost)));
            roadGraph.get(to).add(new ArrayList<>(List.of(from, cost)));
        }


        // 2. 다익스트라를 수행하며 각 마을까지의 비용 계산

        int[] costList = new int[N + 1];  // 다익스트라 결과를 담을 비용 List
        for (int i = 0; i < N + 1; i++)
            costList[i] = Integer.MAX_VALUE;
        boolean[] visited = new boolean[N + 1];  // 방문 여부

        costList[1] = 0;  // 1번 마을부터 시작 (1번 마을의 비용: 0)

        for (int i = 0; i < N - 1; i++) {

            int minNode = getMinIndex(costList, visited);  // 방문하지 않은 최소 비용 마을 찾기
            visited[minNode] = true;  // 방문 처리

            for (List<Integer> adjacentNode: roadGraph.get(minNode)) {  // minNode를 기준으로 인접 노드의 거리 갱신

                int from = minNode, to = adjacentNode.get(0), cost = adjacentNode.get(1);

                if (costList[from] + cost < costList[to])  // 현재 노드 값 + 인접 노드로의 값을, 인접 노드 최소 비용과 비교하여 갱신
                    costList[to] = costList[from] + cost;
            }
        }

        // 3. 배달 가능 마을 수 계산

        int answer = 0;

        for (int cost: costList)
            if (cost <= K)
                answer++;

        return answer;
    }
}