// 풀이 시간: 35분
// 풀이 방법:
// 각 문자를 key, 문자의 인덱스들을 value로 저장하고, k개 이상 존재하는 문자에 대해
// 'k 간격(k개의 문자가 포함되었다는 뜻)의 인덱스 값'으로 maxLen과 minLen을 구한다.

fun main() {

    val t = readln().toInt()

    repeat(t) {  // t번 반복

        val str = readln()
        val k = readln().toInt()

        val map = mutableMapOf<Char, MutableList<Int>>()   // map 생성 (key: 문자, value: 해당 문자 인덱스 리스트)
        str.forEachIndexed { index, char ->
            map.getOrPut(char) { mutableListOf() }.add(index)  // '문자' - '문자의 인덱스 List'로 map을 구성
        }

        var minLen = 10000
        var maxLen = -1

        for ((char, idxList) in map) {  // k개 이상 존재하는 문자들에 대해 'k 간격(k개의 문자가 포함되었다는 뜻)의 인덱스 값'으로 maxLen과 minLen을 구함

            if (idxList.size < k) continue

            for (i in 0 until idxList.size - (k - 1)) {  // k 간격(k개의 문자가 포함되었다는 뜻)으로 인덱스 값을 가져와 길이를 구함

                val len = idxList[i + (k - 1)] - idxList[i] + 1
                if (len > maxLen) maxLen = len
                if (len < minLen) minLen = len
            }
        }

        if (maxLen != -1)
            println("$minLen $maxLen")
        else
            println(-1)
    }
}