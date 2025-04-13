class Solution {
    public boolean notDivisible(int[] arr, int num){  // arr의 모든 원소가 num으로 나누어떨어지지 않는지 검사
        for(int n: arr)
            if(n % num == 0)
                return false;
        return true;
    }

    public int gcd(int a, int b){  // 최대공약수 리턴
        if(a % b == 0) return b;
        return gcd(b, a % b);
    }

    public int solution(int[] arrayA, int[] arrayB) {

        int answer = 0;
        int gcdA = arrayA[0], gcdB = arrayB[0];

        // 1. 각 배열의 최대공약수를 구함
        for(int i = 1; i< arrayA.length;i++){
            gcdA = gcd(gcdA, arrayA[i]);
            gcdB = gcd(gcdB, arrayB[i]);
        }

        // 2. 서로의 배열을 나눌 수 없는지 확인
        if(notDivisible(arrayB, gcdA) && answer < gcdA)
            answer = gcdA;
        if(notDivisible(arrayA, gcdB) && answer < gcdB)
            answer = gcdB;

        // 3. 최댓값 반환
        return answer;
    }
}