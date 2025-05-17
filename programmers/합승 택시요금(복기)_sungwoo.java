// 풀이 시간: 40분

import java.util.*;

class Solution {

    public int[] dijkstra(ArrayList<ArrayList<ArrayList<Integer>>> adjList, int n, int start) {  // 다익스트라 수행

        PriorityQueue<ArrayList<Integer>> pq = new PriorityQueue<>((a, b) -> a.get(1) - b.get(1));  // cost 값 기반 우선순위 큐
        int[] cost = new int[n + 1];
        Arrays.fill(cost, Integer.MAX_VALUE);

        pq.offer(new ArrayList<>(List.of(start, 0)));
        cost[start] = 0;

        while (!pq.isEmpty()) {

            ArrayList<Integer> vertexAndCost = pq.poll();
            int v1 = vertexAndCost.get(0), c1 = vertexAndCost.get(1);

            if (c1 > cost[v1])
                continue;

            for (ArrayList<Integer> adj: adjList.get(v1)) {
                int v2 = adj.get(0), c2 = adj.get(1);

                if (cost[v1] + c2 < cost[v2]) {
                    cost[v2] = cost[v1] + c2;
                    pq.offer(new ArrayList<>(List.of(v2, cost[v2])));
                }
            }
        }

        return cost;
    }

    public int solution(int n, int s, int a, int b, int[][] fares) {

        ArrayList<ArrayList<ArrayList<Integer>>> adjList = new ArrayList<>();  // 인접 리스트 초기화
        for (int i = 0; i < n + 1; i++)
            adjList.add(new ArrayList<>());

        for (int[] fare: fares) {  // 인접 리스트 생성
            adjList.get(fare[0]).add(new ArrayList<>(List.of(fare[1], fare[2])));
            adjList.get(fare[1]).add(new ArrayList<>(List.of(fare[0], fare[2])));
        }

        int[] costFromS = dijkstra(adjList, n, s);  // s부터 모든 정점까지의 비용을 구함

        int result = Integer.MAX_VALUE;

        for (int i = 1; i <= n; i++) {  // mid(동승 지점)을 i ~ n까지 순회

            int[] costFromMid = dijkstra(adjList, n, i);  // i부터 모든 정점까지의 비용을 구하고
            int realCost = costFromS[i] + costFromMid[a] + costFromMid[b];  // 총 비용을 구함

            result = Math.min(result, realCost);  // 최솟값 갱신
        }

        return result;
    }
}