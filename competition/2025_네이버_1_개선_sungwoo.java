// 슬라이딩 윈도우 적용한 풀이
// 풀이 방법: 구간 합을 구한 뒤 해당 구간을 한 칸씩 이동하며 구간 합을 갱신하였다. (슬라이딩 윈도우)
//         구간 합은 총알이 발사된 횟수를 의미하므로 구간 합이 0인지를 검사하면 a번 동안 총알이 발사되었는지 여부를 알 수 있다.
//         결과적으로 n과 a가 유사한 값이라면 최악의 경우 O(n^2)지만 슬라이딩 윈도우로 개선함에 따라 O(N) 시간복잡도를 갖게 되었다.
//         (이전 풀이는 직관적인 풀이였으나, 최악의 입력 조건을 생각해보게 되어 이번 풀이를 떠올릴 수 있었다.)

import java.util.*;

class Main {

    public static List<Integer> solution(List<Integer> cylinder, int a) {

        int N = cylinder.size();  // 실린더 크기
        int notShootCnt = 0, tryCnt = 0;  // 총알이 발사되지 않은 횟수(분자), 발사 시도 횟수(분모)
        int intervalSum = 0;  // 구간 합 (총알이 발사된 횟수)

        for (int i = 0; i < a; i++)  // 최초의 구간 합을 구하여 이후 구간을 한 칸씩 이동할 것임 (슬라이딩 윈도우)
            intervalSum += cylinder.get(i);

        for (int i = 0; i < N; i++) {
            intervalSum += cylinder.get((i + a) % N) - cylinder.get(i);  // 현재 구간에서 i+a번 실린더 값을 더하고 i번 실린더 값을 빼서 구간 이동

            if (cylinder.get(i) == 0) {  // 총알이 발사되지 않은 실린더인 경우
                if (intervalSum == 0)  // 해당 실린더 이후, a번 동안 한 번도 총알이 발사되지 않았다면 cnt 증가
                    notShootCnt++;
                tryCnt++;
            }
        }

        for (int i = notShootCnt; i > 1; i--) {  // 기약 분수로 변환
            if (notShootCnt % i == 0 && tryCnt % i == 0) {
                notShootCnt /= i;
                tryCnt /= i;
            }
        }

        return new ArrayList<>(List.of(notShootCnt, notShootCnt == 0 ? 1 : tryCnt));
    }

    public static void main(String[] args) {

        System.out.println(solution(new ArrayList<>(List.of(1, 1, 0, 0, 0, 0)), 2));
        System.out.println(solution(new ArrayList<>(List.of(1, 0, 0, 0, 0, 1)), 2));
        System.out.println(solution(new ArrayList<>(List.of(0, 0, 0, 0, 0, 0)), 1));
        System.out.println(solution(new ArrayList<>(List.of(1, 0, 1, 0, 1, 0)), 1));
        System.out.println(solution(new ArrayList<>(List.of(0, 0, 0, 0, 0, 0, 0, 0, 1)), 4));
    }
}
