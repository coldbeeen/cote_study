// 풀이 시간: 40분
// 풀이 방법: 재귀(백트래킹)를 활용해 가능한 조합들을 생성하고, 과일 주스를 만들어 10진수로 변환해 Set에 담았다. (ps. HashSet은 동등성 비교가 이루어지므로 String으로 해도 되겠다)
//        + 조합 생성 이전에 중복된 맛을 가진 과일을 사전에 제거해주는 것도 좋겠다는 생각이 들었다.

import java.util.*;

class Main {

    public static int fruitToInt(String fruit) {  // 과일 배열 2진수를 10진수로 변환
        return Integer.parseInt(fruit, 2);
    }

    public static String mix(ArrayList<String> combList) {  // 과일 조합을 섞음

        int fruitLen = combList.get(0).length();
        char[] juice = new char[fruitLen];
        for (int i = 0; i < fruitLen; i++)
            juice[i] = '0';

        for (String comb: combList)   // 섞기 (comb의 1을 tmp에 씌우기)
            for (int i = 0; i < comb.length(); i++)
                if (comb.charAt(i) == '1')
                    juice[i] = '1';

        return new String(juice);
    }

    public static void comb(String[] fruits, ArrayList<String> combList, int k, int start, HashSet<Integer> juiceSet) {  // k개로 이후어진 조합 생성

        if (combList.size() == k) {
            int juiceInt = fruitToInt(mix(combList));   // k개의 조합으로 섞은 후 10진수로 변환
            juiceSet.add(juiceInt);  // 해당 값을 과일주스 set에 삽입
        }

        for (int i = start; i < fruits.length; i++) {  // 재귀 방식으로 가능한 모든 조합 생성
            combList.add(fruits[i]);
            comb(fruits, combList, k, i + 1, juiceSet);
            combList.remove(combList.size() - 1);
        }
    }

    public static int solution(String[] fruits, int k) {

        HashSet<Integer> juiceSet = new HashSet<>();  // 과일주스 Set (10진수로 변환하여 담음)
        comb(fruits, new ArrayList<>(), k, 0, juiceSet);  // 조합 생성

        return juiceSet.size();
    }

    public static void main(String[] args) {

        System.out.println(solution(new String[] {"1100", "0110", "0011", "1100"}, 2));
        System.out.println(solution(new String[] {"100", "100", "011", "100", "111", "011"}, 1));
        System.out.println(solution(new String[] {"100", "100", "011", "100", "111", "011"}, 5));
        System.out.println(solution(new String[] {"001", "001", "001", "010", "010", "010", "010", "100", "100"}, 3));
    }
}