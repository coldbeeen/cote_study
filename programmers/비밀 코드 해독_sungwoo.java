// 풀이 시간: 35분 (구글링)

import java.util.*;

class Solution {

    int answer = 0;

    public void search(HashSet<Integer> comb, int n, int idx, int[][] q, int[] ans) {

        if (comb.size() == 5) {

            for (int i = 0; i < q.length; i++) {

                int cnt = 0;
                for (int j = 0; j < q[i].length; j++)
                    if(comb.contains(q[i][j]))
                        cnt++;

                if (cnt != ans[i])
                    return;
            }

            answer++;
            return;
        }

        for(int i = idx; i <= n; i++) {
            comb.add(i);
            search(comb, n, i + 1, q, ans);
            comb.remove(i);
        }
    }

    public int solution(int n, int[][] q, int[] ans) {

        search(new HashSet<>(), n, 1, q, ans);
        return answer;
    }
}