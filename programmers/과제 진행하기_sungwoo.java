// 풀이 시간: 33분
// 풀이 방법: 스택을 활용함.
//         시간을 기준으로 배열 정렬을 수행하였고,
//         수행하지 못한 과제는 스택에 삽입해, 시간이 남을 때마다 최근 과제 순으로 처리되도록 함

import java.util.*;

class Solution {

    class Assignment {  // 과제 클래스 (과제명과 남은 시간을 가짐)
        String name; int remainingTime;
        Assignment (String name, int remainingTime) {
            this.name = name; this.remainingTime = remainingTime;
        }
    }

    public int timeToMinute(String time) {  // 시간을 분 단위로 변환
        String[] timeArr = time.split(":");
        return Integer.parseInt(timeArr[0]) * 60 + Integer.parseInt(timeArr[1]);
    }

    public String[] solution(String[][] plans) {

        Arrays.sort(plans, new Comparator<String[]>() {  // plans를 시간순으로 정렬
            @Override
            public int compare(String[] a, String[] b) {
                return a[1].compareTo(b[1]);
            }
        });

        ArrayList<String> answer = new ArrayList<>();  // 결과 리스트
        Stack<Assignment> stack = new Stack<>();  // 과제 클래스를 원소로 가지는 스택 생성

        for (int i = 0; i < plans.length - 1; i++) {  // plans 순회

            String name = plans[i][0];
            int minute = timeToMinute(plans[i][1]), duration = Integer.parseInt(plans[i][2]);
            int nextMinute = timeToMinute(plans[i + 1][1]);

            if (minute + duration > nextMinute) {  // 이번 과제를 시간 내에 마치지 못한다면 스택에 삽입

                stack.push(new Assignment(name, minute + duration - nextMinute));

            } else {  // 이번 과제를 시간 내에 마칠 수 있다면, 남은 여유 시간동안 최근 과제 순으로 이어서 수행

                answer.add(name);  // 마친 과제는 결과 리스트에 추가

                int time = nextMinute - (minute + duration);  // 남은 여유 시간

                while (!stack.isEmpty() && time > 0) {  // 스택에서 최근 과제 순으로 가져와 과제를 수행함

                    Assignment assignment = stack.pop();
                    if (assignment.remainingTime > time) {  // 마치지 못한 과제는 수행 시간만큼만 빼고 다시 스택에 삽입
                        assignment.remainingTime -= time;
                        stack.push(assignment);
                        break;
                    }
                    time -= assignment.remainingTime;
                    answer.add(assignment.name);
                }
            }
        }
        answer.add(plans[plans.length - 1][0]);  // 가장 마지막 과제는 그대로 수행한 뒤

        while (!stack.isEmpty())  // 스택에 남은 과제 순차적으로 수행
            answer.add(stack.pop().name);

        return answer.toArray(new String[0]);
    }
}