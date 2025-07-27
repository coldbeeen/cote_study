// 풀이시간: 25분

import java.io.*;
import java.util.*;

public class Main
{
    public static void main(String[] args) throws Exception{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        StringBuilder original = new StringBuilder();

        int sIdx = 0, originalIdx = 0, i = 1;

        while (sIdx < s.length()) {  // s를 끝까지 순회하면, i - 1이 최종 매칭된 숫자가 됨

            if (original.length() <= originalIdx)  // original String을 동적으로 늘려줌 (현재 숫자 i를 추적하기 위함)
                original.append(i++);

            if (original.charAt(originalIdx) == s.charAt(sIdx))  // 같을 때 sIdx를 증가
                sIdx++;

            originalIdx++;
        }

        System.out.println(i - 1);
    }
}