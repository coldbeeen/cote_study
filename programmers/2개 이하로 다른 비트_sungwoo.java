// 풀이 시간: 30분 시도 후, 레퍼런스 참고하여 해결했습니다.

import java.util.*;

class Solution {

    public ArrayList<Integer> DecToBinary(long n) {  // 10진수 -> 2진수

        ArrayList<Integer> binaryList = new ArrayList<>();

        while (n > 0) {
            binaryList.add(Long.valueOf(n % 2).intValue());
            n /= 2;
        }

        binaryList.add(0);  // 비트 수정의 편의를 위해 리턴할 binaryList 맨 앞에 0을 추가
        Collections.reverse(binaryList);
        return binaryList;
    }

    public long binaryToDec(ArrayList<Integer> binaryList) {  // 2진수 -> 10진수

        long n = 0, i = 1;
        Collections.reverse(binaryList);

        for (int bit: binaryList) {
            n += bit * i;
            i *= 2;
        }

        return n;
    }

    public long[] solution(long[] numbers) {

        ArrayList<Long> answer = new ArrayList<>();

        for (long n: numbers) {

            if (n % 2 == 0) {  // 짝수의 경우, n + 1
                answer.add(n + 1);
            } else {  // 홀수의 경우, 2진수의 가장 오른쪽 0을 1로 수정한 뒤, 바로 오른쪽 비트를 0으로 수정
                ArrayList<Integer> binaryList = DecToBinary(n);

                for (int i = binaryList.size() - 1; i >= 0; i--) {
                    if (binaryList.get(i).equals(0)) {  // 가장 오른쪽 0을 찾아서 비트 수정
                        binaryList.set(i, 1);
                        binaryList.set(i + 1, 0);
                        break;
                    }
                }

                answer.add(binaryToDec(binaryList));  // 10진수로 변환
            }
        }

        return answer.stream().mapToLong(i -> i).toArray();
    }
}