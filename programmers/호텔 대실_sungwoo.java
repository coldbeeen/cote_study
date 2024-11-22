// 풀이 시간: 22분 50초

class Solution {

    public int convertTimeToMinute(String time) {  // HH:MM 형태의 시간을 분으로 변환하는 함수
        return Integer.valueOf(time.substring(0,2)) * 60 + Integer.valueOf(time.substring(3));
    }

    public int solution(String[][] book_time) {
        int roomCnt = 0, answer = 0;

        for (int minute = 0; minute < 60*24; minute++) {  // 00:00 - 23:59 까지 minute 변수로 반복하며, 해당 시각의 퇴실 및 입실을 기록함

            for (String[] startEndTime: book_time) {  // 방 개수의 불필요한 증가를 막기 위해 퇴실 먼저!
                int end = convertTimeToMinute(startEndTime[1]) + 10;
                if (minute == end)  // 퇴실할 시 방의 개수 감소
                    roomCnt -= 1;
            }

            for (String[] startEndTime: book_time) {
                int start = convertTimeToMinute(startEndTime[0]);
                if (minute == start)  // 입실할 시 방의 개수 증가
                    roomCnt += 1;
            }

            answer = Math.max(answer, roomCnt);  // answer 갱신
        }
        return answer;
    }
}