import java.util.*;

class Solution {

    public int convertTimeIntoMinutes(String time) {  // HH:MM 형태를 분 단위로 변환
        String[] timeArr = time.split(":");
        return Integer.parseInt(timeArr[0]) * 60 + Integer.parseInt(timeArr[1]);
    }

    public int[] solution(int[] fees, String[] records) {

        HashMap<Integer, Integer> currentVehicle = new HashMap<>();  // HashMap (차량번호 - 입차시간) 생성
        TreeMap<Integer, Integer> vehicleParkingMinutes = new TreeMap<>();  // TreeMap (차량번호 - 주차시간) 생성 -> 차량번호 기준 정렬됨

        int basicTime = fees[0], basicFee = fees[1];
        int unitTime = fees[2], unitFee = fees[3];

        for (String record: records) {  //
            String[] recordArr = record.split(" ");
            int minute = convertTimeIntoMinutes(recordArr[0]), vehicleNum = Integer.parseInt(recordArr[1]);  // 시간, 차량번호

            if (recordArr[2].equals("IN")) {  // 입차인 경우 입차시간 저장
                currentVehicle.put(vehicleNum, minute);
            } else {  // 출차인 경우 해당 차량번호의 입차시간을 빼고 주차시간 누적 (출차한 차량을 HashMap에서 제거 - 출차하지 않은 차량 판단하기 위함)
                int parkingMinute = minute - currentVehicle.get(vehicleNum);
                vehicleParkingMinutes.put(vehicleNum, vehicleParkingMinutes.getOrDefault(vehicleNum, 0) + parkingMinute);
                currentVehicle.remove(vehicleNum);
            }
        }

        for (Map.Entry<Integer, Integer> entry : currentVehicle.entrySet()) {  // 출차하지 않는 차량의 시간 누적
            int vehicleNum = entry.getKey(), minute = entry.getValue();
            vehicleParkingMinutes.put(
                    vehicleNum, vehicleParkingMinutes.getOrDefault(vehicleNum, 0) + convertTimeIntoMinutes("23:59") - minute);
        }

        int[] result = new int[vehicleParkingMinutes.size()];  // 결과 배열 생성
        int i = 0;

        for (Map.Entry<Integer, Integer> entry: vehicleParkingMinutes.entrySet()) {  // 차량번호 오름차순으로 순회하며 주차시간으로 비용 계산
            int parkingMinute = entry.getValue();
            result[i++] = (parkingMinute <= basicTime) ? basicFee :
                    basicFee + (int) Math.ceil((double) (parkingMinute - basicTime) / unitTime) * unitFee;
        }

        return result;
    }
}