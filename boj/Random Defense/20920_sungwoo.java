// 풀이 시간: 48분
// 풀이 방법: 모든 단어의 개수를 구하고, 개수별 단어 리스트를 만든다. 이후 개수 별로 단어 리스트를 기준에 맞게 정렬하여 출력한다.

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] str = br.readLine().split(" ");
        int N = Integer.parseInt(str[0]), M = Integer.parseInt(str[1]);

        HashMap<String, Integer> wordMap = new HashMap<>();  // 단어-개수 Map (key: word, value: count)

        for (int i = 0; i < N; i++) {  // 단어 입력 및 단어 개수 업데이트

            String word = br.readLine();
            if (word.length() >= M) {
                wordMap.put(word, wordMap.getOrDefault(word, 0) + 1);
            }
        }

        List<String> words = new ArrayList<>(wordMap.keySet());
        Collections.sort(words, new Comparator<String>((o1, o2) -> {
                // 자주 등장하는 단어 순서대로 정렬
                if (wordMap.get(o1) != wordMap.get(o2)) {
                    return wordMap.get(o2) - wordMap.get(o1)
                }
                // 등장 횟수가 같으면 길이가 긴 단어가 먼저 오도록 정렬
                if (o1.length() != o2.length()) {
                    return o2.length() - o1.length();
                }
                // 등장 횟수와 길이가 같으면 사전 순으로 정렬
                return o1.compareTo(o2);
            }
        });

        for (String word: words)  // 정렬된 words를 순서대로 출력
                bw.write(word + "\n");
        bw.flush();
    }
}