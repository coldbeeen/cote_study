// 풀이 시간: 45분
// 풀이 방법: 각 집중국 수신 구간의 "간격"을 내림차순으로 K-1개 구해, "각 간격의 양 끝점 값"으로 "각 집중국 수신 길이"를 구해 누적함

import java.util.*;
import java.io.*;

public class Main {

    static class Range {
        int start, end, interval;

        Range(int start, int end, int interval) {
            this.start = start;
            this.end = end;
            this.interval = interval;
        }
    }

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine()), K = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] sensorArr = new int[N];
        for (int i = 0; i < N; i++) {
            sensorArr[i] = Integer.parseInt(st.nextToken());
        }

        if (N == 1) {  // 센서가 하나라면 0 출력
            System.out.println(0);
            return;
        }

        Arrays.sort(sensorArr);  // 센서 위치 정렬 후
        ArrayList<Range> rangeList = new ArrayList<>();  // 각 센서 구간의 간격을 담을 리스트 생성
        for (int i = 1; i < N; i++) {  // 각 구간의 간격의 [시작점, 끝점, 간격 길이]을 생성
            rangeList.add(new Range(i - 1, i, sensorArr[i] - sensorArr[i - 1]));
        }

        rangeList.sort((a, b) -> Integer.compare(b.interval, a.interval));  // 간격 길이로 내림차순 정렬
        ArrayList<Range> kRangeList = new ArrayList<>(rangeList.subList(0, Math.min(K - 1, N - 1)));  // 그 중 K - 1개를 가져옴 (실제로 나눌 구간))
        kRangeList.sort((a, b) -> Integer.compare(a.start, b.start));  // k개의 간격 오름차순 정렬

        int result = 0, prevEnd = 0;

        for (int i = 0; i < kRangeList.size(); i++) {  // 간 간격의 양 끝점으로 집중국 수신 길이를 누적함
            Range range = kRangeList.get(i);
            result += sensorArr[range.start] - sensorArr[prevEnd];
            prevEnd = range.end;
        }
        result += sensorArr[sensorArr.length - 1] - sensorArr[prevEnd];

        System.out.println(result);
    }
}