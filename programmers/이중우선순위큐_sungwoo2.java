// 1번 풀이는 sort를 여러 번 사용한다는 점 때문에 찝찝하여 더 나은 풀이를 찾아보았다.
// 자바 다른 풀이의 경우, 최대힙과 최소힙을 이용하는 풀이가 다수 존재하여 시도하였으나,
// remove() 메서드가 O(n)의 시간복잡도를 가지므로 의미가 없었다.

// 가장 처음에 문제를 보고 TreeSet 사용하면 금방 풀릴 문제라고 생각했으나 중복을 허용하지 않는다는 점 때문에 TreeSet 사용하지 못했다.
// 그러나, 파이썬 풀이 맨 위에 있는 풀이가 중복을 허용하는 Tree를 활용한 풀이로서, 가장 정석 풀이라고 생각된다. (최대/최소 탐색 및 삭제가 O(logn)이기 때문)

import java.util.*;

class Solution {
    public int[] solution(String[] operations) {

        PriorityQueue<Integer> pqAsc = new PriorityQueue<>();  // 최소힙
        PriorityQueue<Integer> pqDesc = new PriorityQueue<>(Collections.reverseOrder());  // 최대힙

        for (String operation: operations) {

            char o = operation.charAt(0);  // 명령어
            Integer n = Integer.parseInt(operation.substring(2));  // 숫자

            if (o == 'I') {  // I: 삽입 -> 양 큐의 삽입
                pqAsc.offer(n);
                pqDesc.offer(n);
            } else {  // D: 삭제
                if (pqAsc.isEmpty())  // 하나의 큐가 비었다면 명령어 무시
                    continue;

                if (n == -1) { // 최솟값 삭제
                    int tmp = pqAsc.poll();
                    pqDesc.remove(tmp);  // 삭제된 값을 최대힙에서 삭제
                }
                else { // 최댓값 삭제
                    int tmp = pqDesc.poll();
                    pqAsc.remove(tmp);  // 삭제된 값을 최소힙에서 삭제
                }
            }
        }

        if (pqAsc.isEmpty())  // 비어있으면 [0,0] 리턴
            return new int[]{0, 0};

        return new int[]{pqDesc.poll(), pqAsc.poll()};  // [최댓값, 최솟값] 리턴
    }
}