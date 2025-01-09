// 풀이 시간: 43분 + 코드 리팩터링 10분

class Solution {

    int answer = Integer.MAX_VALUE;

    public void search(int storey, int nDigit, int cnt) {  // 완전 탐색 재귀 함수

        if (storey / (int) Math.pow(10, nDigit - 1) == 0) {  // (종료 조건) 모든 자릿수를 다 고려했다면
            answer = Math.min(answer, cnt);   // 더 작은 값을 answer로 갱신
            return;
        }

        int digit = storey / (int) Math.pow(10, nDigit - 1) % 10;  // nDigit 자릿수의 숫자

        if (digit >= 5) {  // 불필요한 탐색을 없앰. 4 이하의 숫자에는 더할 필요 없음. -1 네 번, +10 한 번이 +1 여섯 번보다 항상 효율적
            int addCnt = 10 - digit;  // 더해야 할 횟수
            int newStorey = storey + (int) Math.pow(10, nDigit - 1) * addCnt;  // 더한 후의 층수
            search(newStorey, nDigit + 1, cnt + addCnt);  // 재귀
        }
        if (digit <= 5) {  // 마찬가지로 6 이상의 숫자에는 뺄 필요 없음. +1 네 번, -10 한 번이 -1 여섯 번보다 항상 효율적)
            int subCnt = digit;  // 빼야 할 횟수
            int newStorey = storey - (int) Math.pow(10, nDigit - 1) * subCnt;  // 뺀 후의 층수
            search(newStorey, nDigit + 1, cnt + subCnt);  // 재귀
        }
    }

    public int solution(int storey) {

        search(storey, 1, 0);
        return answer;
    }
}