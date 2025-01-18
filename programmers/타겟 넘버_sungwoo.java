// 풀이 시간: 6분

class Solution {

    int answer = 0;  // target을 만드는 방법의 수

    // 깊이 우선 탐색 메서드 - target을 만드는 방법의 수를 탐색함 (idx: 현재 인덱스, sum: 현재까지의 합)
    public void dfs(int[] numbers, int idx, int sum, int target) {

        if (idx == numbers.length) {  // 종료 조건 (모든 인덱스를 다 보았다면 종료)
            if (sum == target)   // target과 일치한다면 방법의 수 증가
                answer++;

            return;
        }

        dfs(numbers, idx + 1, sum + numbers[idx], target);  // idx번째 인덱스 숫자 더하기
        dfs(numbers, idx + 1, sum - numbers[idx], target);  // idx번째 인덱스 숫자 빼기
    }

    public int solution(int[] numbers, int target) {

        dfs(numbers, 0, 0, target);  // dfs 메서드 호출
        return answer;
    }
}