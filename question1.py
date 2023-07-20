# def solution(S):
#     n = len(S)
#     m = len(S[0])


# # picks first word in list
#     for i in range(n):
#         #picks second word in list ensuring a word is not repeated
#         for j in range(i+1, n):
#             # similar_position = {}
#             for k in range(m):
#                 if S[i][k] == S[j][k]:
#                     # similar_position.insert(k)
#                     return [i,j,k]


#     return []


def solution(S):
    #Check if there is any pair of strings that share a common letter.
    for i in range(len(S)):
        for j in range(i + 1, len(S)):
            for k in range(len(S[0])):
                if S[i][k] == S[j][k]:
                    return[i, j, k]
                    
    #If no pair of the strings exists, return an empty arrary.
    return[]


#for testing purposes 

if __name__ == "__main__":
    S = ["abc", "bca", "dbe"]
    print(solution(S))
