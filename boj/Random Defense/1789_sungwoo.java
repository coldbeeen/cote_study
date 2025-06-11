// 풀이 시간: 7분
// 풀이 방법: (시그마 공식에 따라) 시간복잡도는 약 sqrt(S)
//          즉 문제 없을 것이라 판단해 N의 최댓값을 선형 탐색함

import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long s = Long.parseLong(br.readLine());  // Long 타입으로 입력 받음

        long sum = 0, i = 1;  // i를 1부터 탐색
        while (true) {
            sum += i;
            if (sum > s)  // s보다 커지면 반복문 종료
                break;
            i++;
        }

        System.out.println(i - 1);  // i - 1 리턴
    }
}