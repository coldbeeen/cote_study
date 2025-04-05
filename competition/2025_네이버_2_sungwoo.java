// 풀이 시간: 50분
// 풀이 방법: 문제의 제약 조건이 명시되지 않은 관계로 타임 테이블 활용 vs Map 활용 중에 고민하다가 좀 더 직관적인 Map을 활용하기로 결정했다.
//         HashMap을 활용해 "Key: 유저 ID, Value: [최초 접속 시간, 최근 접속 시간]" 형태로 접속 중인 유저를 관리하여 문제를 해결하였다.
//         하나의 request를 처리할 때 마다 autoDisconnect 메서드를 통해 b초가 지난 유저를 접속 해제시키며,
//         접속 중인 유저 수가 n보다 크거나 같을 때는 자리 비움 유저를 접속 해제시킨다.

import java.util.*;

class Main {

    public static void autoDisconnect(HashMap<Integer, List<Integer>> accessMap, int b, int curTime) {  // 최초 접속 시간으로부터 b초가 지난 유저 접속 해제

        HashSet<Integer> removeIdList = new HashSet<>();

        for (Map.Entry<Integer, List<Integer>> entry : accessMap.entrySet()) {  // 현재 시간 - 최초 접속 시간이 b보다 크거나 같은 유저를 찾음
            int id = entry.getKey(), firstAccessTime = entry.getValue().get(0);
            if (curTime - firstAccessTime >= b)
                removeIdList.add(id);
        }

        for (int removeId: removeIdList) {  // accessMap에서 해당 유저 삭제
            accessMap.remove(removeId);
        }
    }

    public static int absenceDisconnect(HashMap<Integer, List<Integer>> accessMap, int a, int curTime) {  // 마지막 접속 시간으로부터 b초가 지난 유저 접속 ID 리턴 (자리비움 없다면 -1 리턴)

        int maxAbsenceUserId = -1, maxAbsenceTime = -1;

        for (Map.Entry<Integer, List<Integer>> entry : accessMap.entrySet()) {  // 현재 시간 - 마지막 접속 시간이 a보다 크거나 같으며, 그 자리비움 시간이 가장 큰 유저를 찾음

            int id = entry.getKey(), lastAccessTime = entry.getValue().get(1);

            if (curTime - lastAccessTime >= a && curTime - lastAccessTime > maxAbsenceTime) {
                maxAbsenceUserId = id;
                maxAbsenceTime = curTime - lastAccessTime;
            }
        }

        return maxAbsenceUserId;
    }

    public static List<Integer> solution(int n, int a, int b, int[][] requests) {

        ArrayList<Integer> answer = new ArrayList<>();
        HashMap<Integer, List<Integer>> accessMap = new HashMap<>();  // Key: 유저 ID, Value: [최초 접속 시간, 최근 접속 시간]

        for (int[] request: requests) {  // request 순회

            int time = request[0], id = request[1];

            autoDisconnect(accessMap, b, time);  // 자동 접속 해제 (최초 접속으로부터 b초 지난 유저)

            if (accessMap.size() < n) {  // 바로 접속 가능한 조건

                if (accessMap.containsKey(id))  // 이미 접속 중 -> 마지막 접속 시간 업데이트
                    accessMap.get(id).set(1, time);
                else  // 접속 중이 아님 -> 새로 삽입
                    accessMap.put(id, new ArrayList<>(List.of(time, time)));

            } else {  // 접속 중인 유저가 n명인 경우

                if (accessMap.containsKey(id)) {  // 이미 접속 중인 유저라면 마지막 접속 시간만 업데이트
                    accessMap.get(id).set(1, time);
                } else {  // 아니라면 자리비움 유저를 찾음
                    int maxAbsenceUserId = absenceDisconnect(accessMap, a, time);  // 가장 오래 자리 비운 유저 탐색

                    if (maxAbsenceUserId == -1) {  // 못 찾은 경우
                        answer.add(-1);
                        continue;
                    } else {  // 찾은 경우 해당 유저 삭제 후 새로운 유저 접속
                        accessMap.remove(maxAbsenceUserId);
                        accessMap.put(id, new ArrayList<>(List.of(time, time)));
                    }
                }
            }
            answer.add(accessMap.size());
        }

        return answer;
    }

    public static void main(String[] args) {

        System.out.println(solution(5, 100, 200, new int[][] {{11, 1}, {12, 2}, {13, 1}, {16, 3}, {200, 1}, {214, 1}, {216, 1}}));
        System.out.println(solution(2, 10, 100, new int[][] {{2, 1000}, {3, 1001}, {4, 1005}, {8, 1000}, {12, 1002}, {13, 1002}, {14, 1001}, {200, 1301}}));
    }
}