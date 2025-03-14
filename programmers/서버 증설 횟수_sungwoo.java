// 풀이 시간: 25분

class Solution {

    public int solution(int[] players, int m, int k) {

        int[] servers = new int[players.length];
        int answer = 0;

        for (int i = 0; i < players.length; i++) {

            if (players[i] >= (servers[i] + 1) * m) {  // 증설이 필요하다면

                int increment  = (players[i] - (servers[i] * m)) / m;  // 증설해야 할 서버 수
                answer += increment;

                for (int j = i; j < players.length && j < i + k; j++)  // 인덱스 i부터 시작하여 k개의 서버 수 업데이트
                    servers[j] += increment;
            }
        }

        return answer;
    }
}