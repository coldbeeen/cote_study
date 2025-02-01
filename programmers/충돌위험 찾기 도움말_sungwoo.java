import java.util.*;

class Point {  // 좌표 클래스
    private final int x, y;

    public Point(int x, int y) {
        this.x = x;  this.y = y;
    }

    @Override
    public boolean equals(Object obj) {  // Point 객체의 동등성 비교 재정의
        if (this == obj) return true;
        if (!(obj instanceof Point)) return false;
        Point other = (Point) obj;
        return x == other.x && y == other.y;
    }

    @Override
    public int hashCode() { return 31 * x + y; }  // equals가 같다면 hashCode도 같아야 함
    // 해시 기반 컬렉션에서 예상치 못한 동작이 발생할 수 있기 때문에 일관성을 유지하기 위해 재정의
}

class Solution {
    public int solution(int[][] points, int[][] routes) {

        ArrayList<HashMap<Point, Integer>> pointPerStep = new ArrayList<>();  // step 별 Point의 개수를 담는 리스트

        for (int[] route: routes) {  // 모든 route를 순회하며 step별 위치를 저장

            int step = 0;
            int curX = -1, curY = -1;

            for (int i = 0; i < route.length - 1; i++) {  // 경로를 따라 운송

                int[] start = points[route[i] - 1];  // 시작점
                int[] end = points[route[i + 1] - 1];  // 도착점
                int endX = end[0] - 1, endY = end[1] - 1;  // 도착점 좌표

                curX = start[0] - 1;  curY = start[1] - 1;  // 현 좌표

                while (!(curX == endX && curY == endY)) {  // 도착점에 도달하기 전까지 반복

                    if(step == pointPerStep.size())  // HashMap 생성 (Key: Point, Value: equals한 Point 객체 개수)
                        pointPerStep.add(new HashMap<Point, Integer>());
                    HashMap<Point, Integer> pointMap = pointPerStep.get(step++);
                    pointMap.put(new Point(curX, curY), pointMap.getOrDefault(new Point(curX, curY), 0) + 1);  // 해당 좌표의 개수 1 증가

                    if (curX != endX) {  // r 좌표 우선으로 하여 curX, curY 갱신
                        if (curX < endX)
                            curX++;
                        else
                            curX--;
                    } else {
                        if (curY < endY)
                            curY++;
                        else
                            curY--;
                    }
                }
            }

            if(step == pointPerStep.size())
                pointPerStep.add(new HashMap<Point, Integer>());
            HashMap<Point, Integer> pointMap = pointPerStep.get(step);
            pointMap.put(new Point(curX, curY), pointMap.getOrDefault(new Point(curX, curY), 0) + 1);  // 마지막 도착점 좌표까지 개수 1 증가
        }

        int answer = 0;
        for (int i = 0; i < pointPerStep.size(); i++)  // 모든 step 순회
            for (Integer cnt: pointPerStep.get(i).values())  // step 별 HashMap의 values(개수) 순회
                if (cnt > 1)  // 1번 이상 등장했다면 충돌 횟수 증가
                    answer++;

        return answer;
    }
}