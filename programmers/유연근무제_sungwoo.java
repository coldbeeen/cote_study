// 풀이 시간: 14분

class Solution {

    public int toMin(int n) {  // 분으로 변환하는 함수
        return (n / 100) * 60 + n % 100;
    }

    public int solution(int[] schedules, int[][] timelogs, int startday) {

        int answer = 0;

        for (int i = 0; i < schedules.length; i++) {

            boolean late = false;

            for (int j = 0; j < timelogs[i].length; j++) {

                if ((startday + j - 1) % 7 == 5 || (startday + j - 1) % 7 == 6)  // 토/일은 건너뜀
                    continue;

                if (toMin(timelogs[i][j]) > toMin(schedules[i] + 10)) {  // 10분 이상 늦었다면 반복문 종료
                    late = true;
                    break;
                }
            }

            if (!late)  // 늦은 적이 없다면 answer 증가
                answer++;
        }

        return answer;
    }
}