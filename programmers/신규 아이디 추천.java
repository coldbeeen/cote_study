import java.util.LinkedList;
import java.util.ListIterator;

class Solution {

    public String solution(String new_id) {

        LinkedList<Character> newIdList = new LinkedList<>();
        for (char c: new_id.toCharArray())
            newIdList.add(c);

        // 1 ~ 2단계
        ListIterator<Character> iter = newIdList.listIterator();
        while(iter.hasNext()){
            char c = iter.next();
            if (c >= 'A' && c <= 'Z')
                iter.set((char) (c + 'a' - 'A'));
            else if (!(c >= '0' && c <= '9') && !(c >= 'a' && c <= 'z') && c != '-' && c != '_' && c != '.')
                iter.remove();
        }

        // 3단계
        iter = newIdList.listIterator();
        while(iter.hasNext())
            if (iter.next() == '.')
                while (iter.hasNext() && iter.next() == '.')
                    iter.remove();


        // 4단계
        if (newIdList.size() > 0 && newIdList.getFirst() == '.')
            newIdList.removeFirst();
        if (newIdList.size() > 0 && newIdList.getLast() == '.')
            newIdList.removeLast();


        // 5 ~ 6단계
        if (newIdList.size() == 0) {
            newIdList.add('a');
        } else if (newIdList.size() >= 16) {
            newIdList = new LinkedList<>(newIdList.subList(0, 15));
            if (newIdList.getLast() == '.')
                newIdList.removeLast();
        }

        // 7단계
        while(newIdList.size() <= 2) {
            newIdList.add(newIdList.getLast());
        }

        // 결과 리턴
        StringBuilder stringBuilder = new StringBuilder();
        for (char c: newIdList)
            stringBuilder.append(c);

        return stringBuilder.toString();
    }
}