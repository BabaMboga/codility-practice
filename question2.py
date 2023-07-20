def Solution(A):
    max_list = []
    for _ in A:
        
        if _% 4 == 0:
            max_list.append(_)
        
    maximum = max(max_list)
    return maximum

if __name__ == "__main__":
    A = [-6, -91, 1011, -100, 84, -22, 0, 1, 473]
    print(Solution(A))