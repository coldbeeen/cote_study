import java.util.*;

class Solution {

    List<List<Integer>> list = new ArrayList<>();  // 원판 이동 과정을 저장할 list

    public void hanoi(int n, int start, int mid, int end) {  // 하노이 탑 재귀함수 (from n to 1)

        if (n == 1) {  // 1개의 원판은 바로 목적지로
            list.add(Arrays.asList(start, end));
        } else {  ,  n-1mid -> end
            hanoi(n-1, start, end, mid);  // n-1개 원판 start에서 mid로 (end를 거쳐서)
            list.add(Arrays.asList(start, end));  // 남은 1개의 원판 start에서 end로
            hanoi(n-1, mid, start, end);  // mid에 옮겨놨던 n-1개 원판 end로 (start를 거쳐서)
        }
    }

    public int[][] solution(int n) {

        hanoi(n, 1, 2, 3);  // 하노이 탑 재귀함수 실행

        // List<List<Integer>>를 int[][]로 변환
        int[][] answer = new int[list.size()][2];
        for (int i = 0; i < list.size(); i++)
            for (int j = 0; j < 2; j++)
                answer[i][j] = list.get(i).get(j);

        return answer;
    }
}