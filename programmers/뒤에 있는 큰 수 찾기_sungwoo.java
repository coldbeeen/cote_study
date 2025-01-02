// 풀이 시간: 1시간 이상... (가장 중요한 인사이트를 찾아 놓고 스택 활용하지 못하고 헤맸음)

import java.util.*;

class Solution {
    public int[] solution(int[] numbers) {
        int[] answer = Arrays.stream(new int[numbers.length]).map(i -> -1).toArray();  // -1로 채워 넣음
        Stack<Integer> stack = new Stack<>();  // 스택 활용

        for (int i = 0; i < numbers.length - 1; i++) {

            stack.push(i);  // i를 우선 스택에 삽입

            if (numbers[i] >= numbers[i + 1])  // 다음 원소보다 같거나 큰 경우는 건너뜀
                continue;

            while (!stack.isEmpty()) {  // 다음 원소보다 작은 경우, 가장 최근 삽입된 원소부터 순회함
                int idx = stack.peek();  // 인덱스를 가져온 후
                if (numbers[idx] >= numbers[i + 1])  // i+1의 원소보다 같거나 큰 원소가 나오기 전까지 반복함 (이 경우엔 더 이상 볼 필요가 없음!!! -> 그 앞에는 아직 뒷 큰수를 구하지 못한 더 큰 원소들이 있을 것이기 때문)
                    break;

                answer[stack.pop()] = numbers[i + 1];  // 최근 삽입된 원소를 pop하면서 answer에 i+1 원소를 저장
            }
        }

        return answer;
    }
}