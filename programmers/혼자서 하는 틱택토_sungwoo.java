// 풀이 시간: 35분
// 풀이 방법:
// 1. 빙고가 있다면 O 또는 X의 빙고여야 함
// 2. O의 빙고인 경우, X 개수보다 1 큰지
// 3. X의 빙고인 경우, O의 개수와 같은지
// 4. 빙고가 없다면, O의 개수가 X보다 1 크거나 같은지

class Solution {

    public boolean checkBingo(String[] board, char target) {  // target 모양이 빙고라면 1, 아니라면 0

        int targetCnt;

        for (int i = 0; i < 3; i++) {  // 가로 빙고 검사
            targetCnt = 0;
            for (int j = 0; j < 3; j++)
                if (board[i].charAt(j) == target)
                    targetCnt++;

            if (targetCnt == 3)  // 빙고!
                return true;
        }

        for (int j = 0; j < 3; j++) {  // 세로 빙고 검사
            targetCnt = 0;
            for (int i = 0; i < 3; i++)
                if (board[i].charAt(j) == target)
                    targetCnt++;

            if (targetCnt == 3)  // 빙고!
                return true;
        }

        targetCnt = 0;
        for (int i = 0; i < 3; i++)  // 대각선 (\)
            if (board[i].charAt(i) == target)
                targetCnt++;

        if (targetCnt == 3)  // 빙고!
            return true;

        targetCnt = 0;
        for (int i = 0; i < 3; i++)  // 대각선 (/)
            if (board[2 - i].charAt(i) == target)
                targetCnt++;

        if (targetCnt == 3)  // 빙고!
            return true;

        return false;
    }

    public int countTarget(String[] board, char target) {  // target 모양의 개수를 카운트함

        int cnt = 0;

        for (int i = 0; i < 3; i++)
            for (int j = 0; j < 3; j++)
                if (board[i].charAt(j) == target)
                    cnt++;

        return cnt;
    }

    public int solution(String[] board) {

        boolean OBingo = checkBingo(board, 'O');  // O, X의 빙고 체크
        boolean XBingo = checkBingo(board, 'X');

        if (OBingo && XBingo)  // 둘 다 빙고라면 0 리턴
            return 0;

        int OCount = countTarget(board, 'O');  // O, X의 모양 개수 카운트
        int XCount = countTarget(board, 'X');

        if (OBingo) {
            if (OCount == XCount + 1)  // O의 빙고이며, O의 개수가 X보다 1개 많다면 정상
                return 1;
        } else if (XBingo) {  // X의 빙고이며, X의 개수가 O와 같다면 정상
            if (OCount == XCount)
                return 1;
        } else {
            if (OCount == XCount || OCount == XCount + 1)  // 빙고가 없으나, O의 개수가 X보다 1 크거나 같다면 정상
                return 1;
        }

        return 0;
    }
}