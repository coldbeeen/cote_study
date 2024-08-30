def solution(n, k, cmd):

    # 이중 연결 리스트 클래스 생성
    class Node:
        def __init__(self, data):
            self.prev = None
            self.data = data
            self.next = None

    # 0 ~ n-1까지의 연결 리스트 생성
    head, prev = None, None
    for i in range(n):
        node = Node(i)
        if prev is None:
            head = node
        else:
            node.prev = prev
            node.prev.next = node
        prev = node

    # k번째 노드로 이동
    node = head
    for _ in range(k):
        node = node.next

    removed_nodes = []  # 삭제된 노드 관리

    # 명령어 수행
    for c in cmd:

        c = c.split()
        action, size = (c[0], int(c[1])) if len(c) >= 2 else (c[0], None)  # action, size를 추출

        if action == 'U':  # 위로(prev로) size만큼 이동
            for _ in range(size):
                node = node.prev

        elif action == 'D':  # 아래로(next로) size만큼 이동
            for _ in range(size):
                node = node.next

        elif action == 'C':  # 현재 노드를 삭제된 노드 리스트에 추가 후, 앞 뒤 노드의 포인터를 적절히 수정해준 뒤, 현재 노드 조정
            removed_nodes.append(node)  #
            if node.prev is not None:
                node.prev.next = node.next
            if node.next is not None:
                node.next.prev = node.prev
            node = node.next if node.next is not None else node.prev

        else:  # 가장 최근에 삭제된 노드를 가져와 앞 뒤의 노드의 포인터를 다시 해당 노드로 수정함
            removed_node = removed_nodes.pop()
            if removed_node.prev is not None:
                removed_node.prev.next = removed_node
            if removed_node.next is not None:
                removed_node.next.prev = removed_node

    # 정답 생성 후 리턴
    answer = ['O' for _ in range(n)]
    for node in removed_nodes:
        answer[node.data] = 'X'

    return ''.join(answer)