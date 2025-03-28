// 풀이 시간: 1시간 (30분 동안 배열로 시도 중, 수학 연산으로 전환해 30분 걸려 성공)

class Solution {

    public int numToX(int num, int w) {  // num과 w(가로)를 입력받아 x 좌표를 리턴
        return ((num - 1) / w) % 2 == 0 ? (num - 1) % w : w - ((num - 1) % w + 1);
    }

    public int numToHeight(int num, int w) {  // num과 w(가로)를 입력받아 높이를 리턴
        return (int) Math.ceil((double) num / w);
    }

    public int solution(int n, int w, int num) {

        int nHeight = numToHeight(n, w), numHeight = numToHeight(num, w);  // n과 num 박스의 높이
        int nX = numToX(n, w), numX = numToX(num, w), result;  // n과 num 박스의 x 좌표

        if (((n- 1) / w) % 2 == 0) {  // 맨 윗층 박스가 왼쪽에서 오른쪽으로 쌓이고
            if (nX >= numX)  // 맨 윗층 numX 위치에 박스가 있다면 1 더한 값으로 구함
                result = nHeight - numHeight + 1;
            else
                result = nHeight - numHeight;

        } else {  // 맨 윗층 박스가 오른쪽에서 왼쪽으로 쌓이고
            if (nX <= numX)  // 맨 윗층 numX 위치에 박스가 있다면 1 더한 값으로 구함
                result = nHeight - numHeight + 1;
            else
                result = nHeight - numHeight;
        }

        return result;
    }
}