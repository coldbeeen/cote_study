// 풀이 시간: 15분
// 풀이 방법: 제한 사항을 확인하고 시간복잡도 O(n)을 만족하기 위한 방법을 생각해보았다.
//         뒷 큰수가 구해지지 않은 원소를 스택에 관리한다.
//         순차적으로 '원소'를 확인하면서 '다음 원소'가 더 크다면 해당 '원소'의 result 값을 갱신함과 동시에
//         스택을 순회하며 '다음 원소'보다 작다는 조건이 만족하는 동안 result 값을 갱신한다.
//         이렇게 하면 선형 시간으로 풀어낼 수 있다.

import java.util.*;

class Solution {

    class IndexValue {  // 인덱스와 값을 담을 클래스
        int index, value;
        IndexValue(int index, int value) { this.index = index; this.value = value; }
    }

    public int[] solution(int[] numbers) {

        Stack<IndexValue> stack = new Stack<>();  // 스택 생성
        int[] result = new int[numbers.length];  // 결과 배열 생성

        for (int i = 0; i < numbers.length - 1; i++) {

            if (numbers[i] < numbers[i + 1]) {  // '다음 원소'가 더 크다면

                result[i] = numbers[i + 1];  // 이번 원소에 대해 result 값 갱신 후

                // 이어서 스택 순회하며 result 값 추가로 갱신 ('다음 원소'보다 작은 동안)
                while (!stack.isEmpty() && stack.peek().value < numbers[i + 1]) {
                    IndexValue iv = stack.pop();
                    result[iv.index] = numbers[i + 1];
                }

            } else {  // '다음 원소'보다 크지 않다면 스택에 임의로 넣어둠

                stack.push(new IndexValue(i, numbers[i]));
            }
        }

        while(!stack.isEmpty()) {  // 스택에 남은 원소들에 대해 result 값 -1로 갱신
            IndexValue iv = stack.pop();
            result[iv.index] = -1;
        }
        result[result.length - 1] = -1;  // 마지막 result 값은 -1

        return result;
    }
}