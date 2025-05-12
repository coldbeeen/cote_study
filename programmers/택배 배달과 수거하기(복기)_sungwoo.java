// 풀이 시간: 28분
// 풀이 방법: 역방향으로 순회하며 배달과 수거를 그리디하게 수행한다.

class Solution {
    public long solution(int cap, int n, int[] deliveries, int[] pickups) {

        int i = deliveries.length - 1, right = deliveries.length - 1;  // right는 방문해야하는 가장 오른쪽 지점
        int deliver = 0, pickup = 0;  // 배달과 수거 현황
        long answer = 0;

        while (i >= 0) {  // i를 역방향으로 순회

            if (deliver + deliveries[i] > cap || pickup + pickups[i] > cap) {  // 트럭 용량 초과로 물류창고에 가야하는 경우

                deliveries[i] -= (cap - deliver);  // 배달 및 수거를 최대한 cap에 맞춰 수행하기 위해 갱신
                pickups[i] -= (cap - pickup);

                answer += (right + 1) * 2;  // 거리 누적
                right = i;  // right 지점 갱신
                deliver = pickup = 0;  // 배달 및 수거 현황 초기화

            } else {  // 배달 및 수거 현황 갱신

                deliver += deliveries[i];
                pickup += pickups[i];
                i--;
            }
        }

        if (answer + pickup + deliver > 0)  // 마지막 동선 거리 누적 (배달 및 수거가 없는 경우를 위한 조건문)
            answer += (right + 1) * 2;

        return answer;
    }
}