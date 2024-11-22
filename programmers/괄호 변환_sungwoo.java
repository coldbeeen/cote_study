// 풀이 시간: 33분 40초

class Solution {

    public String flipParenthesis(String p) {  // 괄호를 뒤집는 함수
        StringBuilder result = new StringBuilder();  // 효율적인 처리를 위해 StringBuilder를 활용

        for (int i = 0; i < p.length(); i++) {
            if(p.charAt(i) == '(')
                result.append(')');
            else
                result.append('(');
        }
        return result.toString();
    }

    public boolean isCorrentParenthesis(String p) {  // '올바른 괄호 문자열'인지 확인하는 함수
        int cnt = 0;

        for (int i = 0; i < p.length(); i++) {  // 문자열을 순회하며 닫는 괄호의 개수가 여는 괄호의 개수를 넘어가는지 확인
            if (p.charAt(i) == '(') {
                cnt++;
            }
            else {
                cnt--;
                if (cnt < 0)
                    return false;
            }
        }
        return true;
    }

    public String convertToCorrectParenthesis(String p) {  // '올바른 괄호 문자열'을 생성하는 재귀 하뭇

        if (p.equals(""))  // 빈 문자열은 그대로 리턴
            return p;

        int i, l_cnt = 0, r_cnt = 0;  // 두 균형잡힌 괄호 문자열로 분리하기 위해 분할점을 찾음
        for (i = 0; i < p.length(); i++) {
            if (!(l_cnt == 0 && r_cnt == 0) && l_cnt == r_cnt)
                break;
            if (p.charAt(i) == '(')
                l_cnt++;
            else
                r_cnt++;
        }

        String u = p.substring(0, i), v = p.substring(i);  // u, v로 분리

        if (isCorrentParenthesis(u))  // u가 이미 올바른 문자열이라면 v를 재귀한 뒤, 합쳐서 리턴
            return u + convertToCorrectParenthesis(v);

        String result = "(" + convertToCorrectParenthesis(v) + ")"  // v 재귀 및 u에 대한 작업을 수행한 뒤, 합쳐서 리턴
                + flipParenthesis(u.substring(1, u.length() - 1));

        return result;
    }


    public String solution(String p) {
        return convertToCorrectParenthesis(p);
    }
}