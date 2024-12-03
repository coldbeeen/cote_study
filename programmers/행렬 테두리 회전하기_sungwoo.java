// 풀이 시간: 46분

import java.util.*;

class Solution {

    public int rotateAndReturnMin(int[][] table, int r1, int c1, int r2, int c2) {  // 입력 받은 범위의 회전을 수행하며, 회전된 숫자 중 가장 작은 숫자를 리턴하는 함수

        int[] dr = {1, 0, -1, 0};  // 하, 우, 상, 좌 순서의 좌표 변화량
        int[] dc = {0, 1, 0, -1};
        int r = r1, c = c1, di = 0, tmp = table[r1][c1], min = tmp;  // r, c 초깃값 및 min 설정

        while (true) {

            if (r == r1 && c == c1 + 1) {  // 종료 조건 (마지막 요소 대입 시점)
                table[r][c] = tmp;
                break;
            }

            if ((r == r2 && c == c1) ||  // 각 꼭짓점 좌표에서 di를 증가하여 좌표 변화량을 수정
                    (r == r2 && c == c2) ||
                    (r == r1 && c == c2))
                di++;

            int nextR = r + dr[di];  // 다음 요소의 좌표
            int nextC = c + dc[di];

            table[r][c] = table[nextR][nextC];  // 다음 요소를 덮어씌움
            min = Math.min(table[r][c], min);  // min 값 갱신

            r = nextR;  // 좌표 갱신
            c = nextC;  // 좌표 갱신
        }

        return min;
    }


    public int[] solution(int rows, int columns, int[][] queries) {

        int[][] table = new int[rows][columns];  // 행렬(2차원 배열) 생성

        for (int i = 0, cnt = 1; i < rows; i++)  // 숫자 입력
            for (int j = 0; j < columns; j++)
                table[i][j] = cnt++;


        ArrayList<Integer> answer = new ArrayList<>();  // 정답 리스트 생성

        for (int[] query: queries) {  // 모든 쿼리 순회
            int r1 = query[0] - 1, c1 = query[1] - 1, r2 = query[2] - 1, c2 = query[3] - 1;
            int minValue = rotateAndReturnMin(table, r1, c1, r2, c2);  // 회전 및 최솟값을 저장
            answer.add(minValue);
        }

        return answer.stream().mapToInt(i -> i).toArray();  // 정답 리스트를 배열로 변환하여 리턴
    }
}