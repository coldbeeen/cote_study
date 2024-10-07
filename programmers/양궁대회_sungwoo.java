import java.util.Arrays;

class Solution {

    int[] base;  // 어피치의 점수
    int[] answer = null;  // 정답이 되는 경우의 수
    int answerScoreDiff = 0;  // 정답의 점수 차

    public void search(int[] info, int step, int remaining){  // 어피치의 각 과녁 점수를 넘기는 점수를 쏘거나 안쏘거나의 경우의 수를 완전 탐색 (2^11)

        if(step == 11){  // 경우의 수를 완성한 경우 점수 차를 계산
            int scoreA = 0, scoreL = 0;

            for (int i = 0; i < 11; i++) {
                if(info[i] != 0 || base[i] != 0) {  // 한 쪽이라도 점수를 낸 경우, 점수를 계산
                    if (info[i] > base[i])
                        scoreL += 10 - i;
                    else
                        scoreA += 10 - i;
                }
            }
            int scoreDiff = scoreL - scoreA;

            if(scoreDiff > answerScoreDiff) {  // 점수 차가 기존 점수 차보다 높은 경우, 업데이트
                answer = info;
                answerScoreDiff = scoreDiff;
            }
            if(scoreDiff == answerScoreDiff && answer != null) {  // 점수 차가 동일한 경우, 더 낮은 점수에 맞춘 경우의 수로 업데이트
                boolean flag = true;

                if(answer != null){
                    for (int i = info.length - 1; i >= 0; i--) {  // 뒤에서부터, 한 쪽이라도 점수를 낸 경우의 answer[i]와 info[i]의 값으로 업데이트 여부 판단
                        if (info[i] != 0 || answer[i] != 0) {
                            if (answer[i] != 0)
                                flag = false;
                            break;
                        }
                    }
                }

                if(flag) {  // 업데이트
                    answer = info;
                    answerScoreDiff = scoreDiff;
                }
            }
            return;
        }

        // 점수를 넘기는 화살을 쏘거나, 안 쏘거나의 경우의 수를 위해 2개의 배열 생성
        int[] newInfo1 = info.clone();
        int[] newInfo2 = info.clone();

        int toShoot = step < 10 ? base[step] + 1 : remaining;  // 쏴야할 화살의 개수
        newInfo1[step] = step < 10 ? toShoot : remaining;  // 쏘는 경우
        newInfo2[step] = 0;  // 안 쏘는 경우

        if(remaining >= toShoot) {  // 남은 화살의 개수가 여유있다면 쏘는 경우의 수로 재귀 탐색
            search(newInfo1, step + 1, remaining - toShoot);
        }
        search(newInfo2, step + 1, remaining);  // 안 쏘는 경우의 수로 재귀 탐색

    }


    public int[] solution(int n, int[] info) {
        base = info;  // base에 저장
        search(new int[11], 0, n);  // 탐색 시작

        return answer != null ? answer : new int[]{-1};  // 결과 리턴
    }
}