class Solution {
    public int solution(String name) {
        int answer = 0;
        int len = name.length();

        int index;
        int move = len;

        for(int i = 0; i < len; i++){
            answer += Math.min(name.charAt(i) - 'A', 'Z' - name.charAt(i) + 1);  // 상하 조작 횟수 누적

            // index는 현재 위치 i에서 시작하여, 연속된 'A' 구간의 끝을 찾기 위해 사용됩니다.
            // index가 문자열의 끝(len)에 도달하거나 'A'가 아닌 문자를 만나면 반복문을 종료합니다.
            index = i + 1;
            while(index < len && name.charAt(index) == 'A'){
                index++;
            }

            // move는 현재까지 구한 좌우 이동의 최소값을 유지합니다.
            // i * 2 + len - index는 첫 번째 위치에서 i까지 이동한 후 다시 돌아와 남은 부분을 탐색하는 경우의 이동 거리입니다.
            // (len - index) * 2 + i는 반대 방향으로 탐색하다가 다시 i까지 돌아오는 경우의 이동 거리입니다.
            // 두 가지 방식 중 최소 이동 횟수를 move에 갱신합니다.
            move = Math.min(move, i * 2 + len - index);
            move = Math.min(move, (len - index) * 2 + i);
        }

        // answer는 상하 이동 횟수의 총합이고, move는 최소 좌우 이동 횟수입니다. 이 둘을 합하여 최소 조이스틱 조작 횟수를 반환합니다.
        return answer + move;
    }
}