// 풀이 시간: 20분
// 풀이 방법: 가로등 사이의 최대 간격을 찾는다.
//            각 가로등 사이는 ceil(간격 / 2)로 계산하고, 가장자리는 그대로 계산하여 최댓값을 찾는다.

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int goolLen = Integer.parseInt(br.readLine());  // 굴다리 길이
        int lightNum = Integer.parseInt(br.readLine());  // 가로등 개수
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int[] lightPoint = new int[lightNum];  // 가로등 위치
        for (int i = 0; i < lightNum; i++)
            lightPoint[i] = Integer.parseInt(st.nextToken());

        int maxInterval = lightPoint[0];  // 최대 간격을 저장 (가장자리는 h 만큼)
        for (int i = 1; i < lightNum; i++)  // 각 가로등 사이의 경우에는 h*2만큼 영향을 미치므로 ceil(간격 / 2)로 계산하여 최댓값을 갱신
            maxInterval = (int) Math.max(maxInterval, Math.ceil((lightPoint[i] - lightPoint[i-1]) / 2.0));
        maxInterval = Math.max(maxInterval, (goolLen) - lightPoint[lightNum - 1]);  // (가장자리는 h 만큼)

        System.out.println(maxInterval);
    }
}