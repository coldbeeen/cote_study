import java.util.*;

class Solution {

    public int solution(int coin, int[] cards) {
        // TreeMap 생성 (카드: 코인 필요 여부) -> 카드를 정렬 상태로 유지하여 카드의 쌍을 O(n)으로 찾기 위함
        TreeMap<Integer, Boolean> myCards = new TreeMap<>();
        int n = cards.length;
        int round = 1;  // 최종 결과값인 라운드값

        for (int i = 0; i < n / 3; i++)  // n/3개의 카드를 TreeMap에 저장
            myCards.put(cards[i], false);


        for (int i = n / 3; i < n; i += 2, round++) {  // 나머지 카드를 두 장씩 가져오며 라운드를 진행
            myCards.put(cards[i], true);
            myCards.put(cards[i + 1], true);

            // 카드 값을 ArrayList로 변환해 양쪽 포인터(인덱스)를 활용해 쌍을 찾음
            ArrayList<Integer> myCardList = new ArrayList<>(myCards.keySet());
            int left = 0, right = myCards.size() - 1;
            int finalLeftCard = -1, finalRightCard = -1, minCoinCost = Integer.MAX_VALUE;  // 최소 비용으로 카드를 버릴 수 있는 선택

            while (left < right) {  // 투 포인터 로직 수행
                int leftCard = myCardList.get(left);
                int rightCard = myCardList.get(right);

                if (leftCard + rightCard == n + 1) {  // 카드의 합이 n + 1이면 bool값 기반으로 coinCost를 계산해 버릴 카드를 고름
                    int coinCost = (myCards.get(leftCard) ? 1 : 0) + (myCards.get(rightCard) ? 1 : 0);

                    if (coinCost <= coin && coinCost < minCoinCost) {  // minCoinCost보다 적은 coinCost를 사용한다면 업데이트
                        finalLeftCard = leftCard;
                        finalRightCard = rightCard;
                        minCoinCost = coinCost;
                    }
                    left++; right--;
                } else if (leftCard + rightCard < n + 1) {
                    left++;
                } else {
                    right--;
                }
            }

            if (minCoinCost == Integer.MAX_VALUE)  // 라운드 종료
                break;

            coin -= minCoinCost;  // coin 개수 업데이트
            myCards.remove(finalLeftCard);  // 카드 쌍(ㅣeft, right)를 삭제
            myCards.remove(finalRightCard);
        }
        return round;
    }
}