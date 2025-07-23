// 풀이 시간: 15분

import java.util.*;
import java.io.*;

public class Main {

    public static double gradeToPoint(String grade) {

        return switch (grade) {
            case "A+" -> 4.5;
            case "A0" -> 4.0;
            case "B+" -> 3.5;
            case "B0" -> 3.0;
            case "C+" -> 2.5;
            case "C0" -> 2.0;
            case "D+" -> 1.5;
            case "D0" -> 1.0;
            default -> 0.0;
        };
    }

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        final int N = 20;

        double creditSum = 0, creditTimesGradePointSum = 0;

        for (int i = 0; i < N; i++) {
            String[] s = br.readLine().split(" ");
            double credit = Double.parseDouble(s[1]);
            String grade = s[2];

            if (!grade.equals("P")) {
                creditSum += credit;
                creditTimesGradePointSum += credit * gradeToPoint(grade);
            }
        }

        System.out.println(creditTimesGradePointSum / creditSum);

    }
}