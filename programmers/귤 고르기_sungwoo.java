// 풀이시간: 15분

import java.util.*;

class Solution {
    public int solution(int k, int[] tangerine) {

        HashMap<Integer, Integer> map = new HashMap<>();  // 해쉬맵 활용 (key: 크기, value: 개수)

        // 1. 귤 크기별로 개수를 저장
        for (int i = 0; i < tangerine.length; i++)
            map.put(tangerine[i], map.getOrDefault(tangerine[i], 0) + 1);

        // 2. 리스트에 크기별 귤 개수(values)를 내림차순으로 저장
        ArrayList<Integer> cntList = new ArrayList<>();

        for (Integer key: map.keySet()) {
            cntList.add(map.get(key));
        }

        cntList.sort(Comparator.reverseOrder());

        // 3. 귤을 개수가 많은 크기부터 담으며 반복하며 종류의 최솟값을 구함
        Iterator<Integer> cntIter = cntList.iterator();
        int answer = 0;

        while (k > 0) {  // 더 이상 담을 귤이 없을 때까지 반복
            k -= cntIter.next();
            answer++;
        }

        return answer;
    }
}