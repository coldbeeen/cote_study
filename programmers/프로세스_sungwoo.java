// 풀이 시간: 55분

import java.util.*;

class Solution {

    class IdxPrt {  // 프로세스 번호와 우선순위를 함께 큐의 원소로 사용하기 위한 클래스
        int idx, prt;
        IdxPrt(int idx, int prt)  { this.idx = idx; this.prt = prt; }
    }

    public int solution(int[] priorities, int location) {

        ArrayList<Integer> priorityList = new ArrayList<>();  // List로 변환
        for (int prt: priorities)
            priorityList.add(prt);

        Queue<IdxPrt> idxPrtQueue = new LinkedList<>();  // 번호와 우선순위를 원소로 가지는 큐
        for (int i = 0; i < priorityList.size(); i++)
            idxPrtQueue.offer(new IdxPrt(i, priorityList.get(i)));

        Collections.sort(priorityList, Collections.reverseOrder());  // 역순 정렬 후 따로 큐로 관리 (Max 값을 효율적으로 가져오기 위함. O(n^2) -> O(n*logn))
        Queue<Integer> sortedPrtQueue = new LinkedList<Integer>(priorityList);


        int answer = 1;  // 실행 순번

        while (!idxPrtQueue.isEmpty()) {  // 큐가 빌 때까지

            if (idxPrtQueue.peek().prt < sortedPrtQueue.peek()) {  // 우선순위 첫 번째보다 작다면 다시 큐 뒤로!
                idxPrtQueue.offer(idxPrtQueue.poll());
                continue;
            }

            IdxPrt idxPrt = idxPrtQueue.poll();  // 프로세스 실행
            sortedPrtQueue.poll();

            if (idxPrt.idx == location)   // 실행한 프로세스가 location이라면 break
                break;

            answer++;
        }

        return answer;
    }
}