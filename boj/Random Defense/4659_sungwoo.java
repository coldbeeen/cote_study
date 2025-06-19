// 풀이 시간: 29분

import java.io.*;

public class Main
{

    public static boolean isVowel(char c) {  // 모음 여부 리턴
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u')
            return true;
        return false;
    }

    public static boolean is_E_or_O(char c) {  // e 또는 o 여부 리턴
        if (c == 'e' || c == 'o')
            return true;
        return false;
    }

    public static void main(String[] args) throws IOException{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {

            String password = br.readLine();

            if (password.equals("end"))
                break;

            boolean containsVowel = false, threeConsequtive = false, twoSameChar = false;  // 각각 조건 1,2,3에 해당하는 boolean 변수
            int vowelCnt = 0, notVowelCnt = 0;  // 연속된 자옴 또는 모음 개수 카운트

            for (int i = 0; i < password.length(); i++) {

                char c = password.charAt(i);

                // 검증 - 1. 모음 포함  2. 3개 연속 자음 또는 모음
                if (isVowel(c)) {
                    containsVowel = true;
                    notVowelCnt = 0;
                    vowelCnt++;
                } else {
                    vowelCnt = 0;
                    notVowelCnt++;
                }
                if (vowelCnt >= 3 || notVowelCnt >= 3) {
                    threeConsequtive = true;
                    break;
                }

                // 검증 - 3. 2개 연속 같은 글자
                if (i > 0 && !is_E_or_O(c) && password.charAt(i - 1) == c) {
                    twoSameChar = true;
                    break;
                }
            }

            if (containsVowel && !threeConsequtive && !twoSameChar) {  // 종합적으로 고려하여 품질 평가
                System.out.println("<" + password + "> is acceptable.");
            } else {
                System.out.println("<" + password + "> is not acceptable.");
            }

        }
    }
}