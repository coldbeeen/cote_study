// 풀이 시간: 20분
// 참고: 정렬 조건이 2개 이상인 경우의 정렬법을 서치함, 다중 XOR 계산법에 대해 서치함

import java.util.*;

class Solution {
    public int solution(int[][] data, int col, int row_begin, int row_end) {

        int answer = 0;

        Arrays.sort(data, Comparator.comparingInt((int[] a) -> a[col - 1])  // 조건에 맞게 정렬
                .thenComparing(Comparator.comparingInt((int[] a) -> a[0]).reversed()));


        for (int i = row_begin - 1; i <= row_end - 1; i++) {  // row_begin ~ row_end 순회

            int sumOfRemainder = 0;
            for (int j = 0; j < data[i].length; j++)  // 나머지의 합 계산
                sumOfRemainder += data[i][j] % (i + 1);

            answer ^= sumOfRemainder;  // bitwise XOR 계산
        }

        return answer;
    }
}