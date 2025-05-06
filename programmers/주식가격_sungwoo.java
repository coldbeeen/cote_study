// 풀이 시간: 22분
// 풀이 방법: 스택을 활용하였다. 주식가격 하락 시, 해당 가격보다 비싼 시간의 객체를 연속으로 pop을 수행하며 결괏값을 저장하였고, 시간복잡도 O(n)으로 풀 수 있겠다. (문제 유형을 몰랐다면 바로 이런 풀이가 떠올랐을 지는 확신하지 못하겠다.)

import java.util.*;

class Solution {

    class TimeAndPrice {  // 시간과 주식가격을 담을 클래스
        int time, price;
        TimeAndPrice(int time, int price) { this.time = time; this.price = price; }
    }

    public int[] solution(int[] prices) {

        Stack<TimeAndPrice> stack = new Stack<>();  // 시간과 주식가격을 담는 스택 초기화
        int[] answer = new int[prices.length];  // 결과 배열

        for (int i = 0; i < prices.length; i++) {

            while(!stack.isEmpty() && stack.peek().price > prices[i]) {  // 가격이 떨어진 시점부터 해당 가격보다 싼 시점까지 계속 pop을 수행함
                TimeAndPrice timeAndPrice = stack.pop();
                answer[timeAndPrice.time] = i - timeAndPrice.time;  // 결괏값 저장
            }

            stack.push(new TimeAndPrice(i, prices[i]));  // 결과를 담은 이후, i초의 가격을 push함
        }

        while (!stack.isEmpty()) {  // 스택에 남은 요소들은 마지막까지 가격이 떨어지지 않은 요소임. 나머지 결괏겂을 저장함
            TimeAndPrice timeAndPrice = stack.pop();
            answer[timeAndPrice.time] = prices.length - (timeAndPrice.time + 1);
        }

        return answer;
    }
}