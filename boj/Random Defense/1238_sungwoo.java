// 풀이 시간: 34분
// 풀이 방법: 다익스트라 알고리즘 힙으로 구현하여,
//            1~N → X 비용과, X → 1~N 비용을 계산해 최댓값을 구하면 된다.

import java.io.*;
import java.util.*;

public class Main
{
    public static int MAX = 200000;

    public static int[] dijkstra(ArrayList<ArrayList<ArrayList<Integer>>> adjList, int start, int N) {  // 다익스트라 힙 구현

        int[] costArr = new int[N + 1];  // 초기 비용 배열
        Arrays.fill(costArr, MAX);  // MAX로 초기화
        costArr[start] = 0;  // start 정점의 비용은 0으로

        PriorityQueue<ArrayList<Integer>> pq = new PriorityQueue<>((a, b) -> Integer.compare(a.get(1), b.get(1)));  // 비용 기반 비교 힙 생성
        pq.offer(new ArrayList<>(List.of(start, 0)));  // 시작점 삽입

        while (!pq.isEmpty()) {

            ArrayList<Integer> vCost = pq.poll();
            int v = vCost.get(0), cost = vCost.get(1);

            for (int i = 0; i < adjList.get(v).size(); i++) {  // 간선 순회
                int nextV = adjList.get(v).get(i).get(0);
                int nextCost = adjList.get(v).get(i).get(1);

                if (costArr[v] + nextCost < costArr[nextV]) {  // 해당 간선을 거쳐갈 경우 costArr의 비용보다 적다면 갱신 후 힙에 삽입
                    costArr[nextV] = costArr[v] + nextCost;
                    pq.offer(new ArrayList<>(List.of(nextV, costArr[nextV])));
                }
            }
        }

        return costArr;  // 비용 배열 리턴
    }

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken()), M = Integer.parseInt(st.nextToken()), X = Integer.parseInt(st.nextToken());

        ArrayList<ArrayList<ArrayList<Integer>>> adjList = new ArrayList<>();  // 인접 행렬 생성

        for (int i = 0; i <= N; i++)
            adjList.add(new ArrayList<>());

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken()), end = Integer.parseInt(st.nextToken()), cost = Integer.parseInt(st.nextToken());
            adjList.get(start).add(new ArrayList<>(List.of(end, cost)));
        }

        int[] costArrOfX = dijkstra(adjList, X, N);  // 가장 먼저 X를 시작점으로 하는 비용 배열을 구함
        int result = 0;
        for (int i = 1; i <= N; i++) {  // 1 ~ N을 순회하며, (i → X까지의 비용 + X → i까지의 비용)의 최댓값을 구함
            int[] costArrOfI = dijkstra(adjList, i, N);
            result = Math.max(result, costArrOfI[X] + costArrOfX[i]);
        }

        System.out.println(result);
    }
}