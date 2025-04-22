// 실행시간: 29분

import java.util.*;

class Solution {
    public double[] solution(int k, int[][] ranges) {

        double[] answer = new double[ranges.length];
        ArrayList<Double> area = new ArrayList<>(List.of(0.0));  // 누적합(DP)을 저장하기 위한 리스트
        int nextK;

        while (k > 1) {  // k가 1이 되기 전까지, 정적분 결과를 area 리스트에 추가


            if (k % 2 == 0)
                nextK = k / 2;
            else
                nextK = k * 3 + 1;

            area.add(area.get(area.size() - 1) + (k + nextK) / 2.0);  // 이전 k값과 현재 k값을 활용해 넓이를 구함 (사다리꼴)
            k = nextK;
        }

        for (int i = 0; i < ranges.length; i++) {  // range 순회하며 정적분 값 구하기

            int a = ranges[i][0], b = ranges[i][1];

            if (b > 0) b = b;
            else if (b < 0) b = area.size() + b - 1;
            else b = area.size() - 1;

            answer[i] = a <= b ? area.get(b) - area.get(a) : -1;  // b까지의 정적분에서 a까지의 정적분을 뺌
        }

        return answer;
    }
}