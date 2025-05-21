// 풀이 시간: 37분
// 풀이 방법: 모든 route를 순회하며 step 별 로봇의 위치를 담고,
//         이후 step 별로 Map<위치, 로봇 개수>를 계산해 충돌 횟수를 누적한다.

import java.util.*;

class Solution {

    class Point {  // 좌표 클래스 (Hash 기반 자료구조 사용을 위해 equals랑 hashCode 오버라이딩함)
        int x, y;
        Point(int x, int y) { this.x = x; this.y = y; }
        @Override
        public boolean equals(Object obj) {
            if (this == obj) return true;
            if (!(obj instanceof Point)) return false;
            Point point = (Point) obj;
            return this.x == point.x && this.y == point.y;
        }
        @Override
        public int hashCode() {
            return 31 * x + y;
        }
    }

    public void addPointByStep(ArrayList<ArrayList<Point>> pointByStep, int step, Point point) {  // 동적으로 리스트 메모리 확장하며 리스트에 Point 추가
        if (pointByStep.size() < step) {
            pointByStep.get(step).add(point);
        } else {
            pointByStep.add(new ArrayList<>());
            pointByStep.get(step).add(point);
        }

    }

    public int solution(int[][] points, int[][] routes) {

        ArrayList<ArrayList<Point>> pointByStep = new ArrayList<>();  // Step 별 좌표들을 저장
        int result = 0;

        for (int[] route: routes) {  // routes 순회

            int step = 0, start = route[0];  // step은 0부터 시작
            int x = points[start - 1][0], y = points[start - 1][1];  // 시작 좌표
            addPointByStep(pointByStep, step++, new Point(x, y));  // 시작 좌표 추가

            for (int i = 1; i < route.length; i++) {  // 운송 경로에 따라 이동

                int toward = route[i];
                int nextX = points[toward - 1][0], nextY = points[toward - 1][1];

                while (x != nextX) {  // x 좌표 우선으로 조정
                    x += (x < nextX) ? 1 : -1;
                    addPointByStep(pointByStep, step++, new Point(x, y));  // 좌표 추가
                }
                while (y != nextY) {  // y 좌표 조정
                    y += (y < nextY) ? 1 : -1;
                    addPointByStep(pointByStep, step++, new Point(x, y));
                }
            }
        }

        for (ArrayList<Point> pointList: pointByStep) {  // step 별로 순회하며

            HashMap<Point, Integer> pointMap = new HashMap<>();  // HashMap에 Point 별 로봇 개수를 저장
            for (Point point: pointList)
                pointMap.put(point, pointMap.getOrDefault(point, 0) + 1);

            for (Map.Entry<Point, Integer> entry: pointMap.entrySet())
                if (entry.getValue() > 1)  // 1개 초과라면 충돌임!
                    result++;
        }

        return result;
    }
}