// 풀이 시간: 50분
// 풀이 방법: 문제의 제약 조건이 명시되지 않은 관계로 타임 테이블 활용 vs Map 활용 중에 고민하다가 좀 더 직관적인 Map을 활용하기로 결정했다.
//         HashMap을 활용해 "Key: 유저 ID, Value: [최초 접속 시간, 최근 접속 시간]" 형태로 접속 중인 유저를 관리하여 문제를 해결하였다.
//         하나의 request를 처리할 때 마다 autoDisconnect 메서드를 통해 b초가 지난 유저를 접속 해제시키며,
//         접속 중인 유저 수가 n보다 크거나 같을 때는 자리 비움 유저를 접속 해제시킨다.

import java.util.*;

class Main {

    public static HashSet<Integer> mixFruitList = new HashSet<>();

    public static int fruitToInt(String fruit) {  // 과일 배열 2진수를 10진수로 변환
        return Integer.parseInt(fruit, 2);
    }

    public static String mix(ArrayList<String> combList) {  // 과일 조합을 섞음

        char[] mixedFruit = new char[combList.get(0).length()];

        for (String comb: combList)   // 섞기 (comb의 1을 tmp에 씌우기)
            for (int i = 0; i < comb.length(); i++)
                if (comb.charAt(i) == '1')
                    mixedFruit[i] = 1;

        return new String(mixedFruit);
    }

    public static void comb(String[] fruits, ArrayList<String> combList, int k, int start) {  // k개로 이후어진 조합 생성

        if (combList.size() == k) {

            int mixedFruitInt = fruitToInt(mix(combList));
            mixFruitList.add(mixedFruitInt);

        }
        for (int i = start; i < fruits.length; i++) {
            combList.add(fruits[i]);
            comb(fruits, combList, k, i);
            combList.remove(combList.size() - 1);
        }
    }

    public static List<Integer> solution(String[] fruits, int k) {

        comb(fruits, new ArrayList<>(), k, 0, mixFruitList);

        return mixFruitList.size();
    }

    public static void main(String[] args) {

        System.out.println(solution(new String[] {"1100", "0110", "0011", "1100"}, 2));
    }
}