class Solution {

    public int timeToSec(String time){  // HH:MM:SS -> second
        String[] timeArr = time.split(":");
        return Integer.valueOf(timeArr[0]) * 60 * 60 + Integer.valueOf(timeArr[1]) * 60 + Integer.valueOf(timeArr[2]);
    }

    public String secToTime(int sec){  // second -> HH:MM:SS
        return String.format("%02d:%02d:%02d", sec / (60 * 60), (sec % (60 * 60)) / 60, sec % 60);
    }

    public String solution(String play_time, String adv_time, String[] logs) {

        int playSec = timeToSec(play_time), advSec = timeToSec(adv_time);
        long[] allTime = new long[playSec + 1];  // playSec(시간:초) 크기 만큼의 배열 생성 (테스트 케이스 17 틀림으로 인해 long형으로 수정)

        for (int i = 0; i < logs.length; i++) {  // start & end time을 가져와 i 시간에 시청을 시작 & 종료한 이벤트 +1 & -1로 기록
            String[] interval = logs[i].split("-");
            Integer start = timeToSec(interval[0]), end = timeToSec(interval[1]);

            allTime[start]++;
            allTime[end]--;
        }

        for (int i = 1; i <= playSec; i++)  // 위에서 기록한 정보를 바탕으로 모든 시간의 시청자 수를 기록
            allTime[i] += allTime[i-1];

        for (int i = 1; i <= playSec; i++)  // 기록된 시청자 수를 바탕으로 누적 시청자 수를 기록
            allTime[i] += allTime[i-1];

        long maxView = 0;  // (테스트 케이스 17 틀림으로 인해 long형으로 수정)
        int maxTime = 0;
        for (int i = advSec - 1; i <= playSec; i++) {  // 누적된 시청자 수를 바탕으로 가장 시청자 수가 많은 구간을 탐색
            if (i >= advSec) {
                if (allTime[i] - allTime[i - advSec] > maxView) {
                    maxView = allTime[i] - allTime[i - advSec];
                    maxTime = i - advSec + 1;
                }
            } else {
                if (allTime[i] > maxView) {
                    maxView = allTime[i];
                    maxTime = i - advSec + 1;
                }
            }
        }

        return secToTime(maxTime);  // Time으로 원상복구하여 리턴
    }
}