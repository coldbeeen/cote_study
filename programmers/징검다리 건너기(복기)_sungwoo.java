// 풀이 시간: 42분
// 풀이 방법: 이분 탐색을 통해 건널 수 있는 인원의 최댓값을 구함
//         mid보다 작은 k개의 연속된 구간이 존재하면 건널 수 없는 것임!

import java.util.*;

class Solution {
    public int solution(int[] stones, int k) {

        int start = 0, end = 200000000, mid = 0;

        while (start <= end) {  // 이분탐색 시작

            mid = (start + end) / 2;
            boolean up = true;

            for (int i = 0; i < stones.length; i++) {

                int j = 0;  // mid보다 작은 연속된 구간을 구함. j는 연속된 구간의 길이
                while (i < stones.length && stones[i] < mid) {
                    i++; j++;
                }

                if (j >= k) {  // k 이상의 구간이 발견되었다면 건널 수 없음
                    up = false;
                    break;
                }
            }

            if (up)  // 건널 수 있다면 더 큰 값의 범위 탐색
                start = mid + 1;
            else  // 건널 수 없다면 더 작은 값의 범위 탐색
                end = mid - 1;
        }

        return end;  // 최종적으로 end에 건널 수 있는 최댓값이 들어가게 됨
    }
}