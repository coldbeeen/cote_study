import java.util.Arrays;

class Solution {
    int solution(int[][] land) {

        for (int i = 1; i < land.length; i++) {  // i - 1행의 최댓값을 선택해 아래로 누적해나감
            for (int j = 0; j < 4; j++) {

                int max = -1;  // 최댓값을 구함
                for (int k = 0; k < 4; k++)
                    if (land[i-1][k] > max && j != k)  // 같은 열은 제외
                        max = land[i-1][k];
                land[i][j] += max;  // 최댓값 누적
            }
        }

        return Arrays.stream(land[land.length-1]).max().getAsInt();
    }
}