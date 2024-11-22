// 풀이 시간: 25분 10초

import java.util.*;

class Solution {
    public int[] solution(int n, long left, long right) {
        int[] answer = new int[(int) (right - left + 1)];  // 정답 배열 생성

        for (long i = left; i <= right; i++) {  // left ~ right까지 반복하며 알아낸 규칙에 따라 answer을 채움
            int row = (int) (i / n), col = (int) (i % n);  // (ㅇㅏ행, 열을 구하고
            if (col <= row)  // 열 값이 행 값 이하라면 행 값을 채움
                answer[(int) (i - left)] = row + 1;
            else  // 열 값이 행 값보다 크다면 열 값을 채움
                answer[(int) (i - left)] = col + 1;
        }

        return answer;
    }
}