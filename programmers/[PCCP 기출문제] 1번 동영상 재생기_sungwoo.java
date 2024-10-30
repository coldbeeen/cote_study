class Solution {

    public int timeToSec(String time) {  // MM:SS to second
        String[] splitTime = time.split(":");
        return Integer.valueOf(splitTime[0]) * 60 + Integer.valueOf(splitTime[1]);
    }

    public String secToTime(int sec) {  // second to MM:SS
        return String.format("%02d:%02d", sec / 60, sec % 60);
    }

    public int skip(int posSec, int opStartSec, int opEndSec) {  // 스킵 구간이라면 opEndSec으로 스킵
        if (posSec >= opStartSec && posSec <= opEndSec)
            return opEndSec;
        return posSec;
    }

    public String solution(String video_len, String pos, String op_start, String op_end, String[] commands) {

        int videoLenSec = timeToSec(video_len);  // second(초)로 변환
        int posSec = timeToSec(pos);
        int opStartSec = timeToSec(op_start);
        int opEndSec = timeToSec(op_end);

        for (String command: commands) {  // 명령을 수행
            posSec = skip(posSec, opStartSec, opEndSec);  // 스킵 조건에 해당하면 스킵

            if (command.equals("prev"))  // 10초 전으로 이동 (0보다 작아지지 않음)
                posSec = posSec - 10 >= 0 ? posSec - 10 : 0;
            else if (command.equals("next"))  // 10초 후로 이동 (videoLenSec보다 커지지 않음)
                posSec = posSec + 10 <= videoLenSec ? posSec + 10 : videoLenSec;
        }

        posSec = skip(posSec, opStartSec, opEndSec);  // 스킵 조건에 해당하면 스킵
        return secToTime(posSec);  // MM:SS로 변환하여 출력
    }
}