// 풀이 시간: 45분

import java.util.*;

class Solution {

    public int nodeSearch(int n, ArrayList<ArrayList<Integer>> wireList) {  // BFS를 수행하며 탐색한 노드 수를 리턴함

        Queue<Integer> q = new LinkedList<>();  // 큐
        boolean[] visited = new boolean[n + 1];  // 방문 여부 배열
        int nodeCnt = 0;  // 방문한 노드 수
        q.offer(1);  // 1번 노드부터

        while (!q.isEmpty()) {  // 1번 노드부터 시작해 BFS를 수행하며 인접한 노드를 방문

            int node = q.poll();
            ArrayList<Integer> adjacentNodeList = wireList.get(node);

            for (int adjacentNode: adjacentNodeList) {

                if (visited[adjacentNode])
                    continue;

                q.offer(adjacentNode);
                visited[adjacentNode] = true;
                nodeCnt++;
            }
        }

        return nodeCnt;
    }

    // 하나의 전선을 제외한 인접 리스트 생성 메서드
    public ArrayList<ArrayList<Integer>> createAdjacentList(int n, int[][] wires, int exclude) {

        ArrayList<ArrayList<Integer>> wireList = new ArrayList<>();

        for (int i = 0; i <= n; i++)
            wireList.add(new ArrayList<>());

        for (int i = 0; i < wires.length; i++) {

            if (i == exclude)  // exclude 인덱스의 전선은 제외
                continue;

            wireList.get(wires[i][0]).add(wires[i][1]);
            wireList.get(wires[i][1]).add(wires[i][0]);
        }

        return wireList;
    }

    public int solution(int n, int[][] wires) {

        int minDiff = Integer.MAX_VALUE;  // 두 전력망의 송전탑 차이 최솟값

        for (int i = 0; i < wires.length; i++) {  // wires[i]를 제외시킨 모든 경우의 수를 순회

            ArrayList<ArrayList<Integer>> wireList = createAdjacentList(n, wires, i);  // i번째 wire를 제외한 인접리스트 생성

            int nodeCnt = nodeSearch(n, wireList);  // 인접한 노드 탐색
            int diff = Math.abs(Math.abs(n - nodeCnt) - nodeCnt);  // 두 전력망의 송전탑 차이 계산

            minDiff = Math.min(minDiff, diff);  // 최솟값 갱신
        }

        return minDiff;
    }
}

// 문제 설명과 조건을 고려하여 전선을 하나씩 제외시킨 모든 전력망 경우의 수를 완전탐색하고자 하였음
// i번째 전선을 제외한 인접리스트를 생성하고, 해당 인접리스트를 활용해 BFS를 수행하여 | |n - nodeCnt| - nodeCnt | 수식을 통해 두 전력망의 송전탑 차이를 구함
