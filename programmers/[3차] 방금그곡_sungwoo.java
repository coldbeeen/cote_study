import java.util.*;

class Solution {

    public int getTimeDuration(String start, String end) {  // 음악 길이를 계산하는 함수
        String[] startArr = start.split(":"), endArr = end.split(":");
        int startMinute = Integer.parseInt(startArr[0]) * 60 + Integer.parseInt(startArr[1]);
        int endMinute = Integer.parseInt(endArr[0]) * 60 + Integer.parseInt(endArr[1]);
        return endMinute - startMinute;
    }

    public List<String> convertMelodyToList(String melody) {  // 멜로디를 리스트로 변환하는 함수 (C# 등의 음을 고려하기 위함)
        ArrayList<String> melodyList = new ArrayList<>();

        for(int i = 0; i < melody.length(); i++) {
            if(i < melody.length() - 1 && melody.charAt(i + 1) == '#')
                melodyList.add(melody.substring(i, (i++) + 2));
            else
                melodyList.add(String.valueOf(melody.charAt(i)));
        }

        return melodyList;
    }

    public String solution(String m, String[] musicinfos) {
        String match = "(None)";  // 일치하는(찾은) 음악 제목
        int matchDuration = 0;  // 일치하는(찾은) 음악 길이 (더 긴 음악을 저장하기 위함)

        List<String> melody = convertMelodyToList(m);  // 주어진 멜로디를 리스트로 변환하여 저장

        for (String musicInfo: musicinfos) {  // 모든 음악(악보)를 순회
            String[] musicInfoArr = musicInfo.split(",");
            int duration = getTimeDuration(musicInfoArr[0], musicInfoArr[1]);  // 음악 길이
            String title = musicInfoArr[2];  // 음악 제목
            List<String> sheetMusic = convertMelodyToList(musicInfoArr[3]);  // 음악 악보(멜로디)를 리스트로 변환하여 저장

            for (int i = 0; i < duration; i++) {  // 악보의 인덱스 i부터 시작해 멜로디를 탐색할 것임
                int j = 0;
                while (j < melody.size() && (j+i) < duration &&  // 주어진 멜로디가 음악 멜로디와 일치할 때까지 j를 통해 반복
                        melody.get(j).equals(sheetMusic.get((j + i) % sheetMusic.size()))) { j++; }

                if (j == melody.size() && duration > matchDuration) {  // 일치하는 음악이라면 음악 길이를 고려하여 저장
                    match = title; matchDuration = duration;
                }
            }
        }

        return match;
    }
}