def matrixMult(n, A, B):
    final = [[0] * n for x in range(n)]
    for i in range (n):
        for j in range (n):
            for k in range(n):
                final[i][j] += A[i][k] * B[k][j]
    return final


def main():
    n1 = 2
    A1 = [[2,7],[3,5]]
    B1 = [[8, -4],[6,6]]
    final1 = matrixMult(n1,A1,B1)
    print("This is the multiplication product of matricies A1 and B1: ")
    for row in final1:
        print(row)

    n2 = 3
    A2 = [[1,0,2],[3,-2,5],[6,2,-3]]
    B2 = [[.3,.25,.1],[.4,.8,0],[-.5,.75,.6]]
    final2 = matrixMult(n2, A2, B2)
    print("This is the nultiplication product of the matricies A2 and B2: ")
    for row in final2:
        print(row)

main()
    
