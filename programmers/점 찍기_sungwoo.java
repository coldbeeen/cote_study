// 풀이 시간: 44분
// 풀이 방법:
// 이중 반복문은 시간 초과를 초래하므로, 원의 가장자리를 따라 조건을 충족하는 점의 개수를 세는 방법으로 접근하였다.
// 1번 예시로 예를 들면,
// (4, 0) O
// (4, 2) X  -> x가 4일 때, (4, 0) 총 1개 가능
// (2, 2) O
// (2, 4) X  -> x가 2일 때, (2, 0), (2, 2) 총 2개 가능
// (0, 4) O  -> x가 0일 때, (0, 0), (0, 2), (0, 3) 총 3개 가능
// => 총 6개
// 이중 반복문이지만, x가 감소하면서 y가 증가하므로 O(n)이다. 투 포인터 풀이라고도 볼 수 있겠다.

class Solution {

    public double helloPythagoras(int x, int y) {  // 유클리드 거리를 구함
        return Math.sqrt((long) x * x + (long) y * y);
    }

    public long solution(int k, int d) {
        long answer = 0;
        int x, y;

        for (x = (d / k) * k, y = 0; x >= 0; x -= k) {  // x는 d에 근접한 k의 배수부터, y는 0부터
            while (helloPythagoras(x, y) <= d)  // 유클리드 거리가 d 이하라면 y를 k만큼 증가시킴 (x를 고정시켜 놓고, y가 가능한 범위까지 증가되는 방식임)
                y += k;

            answer += (y / k);  // 0 ~ y까지 가능한 점의 개수를 y / k로 구해 누적함
        }

        return answer;
    }
}