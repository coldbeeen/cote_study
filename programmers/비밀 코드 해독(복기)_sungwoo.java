// 풀이 시간: 21분
// 풀이 방법: 모든 조합을 DFS(백트래킹)로 생성하고, 해당 조합을 q, ans 배열을 활용해 검증한다.

import java.util.*;

class Solution {

    int result = 0;

    public void combination(ArrayList<Integer> comb, int n, int i, int[][] q, int[] ans) {  // 조합 생성

        if (comb.size() == 5) {  // (재귀 종료 조건) 조합이 완성되면

            for (int idx = 0; idx < q.length; idx++) {  // q 배열 순회하며 조건에 맞는 조합인지 검증

                int correspondingCnt = 0;
                for (int input_num: q[idx])
                    if (comb.contains(input_num))
                        correspondingCnt++;

                if (correspondingCnt != ans[idx])  // 맞지 않다면 return
                    return;
            }

            result++;
            return;
        }

        for (int j = i; j <= n; j++) {  // 조합에 j를 추가하여 재귀
            comb.add(j);
            combination(comb, n, j + 1, q, ans);
            comb.remove(comb.size() - 1);
        }
    }

    public int solution(int n, int[][] q, int[] ans) {

        combination(new ArrayList<>(), n, 1, q, ans);
        return result;
    }
}