// 풀이 시간: 1시간

import java.util.*;

class Solution {
    public int solution(int n, int k, int[] enemy) {

        PriorityQueue<Integer> passHeap = new PriorityQueue<>();  // 우선순위 큐 활용

        for (int i = 0; i < k && i < enemy.length; i++)  // 처음 k라운드는 무적권을 사용하도록 하고 진행함
            passHeap.add(enemy[i]);
        int answer = Math.min(k, enemy.length);  // 건너뛴 라운드로 answer 초기화


        for (int i = k; i < enemy.length; i++) {  // k라운드부터 시작

            int minInPassSet = passHeap.peek();  // 우선순위 큐에서 최솟값을 가져옴 (무적권을 철회할지 결정하기 위함)
            int armyNum = enemy[i];  // 필요한 병사 수

            if (enemy[i] > minInPassSet) {  // 이번 라운드의 필요 병사 수가 더 많다면, 사용했던 무적권 철회 후 이번 라운드에서 무적권 사용
                passHeap.poll();
                passHeap.add(enemy[i]);
                armyNum = minInPassSet;  // 무적권을 철회한 라운드에서 필요한 병사 수를 가져옴
            }

            if (armyNum > n)  // 필요한 병사 수가 n보다 크다면 라운드 종료
                break;

            n -= armyNum;  // 병사 수 감소
            answer++;  // 라운드 증가
        }

        return answer;
    }
}