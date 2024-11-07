import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;

class Solution {
    public int[] solution(String msg) {
        HashMap<String, Integer> dict = new HashMap<String, Integer>();  // 사전 HashMap
        ArrayList<Integer> answer = new ArrayList<>();  // msg 압축 결과 Arraylist
        int nextIndexNum = 27;  // 다음 색인 번호

        for (int i = 0; i < 26; i++)  // 알파벳 색인 값 초기 설정
            dict.put(String.valueOf((char)('A' + i)), i + 1);


        for (int i = 0; i < msg.length(); ) {  // 문자열 순회

            int substringSize = 1;
            while (i + substringSize <= msg.length()) {  // 사전에 존재하지 않는 문자열이 나올 때까지 substringSize++
                if (!dict.containsKey(msg.substring(i, i + substringSize)))
                    break;
                substringSize++;
            }

            int indexNum = dict.get(msg.substring(i, i + substringSize - 1));  // substringSize - 1 까지의 문자열 색인 번호 가져옴
            answer.add(indexNum);  // 색인 번호 저장 후
            if (i + substringSize <= msg.length())  // 새로운 색인 생성 (마지막 문자열이 아니라면)
                dict.put(msg.substring(i, i + substringSize), nextIndexNum++);

            i += substringSize - 1;  // 압축한 문자열만큼 i 증가
        }

        return answer.stream().mapToInt(i -> i).toArray();  // 결과 int array로 리턴
    }
}