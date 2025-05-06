// 풀이 시간: 45분 (레퍼런스 참고함)
// 풀이 방법:
// (수학자 빙의해서 공식 깔끔하게 도출하려 했으나 실패해서 레퍼런스 참고해 이해한 내용을 바탕으로 서술하겠음)
// 가로 w', 세로 h'(w'과 h'는 서로소)인 사각형에서 대각선을 그었을 때,
// 대각선이 만나는 변은, 가로변 h' - 1개, 세로변 w' - 1개이다.
// 만나는 변의 개수 + 1을 해야 사각형의 개수가 나오므로
// (w' - 1) + (h' - 1) + 1 = w' + h' - 1이 나온다.

class Solution {

    int gcd(int a, int b) {
        if (a % b == 0) return b;
        return gcd(b, a % b);
    }

    public long solution(int w, int h) {

        int gcdOfWAndH = gcd(w, h);
        int dividedW = w / gcdOfWAndH, dividedH = h / gcdOfWAndH;
        return (long) w * h - ((dividedW - 1) + (dividedH - 1) + 1) * gcdOfWAndH;
    }
}