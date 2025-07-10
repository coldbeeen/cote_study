// 풀이 시간: 50분
// 풀이 방법: 배열을 전체 순회하여 가능한 키(후보)를 고르고, 그 중 가장 작은 키를 result에 삽입함.
//         이 과정을 N번 반복해 result를 완성할 수 있음.

import java.util.*;
import java.io.*;

public class Main
{

    public static boolean isPossible(int height, int tallerCnt, ArrayList<Integer> list) {  // 자기보다 큰 사람 수가 맞는지 검사

        int tmpTallerCnt = 0;
        for (int i = 0; i < list.size(); i++)
            if (list.get(i) > height)
                tmpTallerCnt++;

        return tmpTallerCnt == tallerCnt;
    }

    public static void main(String[] args) throws Exception{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] arr = new int[N];
        for (int i = 0 ; i < N; i++)
            arr[i] = Integer.parseInt(st.nextToken());

        ArrayList<Integer> result = new ArrayList<>();

        for (int k = 0; k < N; k++) {  // N명의 키를 순서대로 삽입할 것임

            ArrayList<Integer> candidates = new ArrayList<>();  // 후보 리스트

            for (int i = 0; i < N; i++) {
                if (isPossible(i + 1, arr[i], result) && !result.contains(i + 1))  // 이번 k 자리에 들어갈 수 있다면 후보로 추가
                    candidates.add(i + 1);
            }

            result.add(Collections.min(candidates));  // 후보 중 가장 작은 값부터 result에 삽입
        }

        for (int i = 0; i < N; i++)
            System.out.print(result.get(i) + " ");
    }
}