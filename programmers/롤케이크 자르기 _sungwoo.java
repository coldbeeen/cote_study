// 풀이 시간: 1시간 이상 (삽질 1시간...)
// 반례도 계속 못 찾아서 헤맸는데, 알고보니 Integer끼리의 비교를 ==가 아닌 .equals()로 바꿔주니 정답이 나왔다.
// Java에서는 -128부터 127까지의 Integer 객체를 캐싱하므로 ==로 비교해도 동일한 객체를 참조하게 된다고 한다
// 그러나 이 범위를 벗어나는 Integer는 새로운 객체로 생성되므로 == 비교 결과가 다를 수 있다. (이걸 이제야 알다니!!!)

import java.util.*;

class Solution {

    public ArrayList<Integer> countKindOfTopping(ArrayList<Integer> tpList) {  // 토핑의 종류를 순차적으로 카운트하여 리턴함

        ArrayList<Integer> cntList = new ArrayList<>();  // 리턴할 카운트 List
        HashSet<Integer> tmpSet = new HashSet<>();  // 임시 HashSet (중복 허용 X)

        for(Integer tp: tpList) {
            tmpSet.add(tp);
            cntList.add(tmpSet.size());  // Set의 길이로 카운트 List를 채움
        }

        return cntList;
    }

    public int solution(int[] topping) {

        ArrayList<Integer> tpList = new ArrayList<>();
        for (int tp: topping)
            tpList.add(tp);

        ArrayList<Integer> p1CntList = countKindOfTopping(tpList); // 정방향으로 종류 카운트
        Collections.reverse(tpList);
        ArrayList<Integer> p2CntList = countKindOfTopping(tpList);  // 역방향으로 종류 카운트

        int answer = 0;
        for (int i = 0; i < tpList.size() - 1; i++)  // 각자의 종류 카운트 List를 활용헤 공평하게 나눠지는 위치에서 answer 증가
            if (p1CntList.get(i).equals(p2CntList.get(p2CntList.size() - i - 2)))
                answer++;

        return answer;
    }
}