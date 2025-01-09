// 풀이 시간: 20분

import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {

        ArrayList<Integer> answer = new ArrayList<>();
        int remainingDays = (int) Math.ceil((100.0 - progresses[0]) / speeds[0]);  // 각 작업의 배포까지 남은 일자 변수
        int distDays = remainingDays, cnt = 1;  // distDays: 이번 배포의 남은 일자 변수, cnt: 각 배포 작업 개수 변수

        for (int i = 1; i < progresses.length; i++) {

            remainingDays = (int) Math.ceil((100.0 - progresses[i]) / speeds[i]);

            if (remainingDays > distDays) {  // 이번 작업의 배포까지 남은 일자가 distDays보다 길다면 cnt개의 작업 배포
                answer.add(cnt);  // cnt개의 작업 배포
                cnt = 1;  // cnt 초기화
                distDays = remainingDays;  // distDays 초기화
                continue;
            }

            cnt++;
        }

        answer.add(cnt);  // 남은 cnt개의 작업 마지막 배포
        return answer.stream().mapToInt(i -> i).toArray();  // 배열로 변환하여 리턴
    }
}