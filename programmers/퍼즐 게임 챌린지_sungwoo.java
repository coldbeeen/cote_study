// 풀이 시간: 40분 20초

class Solution {

    public long calculateCost(int[] diffs, int[] times, int level) {  // 모든 퍼즐 소요 시간 계산 함수
        long result = 0;  // 총 소요시간
        long cost, tmp = 0;  // 현재 퍼즐 소요 시간, 이전 퍼즐 소요 시간

        for (int i = 0; i < diffs.length; i++) {  // 모든 퍼즐을 순회하며 소요 시간 계산
            if (diffs[i] <= level)
                cost = times[i];
            else
                cost = times[i] + (times[i] + tmp) * (diffs[i] - level);  // 난이도를 고려한 계산

            result += cost;  // 계산한 현재 퍼즐 소요 시간 누적
            tmp = times[i];  // 다음 퍼즐에서 활용할 수 있도록 임시 저장
        }

        return result;
    }

    public int solution(int[] diffs, int[] times, long limit) {

        int left = 1, right = 100000;  // 범위 설정

        while (left <= right) {  // 이분 탐색 수행 (적절한 숙련도 탐색)
            int mid = (left + right) / 2;
            long cost = calculateCost(diffs, times, mid);  // 숙련도 mid일 때 퍼즐 소요 시간 계산

            if (cost > limit)  // 제한 시간을 넘기면 숙련도 up
                left = mid + 1;
            else if (cost < limit)  // 제한 시간을 넘기지 않으면 숙련도 down
                right = mid - 1;
            else  // 제한시간과 일치하더라도 최소 숙련도를 구해야하기 때문에 숙련도 down
                right = mid - 1;
        }

        return left;
    }
}