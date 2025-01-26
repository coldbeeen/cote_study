// 풀이 시간: 18분

import java.util.*;

class Solution {
    public String[] solution(String[] record) {

        HashMap<String, String> idMap = new HashMap<>();  // Map 활용 (key: ID, Value: 닉네임)

        for (String rec: record) {  // 먼저 [id-nickname] Map을 완성시킴
            String[] splitRecord = rec.split(" ");
            String command = splitRecord[0], id = splitRecord[1];

            if (command.equals("Enter") || command.equals("Change")) {  // 닉네임이 추가, 갱신되는 경우에 Map 업데이트
                String nickname = splitRecord[2];
                idMap.put(id, nickname);
            }
        }

        ArrayList<String> result = new ArrayList<>();

        for (String rec: record) {  // 최종 완성된 Map을 기반으로 채팅방 메시지 생성
            String[] splitRecord = rec.split(" ");
            String command = splitRecord[0], id = splitRecord[1];

            if (command.equals("Enter"))
                result.add(idMap.get(id) + "님이 들어왔습니다.");
            else if (command.equals("Leave"))
                result.add(idMap.get(id) + "님이 나갔습니다.");
        }

        return result.toArray(new String[0]);
    }
}