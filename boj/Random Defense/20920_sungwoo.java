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

        HashMap<Integer, ArrayList<String>> cntMap = new HashMap<>();  // 개수-단어리스트 Map (key: count, value: word list)

        for (Map.Entry<String, Integer> entry: wordMap.entrySet()) {  // 단어 개수를 키로 하여 단어 추가

            String word = entry.getKey();
            int cnt = entry.getValue();

            if (!cntMap.containsKey(cnt))
                cntMap.put(cnt, new ArrayList<>());

            cntMap.get(cnt).add(word);
        }

        ArrayList<Integer> cntList = new ArrayList<>(cntMap.keySet());  // 키(단어 개수)를 따로 가져옴
        Collections.sort(cntList, Comparator.reverseOrder());  // 내림차순 정렬함

        for (int cnt: cntList) {  // 단어 개수가 많은 순으로 cntMap 순회

            ArrayList<String> words = cntMap.get(cnt);  // 단어 개수가 cnt개인 단어 리스트

            Collections.sort(words, (a, b) -> {  // 2, 3번 기준에 따른 정렬 수행
                if (a.length() == b.length())  // 길이가 같은 경우 사전순
                    return a.compareTo(b);
                else  // 길이가 다른 경우 길이순
                    return -Integer.compare(a.length(), b.length());
            });

            for (String word: words)  // 정렬된 words를 순서대로 출력
                bw.write(word + "\n");
        }
        bw.flush();
    }
}