// 풀이 시간: 21분
// 풀이 방법: DFS 기반 백트래킹 적용하여 풀이함. 변환 가능 여부를 판단해가며 target까지의 경로를 탐색함.

import java.util.*;

class Solution {

    int minStep = Integer.MAX_VALUE;  // answer

    public boolean isConvertible(String a, String b) {  // a -> b 변환 가능 여부 리턴
        int diffCnt = 0;
        for (int i = 0; i < a.length(); i++) {
            if (a.charAt(i) != b.charAt(i)) {
                diffCnt++;
                if (diffCnt > 1)
                    return false;
            }
        }
        return true;
    }

    public void dfs(String current, String target, String[] words, boolean[] visited, int step) {  // DFS 재귀 함수

        if (step >= minStep)  // minStep 이상이면 더 이상 탐색 X
            return;

        if (current.equals(target)) {  // target에 도달했다면 minStep 갱신 (종료 조건)
            minStep = Math.min(minStep, step);
            return;
        }

        for (int i = 0; i < words.length; i++) {

            if (visited[i] || !isConvertible(current, words[i]))  // 해당 단어 방문(변환) 여부와 변환 가능 여부 고려
                continue;

            visited[i] = true;  // 방문 처리
            dfs(words[i], target, words, visited, step + 1);  // 재귀 호출
            visited[i] = false;  // 방문 처리 해제
        }
    }

    public int solution(String begin, String target, String[] words) {

        boolean[] visited = new boolean[words.length];  // 방문(변환) 여부 배열 생성
        dfs(begin, target, words, visited, 0);  // DFS 재귀 함수 호출

        return minStep != Integer.MAX_VALUE ? minStep : 0;  // minStep or 0
    }
}