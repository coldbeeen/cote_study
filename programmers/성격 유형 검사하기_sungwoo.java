import java.util.HashMap;

class Solution {

    public String solution(String[] survey, int[] choices) {

        HashMap<Character, Integer> charCnt = new HashMap<Character, Integer>();  // {캐릭터: 점수}를 담을 HashMap 생성

        for (int i = 0; i < survey.length; i++) {  // 두 번째 문자(캐릭터)에 대해 score-4를 누적
            Character ch = survey[i].charAt(1);
            charCnt.put(ch, charCnt.getOrDefault(ch, 0) + choices[i] - 4);
        }

        String answer = "";  // answer 생성 후 각 캐릭터의 점수 비교를 통해 유형을 완성

        if(charCnt.getOrDefault('R', 0) >= charCnt.getOrDefault('T', 0))
            answer += 'R';
        else
            answer += 'T';

        if(charCnt.getOrDefault('C', 0) >= charCnt.getOrDefault('F', 0))
            answer += 'C';
        else
            answer += 'F';

        if(charCnt.getOrDefault('J', 0) >= charCnt.getOrDefault('M', 0))
            answer += 'J';
        else
            answer += 'M';

        if(charCnt.getOrDefault('A', 0) >= charCnt.getOrDefault('N', 0))
            answer += 'A';
        else
            answer += 'N';

        return answer;
    }
}