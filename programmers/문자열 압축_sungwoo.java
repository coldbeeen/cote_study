class Solution {
    public int solution(String s) {

        int minSize = s.length();

        for (int unit = 1; unit <= s.length() / 2; unit++) {  // 문자열 분할 단위를 순회
            int i = 0, curSize = 0;  // curSize: 현재 압축 문자열의 길이

            while (i + unit <= s.length()) {  // 분할이 불가능할 때까지 반복
                String tmp = s.substring(i, i + unit);  // 임시 분할 후

                int j = i + unit, cnt = 1;  // j: 다음 분할 기준 인덱스, cnt: 압축 가능한 문자열 개수
                while (j + unit <= s.length() && tmp.equals(s.substring(j, j + unit))) {  // tmp와 동일한 문자열 카운팅
                    j += unit;
                    cnt++;
                }

                curSize += cnt > 1 ? Integer.toString(cnt).length() + unit : unit;  // 압축 가능한 경우 cnt 자리수 고려하여 curSize 갱신
                i = j;  // i는 j에 이어서 순회
            }

            minSize = Math.min(curSize + s.length() - i, minSize);  // "curSize + 남은 문자열 길이"로 최솟값 갱신
        }

        return minSize;
    }
}