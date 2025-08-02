// 풀이시간: 25분

import java.io.*;
import java.util.*;

public class Main
{

    public static final int MAX = 99_999_999;

    public static int dijkstra(List<List<int []>> graph, int N) {

        PriorityQueue<int []> pq = new PriorityQueue<>((a, b) -> Integer.compare(a[1], b[1]));  // 1번 인덱스(비용) 기반 힙 생성
        int[] costArray = new int[N + 1];  // cost 배열 초기화
        Arrays.fill(costArray, MAX);
        costArray[1] = 0;

        pq.offer(new int[] {1, 0});  // 1번 노드부터 시작해 탐색 시작

        while (!pq.isEmpty()) {

            int[] nodeAndCost = pq.poll();
            int node = nodeAndCost[0], cost = nodeAndCost[1];

            for (int [] adjacentNodeAndCost: graph.get(node)) {  // 인접한 노드 순회

                int adjacentNode = adjacentNodeAndCost[0], adjacentCost = adjacentNodeAndCost[1];

                if (cost + adjacentCost < costArray[adjacentNode]) {  // 현재의 인접한 노드를 거쳐가는 것이 더 적은 비용이라면 갱신 후 힙에 삽입
                    costArray[adjacentNode] = cost + adjacentCost;
                    pq.offer(new int[] {adjacentNode, costArray[adjacentNode]});
                }

            }
        }

        return costArray[N];
    }


    public static void main(String[] args) throws Exception{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken()), M = Integer.parseInt(st.nextToken());

        List<List<int []>> graph = new ArrayList<>();

        for (int i = 0; i <= N; i++) {  // 그래프에 각 노드의 인접 노드 삽입을 위해 리스트 초기화
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < M; i++) {  // M개의 간선을 입력 받아 인접 리스트 구조 생성
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken()), b = Integer.parseInt(st.nextToken()), c = Integer.parseInt(st.nextToken());
            graph.get(a).add(new int[] {b, c});
            graph.get(b).add(new int[] {a, c});
        }

        System.out.println(dijkstra(graph, N));  // 다익스트라 메서드 호출
    }
}