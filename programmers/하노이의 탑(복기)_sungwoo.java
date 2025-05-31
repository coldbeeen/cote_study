// 풀이 시간: 17분

import java.util.*;

class Solution {

    ArrayList<ArrayList<Integer>> result = new ArrayList<>();  // 결과 리스트

    // 하노이탑 재귀 함수 (n-1개를 from -> mid로 보관한 뒤, from -> to 수행 후, 보관했던 n-1개를 mid -> to)
    public void hanoi(int from, int mid, int to, int n) {

        if (n > 0) {
            hanoi(from, to, mid, n - 1);
            result.add(new ArrayList<>(List.of(from, to)));
            hanoi(mid, from, to, n - 1);
        }
    }

    public int[][] solution(int n) {

        hanoi(1, 2, 3, n);  // n개를 1에서 3으로 옮기기 위해 hanoi 함수 호출

        int[][] answer = new int[result.size()][2];  // 배열로 변환
        for (int i = 0; i < result.size(); i++)
            for (int j = 0; j < 2; j++)
                answer[i][j] = result.get(i).get(j);

        return answer;
    }
}