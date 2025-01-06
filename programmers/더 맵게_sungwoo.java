// 풀이 시간: 18분

import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {

        PriorityQueue<Integer> pq = new PriorityQueue<>();  // 우선순위 큐 생성
        int cnt = 0;  // 섞은 횟수

        for (int i = 0; i < scoville.length; i++)  // scoville 배열을 우선순위 큐로 변환
            pq.offer(scoville[i]);


        while (pq.size() >= 2) {  // 크기가 2 이상인 동안 반복 (poll을 두번 수행하기 때문)

            if (pq.peek() >= K)  // 최솟값이 K 이상이라면 cnt 리턴
                return cnt;

            pq.offer(pq.poll() + pq.poll() * 2);  // 섞은 음식 스코빌 지수 추가
            cnt++;
        }

        return pq.peek() >= K ? cnt : -1;  // 마지막 남은 음식의 스코빌 지수 확인
    }
}