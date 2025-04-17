// 풀이 시간: 27분
// 풀이 방법: 원소가 0인 인덱스의 다음 인덱스부터 a번 만큼 검사하여 한발도 발사되지 않는 경우의 수를 계산한다. 이후 기약분수로 변환한다.
// 풀고 난 후: 두 포인터로 O(n)으로 개선할 수 있겠다는 생각이 들었다.
//          처음에는 총알이 없는 부분만 골라서 a번 만큼 반복하는 것이 효율적이라고 생각했으나
//          총알이 대부분 비어있고 실린더의 크기 및 a 값이 크다면 최악의 경우 O(n^2)이 될 것이다.

import java.util.*;

class Main {

    public static List<Integer> solution(List<Integer> cylinder, int a) {

        int N = cylinder.size();  // 실린더 크기
        int notShootCnt = 0, tryCnt = 0;  // 총알이 발사되지 않은 횟수(분자), 발사 시도 횟수(분모)

        for (int i = 0; i < N; i++) {
            if (cylinder.get(i) == 0) {  // 총알이 비어있는 곳을 찾았다면

                int trigerIdx = i + 1;  // i + 1번 인덱스부터
                boolean notShoot = true;

                for (int j = 0; j < a; j++, trigerIdx++) {  // a개의 실린더를 순회함
                    if (cylinder.get(trigerIdx % N) == 1) {  // 총알이 있는 경우 break
                        notShoot = false;
                        break;
                    }
                }

                if (notShoot)  // 한 번도 총알이 발사되지 않았다면 cnt 증가
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