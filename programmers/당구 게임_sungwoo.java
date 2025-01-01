// 풀이 시간: 1시간 이상

import java.util.*;

class Solution {
    public int[] solution(int m, int n, int startX, int startY, int[][] balls) {

        int[] answer = new int[balls.length];

        for (int i = 0; i < balls.length; i++) {  // balls 순회

            int targetX = balls[i][0], targetY = balls[i][1];  // 목표 공의 X, Y
            int distX = Math.abs(targetX - startX), distY = Math.abs(targetY - startY);  // X축 거리, Y축 거리

            ArrayList<Integer> candidates = new ArrayList<>();  // 상하좌우 방향으로 쿠션을 때렸을 때의 거리를 저장하기 위한 리스트

            if (!(startX == targetX && startY < targetY))  // 윗쪽 쿠션을 맞출 수 있는 경우 계산하여 리스트에 추가
                candidates.add((int)(Math.pow(n - startY + n - targetY, 2) + Math.pow(distX, 2)));
            if (!(startX == targetX && startY > targetY))  // 아랫쪽 쿠션을 맞출 수 있는 경우 계산하여 리스트에 추가
                candidates.add((int)(Math.pow(startY + targetY, 2) + Math.pow(distX, 2)));
            if (!(startY == targetY && startX > targetX))  // 왼쪽 쿠션을 맞출 수 있는 경우 계산하여 리스트에 추가
                candidates.add((int)(Math.pow(startX + targetX, 2) + Math.pow(distY, 2)));
            if (!(startY == targetY && startX < targetX))  // 오른쪽 쿠션을 맞출 수 있는 경우 계산하여 리스트에 추가
                candidates.add((int)(Math.pow(m - startX + m - targetX, 2) + Math.pow(distY, 2)));

            answer[i] = Collections.min(candidates);  // 최솟값 계산
        }

        return answer;
    }
}