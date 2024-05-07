f = open('in.txt','r')
str=f.readlines()
f.close()
N=int(str[0])
matrix=str[1::]
matrix=[line.rstrip() for line in matrix]
matrix=[line.split() for line in matrix]
for i in range(N):
    for j in range(N):
        matrix[i][j]=int(matrix[i][j])
def color(otv,i,matrix):
    flag=1
    ok=[1,1]
    for color in range(2):
        for shade in range(len(otv[color])):
            if matrix[otv[color][shade]][i]==1:
                ok[color]=0
    if ok[0]==0 and ok[1]==0:
        flag=0
    else:
        otv[ok.index(1)].append(i)
    if flag==0:
        return "N"
    else:
        return otv
def stac(matrix):
    stack=[0]
    otv=[[0],[]]
    lenn=N
    for poz1 in range(lenn):
        if len(stack)==0:
            break
        ok=1
        dell=1
        temp=stack[-1]
        while ok==1:
            for j in range(N):
                if matrix[temp][j]==1 and j not in stack and j not in otv[0] and j not in otv[1]:
                    stack.append(j)
                    temp=j
                    otv=color(otv,temp,matrix)
                    if otv=="N":
                        return "N"
                    break
                elif j==N-1:
                    if len(stack)==1:
                        temp=stack[0]
                        if temp not in otv[0] and temp not in otv[1]:
                            otv=color(otv,temp,matrix)
                        stack.pop()
                        for y in range(N):
                            if y not in otv[0] and y not in otv[1]:
                                stack.append(y)
                    ok=0
        for poz in range(len(stack)-1,0,-1):
            for j in range(N):
                if((matrix[stack[poz]][j]==1 and j not in otv[0]) and (matrix[stack[poz]][j]==1 and j not in otv[1])):
                    dell=0
            if dell==1:
                stack.pop()
                lenn-=1
                poz-=1
            if dell==0:
                break
    otv[0]=sorted(otv[0])
    otv[1]=sorted(otv[1])
    st="Y\n"
    for col in range(2):
        for shade in range(len(otv[col])):
            otv[col][shade]+=1
            st+=(otv[col][shade]).__str__()+" "
        st+="\n"
    return st
out = open("out.txt", "a+")
out.write(stac(matrix))
out.close()
# 6
# 0 1 0 1 0 1
# 1 0 1 0 0 0
# 0 1 0 0 0 1
# 1 0 0 0 0 0
# 0 0 0 0 0 0
# 1 0 1 0 0 0