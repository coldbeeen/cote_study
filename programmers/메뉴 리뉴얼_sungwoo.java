import java.util.*;

class Solution {

    StringBuilder sb = new StringBuilder();

    public void combination(HashMap<String, Integer> combinations, String order, int n, int k){  // 조합 생성 재귀 함수
        if (sb.length() == n) {
            combinations.put(sb.toString(), combinations.getOrDefault(sb.toString(), 0) + 1);  // 동시에 해당 코스의 등장 횟수를 저장함
            return;
        }

        for (int i = k; i < order.length(); i++) {
            sb.append(order.charAt(i));
            combination(combinations, order, n, i + 1);
            sb.deleteCharAt(sb.length() - 1);
        }
    }

    public String[] solution(String[] orders, int[] course) {
        Arrays.sort(course);  // course 정렬 수행

        HashSet<String> result = new HashSet<>();  // 최종 코스요리 구성을 담을 HashSet

        for(int i = 0; i < orders.length; i++){  // orders 각 문자열 정렬 수행 (중복된 구성을 포함하지 않기 위함)
            char[] charArr = orders[i].toCharArray();
            Arrays.sort(charArr);
            orders[i] = new String(charArr);
        }

        for (int courseNum: course) {  // '코스 구성 개수' 배열을 순회하며 개수에 맞는 메뉴 조합을 고름

            HashMap<String, Integer> combinations = new HashMap<>();
            for (String order: orders)  // courseNum개 메뉴의 조합을 생성 (코스와 코스 등장 횟수를 저장)
                combination(combinations, order, courseNum, 0);

            int maxOrderCnt = -1;
            for (Map.Entry<String, Integer> entry: combinations.entrySet())  // 최대 등장 횟수 값을 구함
                maxOrderCnt = Math.max(maxOrderCnt, entry.getValue());

            if(maxOrderCnt < 2)  // maxOrderCnt가 2회 미만이라면 건너뜀
                continue;

            for (Map.Entry<String, Integer> entry: combinations.entrySet())  // maxOrderCnt번 등장한 코스를 result에 추가
                if (entry.getValue() == maxOrderCnt)
                    result.add(entry.getKey());
        }

        String[] resultArray = result.toArray(new String[0]);  // 정렬 후 리턴
        Arrays.sort(resultArray);
        return resultArray;
    }
}