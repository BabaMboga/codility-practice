def Solution(S):
    # n = len(S)
    
    return S.replace("?","<")
  
    

if __name__ == "__main__":
    S = "<><??>>"
    print(Solution(S))