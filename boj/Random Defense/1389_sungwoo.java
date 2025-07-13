// 풀이 시간: 19분
// 풀이 방법: 각 유저마다 BFS를 수행하여 최솟값을 구함

import java.util.*;
import java.io.*;

public class Main {

    public static int minByBFS(ArrayList<ArrayList<Integer>> graph, int start) {

        Queue<Integer> q = new LinkedList<>();  // BFS 큐
        boolean[] visited = new boolean[graph.size()];  // 방문 여부 배열
        int[] distance = new int[graph.size()];  // 단계(거리) 배열
        q.offer(start);
        visited[start] = true;

        while (!q.isEmpty()) {

            int v = q.poll();

            for (int w: graph.get(v)) {

                if (!visited[w]) {
                    distance[w] = distance[v] + 1;
                    q.offer(w);
                    visited[w] = true;
                }
            }
        }

        return Arrays.stream(distance).sum();  // 케빈 베이컨 수 리턴
    }

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split(" ");
        int N = Integer.parseInt(s[0]), M = Integer.parseInt(s[1]);

        ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < N + 1; i++) {
            graph.add(new ArrayList<>());
        }

        for(int i = 0; i < M; i++) {  // 인접 그래프 생성
            s = br.readLine().split(" ");
            int v = Integer.parseInt(s[0]), w = Integer.parseInt(s[1]);
            graph.get(v).add(w);
            graph.get(w).add(v);
        }

        int min = Integer.MAX_VALUE, result = 0;
        for (int v = 1; v <= N; v++) {  // 각 유저의 케빈 베이컨 수를 구해 최솟값을 가지는 유저를 구함

            int vMin = minByBFS(graph, v);
            if (vMin < min) {
                min = vMin;
                result = v;
            }
        }

        System.out.println(result);
    }
}