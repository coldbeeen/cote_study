# 원래 코드가 너무 지저분하고 별로여서 클래스화 해봄
class ID:
    def __init__(self, input_id):
        self.input_id = input_id

    def lev1(self):
        self.input_id = self.input_id.lower()

    def lev2(self):
        result = ""
        for i in self.input_id:
            if "a" <= i <= "z" or "0" <= i <= "9" or i == "-" or i == "_" or i == ".":
                result += i
        self.input_id = result

    def lev3(self):
        result = ""
        is_continuous = False
        for i in self.input_id:
            if i == ".":
                if is_continuous:
                    continue
                else:
                    result += i
                    is_continuous = True
            else:
                is_continuous = False
                result += i

        self.input_id = result

    def lev4(self):
        result = ""
        for i in range(len(self.input_id)):
            if i == 0 or i == len(self.input_id) - 1:
                if self.input_id[i] == ".":
                    continue
            result += self.input_id[i]
        self.input_id = result

    def lev5(self):
        if not self.input_id:
            self.input_id = "a"

    def lev6(self):
        if len(self.input_id) >= 16:
            result = self.input_id[:15]
            if result[-1] == ".":
                result = result[:14]
            self.input_id = result

    def lev7(self):
        result = self.input_id
        if len(self.input_id) <= 2:
            while len(result) != 3:
                result += self.input_id[-1]
            self.input_id = result

    def recommend(self):
        for i in range(1, 8):
            getattr(self, f"lev{i}")()
        return self.input_id


def solution(new_id):
    answer = ID(new_id)
    return answer.recommend()

# # 밑에는 원래 코드
# def solution(new_id):
#     answer = ""

#     def lev1(input_id):
#         return input_id.lower()

#     def lev2(input_id):
#         result = ""
#         for i in input_id:
#             if "a" <= i <= "z" or "0" <= i <= "9" or i == "-" or i == "_" or i == ".":
#                 result += i
#         return result

#     def lev3(input_id):
#         result = ""
#         is_continuous = False
#         for i in input_id:
#             if i == ".":
#                 if is_continuous:
#                     continue
#                 else:
#                     result += i
#                     is_continuous = True
#             else:
#                 is_continuous = False
#                 result += i

#         return result

#     def lev4(input_id):
#         result = ""
#         for i in range(len(input_id)):
#             if i == 0 or i == len(input_id) - 1:
#                 if input_id[i] == ".":
#                     continue
#             result += input_id[i]
#         return result

#     def lev5(input_id):
#         return input_id if input_id else "a"

#     def lev6(input_id):
#         if len(input_id) >= 16:
#             result = input_id[:15]
#             if result[-1] == ".":
#                 result = result[:14]
#             return result
#         return input_id

#     def lev7(input_id):
#         result = input_id
#         if len(input_id) <= 2:
#             while len(result) != 3:
#                 result += input_id[-1]
#             return result
#         else:
#             return input_id

#     print(new_id)
#     print("-----")
#     answer = lev1(new_id)
#     print(answer)
#     answer = lev2(answer)
#     print(answer)
#     answer = lev3(answer)
#     print(answer)
#     answer = lev4(answer)
#     print(answer)
#     answer = lev5(answer)
#     print(answer)
#     answer = lev6(answer)
#     print(answer)
#     answer = lev7(answer)
#     print(answer)
#     return answer
