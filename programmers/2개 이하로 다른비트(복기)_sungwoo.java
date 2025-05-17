// 풀이 시간: 27분
// 풀이 방법: 가장 오른쪽 비트에 따라 간단한 비트 수정만 해주면 문제를 해결할 수 있다.
//         이전에는 제한사항으로 인해 쉽게 접근을 못했지만, 이번에는 규칙을 찾아내어 풀었다.

import java.util.*;

class Solution {

    public ArrayList<Integer> numberToBinary(long number) {  // 10진수 -> 2진수

        ArrayList<Integer> bitList = new ArrayList<>();

        while (number > 0) {
            bitList.add((int) (number % 2));
            number /= 2;
        }
        bitList.add(0);  // 추후 비트 수정을 위해 0을 추가해준다.

        Collections.reverse(bitList);  // 뒤집기!
        return bitList;
    }

    public long binaryToNumber(ArrayList<Integer> bitList) {  // 2진수 -> 10진수

        long number = 0;

        for (int i = 0; i < bitList.size(); i++)
            number += bitList.get(bitList.size() - (i + 1)) * Math.pow(2, i);

        return number;
    }

    public long[] solution(long[] numbers) {

        long[] answer = new long[numbers.length];

        for (int i = 0; i < numbers.length; i++) {

            ArrayList<Integer> bitList = numberToBinary(numbers[i]);  // 2진수로 변환

            if (bitList.get(bitList.size() - 1) == 0) {  // 맨 마지막 비트가 0이라면 1로 수정
                bitList.set(bitList.size() - 1, 1);
            } else {  // 맨 마지막 비트가 1이라면, 0을 만날 때까지 왼쪽으로 순회하며 해당 비트를 1로, 그 왼쪽 비트를 0으로 수정
                int j;
                for (j = bitList.size() - 1; j >= 0 && bitList.get(j) != 0; j--) { }

                bitList.set(j, 1);
                bitList.set(j + 1, 0);
            }

            answer[i] = binaryToNumber(bitList);
        }

        return answer;
    }
}