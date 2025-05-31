// 풀이 시간: 28분
// 풀이 방법: DFS를 활용해 완전 탐색을 진행하여 풀었다.
//         (최대 9자리이므로 2^9개 경우의 수는 크지 않다.)

import java.util.*;

class Solution {

    public int DFS(ArrayList<Integer> digitList, int i, int stoneCnt) {

        if (i == digitList.size() - 1)   // 첫 번째 자리수 까지 다 고려하였다면
            return stoneCnt + digitList.get(i);  // 올림된 숫자를 더해 리턴

        // 1. i번째 숫자만큼을 그대로 내려감
        int case1 = DFS(digitList, i + 1, stoneCnt + digitList.get(i));

        // 2. (10 - i번째 숫자) 만큼 올라감
        digitList.set(i + 1, digitList.get(i + 1) + 1);  // 다음 자릿수 올림
        int case2 = DFS(digitList, i + 1, stoneCnt + (10 - digitList.get(i)));
        digitList.set(i + 1, digitList.get(i + 1) - 1);  // 다음 자릿수 원상복구

        return Math.min(case1, case2);  // 최솟값을 리턴
    }

    public int solution(int storey) {

        ArrayList<Integer> digitList = new ArrayList<>();
        while (storey > 0) {  // storey 각 자리의 숫자를 역으로 저장
            digitList.add(storey % 10);
            storey /= 10;
        }
        digitList.add(0);  // 지릿수가 올림될 수 있으므로 마지막에 0을 추가

        return DFS(digitList, 0, 0);  // DFS 수행 및 결과 리턴
    }
}