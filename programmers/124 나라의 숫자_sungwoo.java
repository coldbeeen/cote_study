// 풀이 시간: 21분

class Solution {
    public String solution(int n) {

        StringBuilder answer = new StringBuilder();  // 효율성을 위해 StringBuilder 사용
        n--;  // n을 1 감소시켜 시작

        while (n >= 0) {  // n이 0보다 크거나 같은 동안 진행

            answer.append((int) Math.pow(2, n % 3));  // 2 ^ (n % 3)를 계산하여 추가

            n /= 3;  // n을 3으로 나눈 몫으로 업데이트 후
            n--;  // 1 감소
        }

        return answer.reverse().toString();  // 순서를 반전시켜 리턴
    }
}