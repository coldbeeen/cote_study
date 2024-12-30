// 풀이 시간: 1시간 이상

class Solution {
    public int[] solution(int[] sequence, int k) {

        int[] ans = {0, Integer.MAX_VALUE};
        int sum = 0, end = 0;  // sum: 부분합, end: 부분 수열의 마지막 인덱스

        for (int start = 0; start < sequence.length; start++) {

            while (sum < k && end < sequence.length)  // 부분합이 k보다 작은 동안 end를 증가시키며 누적합 계산
                sum += sequence[end++];

            if ((sum == k) && (end - start - 1 < ans[1] - ans[0])) {  // 부분합이 k이고, 수열 길이가 더 짧다면 ans 갱신
                ans[0] = start;  ans[1] = end - 1;
            }
            sum -= sequence[start];  // 위에서 구한 부분합을 활용하기 위해 start 인덱스의 값만 빼고 활용 (end 또한 초기화하지 않고 그대로 사용)
        }

        return ans;
    }
}