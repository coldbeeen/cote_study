// 풀이 시간: 55분
// 풀이 방법: 각 집합의 크기를 인덱스로 하는 List를 만든 후, 크기 1인 집합부터 그 다음 크기의 집합과 차집합 연산을 하며 튜플을 복구한다.

import java.util.*;

class Solution {
    public int[] solution(String s) {

        ArrayList<HashSet<Integer>> setList = new ArrayList<>();  // 사이즈별 Set을 담는 List 생성

        for (int i = 0; i <= 500; i++)  // List 내부의 Set 초기화
            setList.add(new HashSet<>());


        // 1. s를 순회하며 각 집합의 크기를 인덱스로 하여 setList에 삽입함
        StringBuilder sb = new StringBuilder();
        HashSet<Integer> tmpSet = new HashSet<>();

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            if (c == '{') {
                continue;
            } else if (c == '}') {  // 닫히는 중괄호를 만나면, tmpSet에 모은 원소의 개수를 인덱스로 하여 set을 삽입함
                tmpSet.add(Integer.parseInt(sb.toString()));
                sb = new StringBuilder();
                setList.get(tmpSet.size()).addAll(tmpSet);
                tmpSet = new HashSet<>();
                i++;
            } else if (c == ',') {
                tmpSet.add(Integer.parseInt(sb.toString()));
                sb = new StringBuilder();
            } else {
                sb.append(c);
            }
        }


        // 2. 크기 1인 집합부터 그 다음 크기의 집합과 차집합 연산을 하며 튜플을 복구함
        ArrayList<Integer> answer = new ArrayList<>();

        for (int i = 1; i <= 500; i++) {
            HashSet<Integer> prevSet = setList.get(i - 1), curSet = setList.get(i);

            if (curSet.isEmpty())  // 현재 집합이 비었다면 반복문 중단
                break;

            HashSet<Integer> diff = new HashSet<>(curSet);
            diff.removeAll(prevSet);  // 현재 집합과 이전 집합과의 차집합 수행

            Iterator iter = diff.iterator();
            answer.add((Integer)iter.next());  // 남은 원소를 answer(튜플)에 추가함
        }

        return answer.stream().mapToInt(i -> i).toArray();
    }
}