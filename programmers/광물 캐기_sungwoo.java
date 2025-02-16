// 풀이 시간: 30분
// 풀이 방법: 최적의 곡괭이 사용 순서를 그리디하게 탐색하며 진행하는 것은 불가능하다고 판단하였고, 문제 조건 등을 고려해 완전 탐색을 통해 문제를 해결하고자 하였음. 가능한 모든 곡괭이 사용 순서의 경우의 수를 탐색하여 문제를 해결함.
// + 탐색 중 피로도가 최솟값을 넘는지 검사하여(백트래킹) 평균 300ms -> 1ms로 개선

import java.util.*;

class Solution {

    int minFatigue = Integer.MAX_VALUE;  // Answer

    public int getFatigue(String[] minerals, int mineralIdx, int gokType) {  // 피로도 계산 메서드 분리

        int fatigue = 0;

        for (int i = mineralIdx; i < minerals.length && i < mineralIdx + 5; i++) {
            if (minerals[i].equals("diamond")) {
                if (gokType == 0)  fatigue += 1;
                else if (gokType == 1)  fatigue += 5;
                else if (gokType == 2)  fatigue += 25;
            }
            else if (minerals[i].equals("iron")) {
                if (gokType == 0)  fatigue += 1;
                else if (gokType == 1)  fatigue += 1;
                else if (gokType == 2)  fatigue += 5;
            }
            else if (minerals[i].equals("stone")) {
                if (gokType == 0)  fatigue += 1;
                else if (gokType == 1)  fatigue += 1;
                else if (gokType == 2)  fatigue += 1;
            }
        }

        return fatigue;
    }

    public void completeSearch(int[] picks, String[] minerals, int mineralIdx, int curFatigue) {  // 완전 탐색 재귀 함수 (현재 미네랄 인덱스, 현재 피로도를 매개변수로 가짐)

        if (Arrays.stream(picks).sum() == 0) {  // 모든 곡괭이 사용 시, 최솟값 갱신 후 재귀 종료
            minFatigue = Math.min(minFatigue, curFatigue);
            return;
        }

        for (int i = 0; i < 3; i++) {  // 곡괭이 종류별로 사용

            if (picks[i] == 0)  // 개수 소진한 곡괭이 건너 뜀
                continue;

            int nextMineralIdx = Math.min(mineralIdx + 5, minerals.length);  // 다음 미네랄 위치
            int nextFatigue = curFatigue + getFatigue(minerals, mineralIdx, i);  // 해당 곡괭이(i) 사용 시 다음 피로도

            if(nextFatigue >= minFatigue)  // 피로도 최솟값 이상이라면 탐색하지 않음 (백트래킹)
                continue;

            picks[i]--;  // 곡괭이 수 갱신
            completeSearch(picks, minerals, nextMineralIdx, nextFatigue);  // 재귀 호출
            picks[i]++;  // 곡괭이 수 복구
        }
    }

    public int solution(int[] picks, String[] minerals) {

        completeSearch(picks, minerals, 0, 0);
        return minFatigue;
    }
}
