// 풀이 시간: 45분

class Solution {
    public long solution(int[] weights) {

        int[] numOfWeight = new int[1001];  // 몸무게에 해당하는 사람의 수를 저장하기 위한 배열

        for (int i = 0; i < weights.length; i++)
            numOfWeight[weights[i]]++;

        long answer = 0;

        for (int weight = 100; weight <= 1000; weight++) {  // 모든 몸무게에 대해 짝꿍을 탐색

            if (numOfWeight[weight] == 0)  // 해당 몸무게의 사람이 존재하지 않는 경우 건너 뜀
                continue;

            int num = numOfWeight[weight];  // 해당 몸무게의 사람 수
            long pairCnt = 0;  // 짝꿍 수

            for (int dist = 2; dist <= 4; dist++) {  // 나의 거리 dist
                for (int oppositeDist = 2; oppositeDist <= 4; oppositeDist++) {  // 상대의 거리 oppositeDist

                    if ((dist * weight) % oppositeDist != 0)  // (반례 해결 Point!) oppositeDist로 나누어 떨어지지 않는 경우 (딱 떨어지는 상대 몸무게가 계산되지 않는 경우)
                        continue;

                    int oppositeWeight = (dist * weight) / oppositeDist;  // 상대 몸무게 계산
                    if (oppositeWeight >= 100 && oppositeWeight <= 1000 && numOfWeight[oppositeWeight] > 0)  // 유효한 몸무게이며, 해당 몸무게를 가진 사람이 1명 이상인 경우
                        pairCnt += (weight == oppositeWeight) ? numOfWeight[oppositeWeight] - 1 : numOfWeight[oppositeWeight];  // 짝꿍 수 누적 (서로 같은 몸무게인 경우 자신이 포함되므로 1을 빼줌)
                }
            }

            if (num > 1) {  // 동일한 몸무게가 1명 이상인 경우
                pairCnt -= (2 * (num - 1));  // 동일한 몸무게 짝꿍에 대해서는 거리별로 모두 카운팅되므로 해당 값(2배)만큼 빼줌
                pairCnt *= num;  // 추후 answer에서 중복된 짝꿍 카운팅으로 인해 2로 나누어주므로, 동일한 몸무게 짝꿍에 대해 강제로 중복 카운팅 되도록 num만큼 곱해줌 (100(1) <-> 100(2), 100(2) <-> 100(1) 로 2번 카운팅되도록 적용))
            }
            answer += pairCnt;  // 짝꿍 수 누적
        }

        return answer / 2;  // 180 <-> 270, 270 <-> 180과 같은 중복된 짝꿍 카운팅이 있으므로 2로 나누어 최종 결과 리턴
    }
}