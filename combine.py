def h_combine(h1,h2):
    def c_combine(c1,c2):#合并体的函数
        len1=len(c1)
        len2=len(c2)
        for i in range(1,len1):
            c1[i].num=c1[i].num+len2-1
            c2.append(c1[i])
            i=i+1

    def p_combine(p1,p2):#合并点的函数
        len1=len(p1)
        len2=len(p2)
        for i in range(1,len1):
            for j in range(1,len2):
                if p1[i] == p2[j]:
                    for cell in p1[i].cells:
                        p2[j].add_cell(cell)
                    p1[i].num=p2[j].num
                    break
                j=j+1
            if j == len2:
                p2.append(p1[i])
            i=i+1
        for i in range(len(p2)):
            p2[i].num=i
            i=i+1



    def f_combine(f1,f2):#合并面的函数

        #上下底面合并
        f11=[]
        for i in range(len(f1[0])):
            # for j in range(len(f2[0])):
            #     if  f1[0][i]==f2[0][j]:
            #         f2[0][j].add_cell(f1[0][i].cells[0])
            #         f2[4].append(f2[0].pop(j))
            #         break
            #     j=j+1
            # if j==len(f2[0]):
            #     f2[1].append(f1[0][i])
            #     break
            for j in range(len(f2[1])):
                if f1[0][i] == f2[1][j]:
                    f2[1][j].add_cell(f1[0][i].cells[0])
                    f2[3].append(f2[1][j])
                    f11.append(f2[1][j])
                    break
                j = j + 1
            if j == len(f2[1]) and j!=0 :
                f2[0].append(f1[0][i])
                # print("f1 : %d in f2" %(i))
            i=i+1
        f13=[]
        for face in f2[1]:
            if face not in f11:
                f13.append(face)
        f2[1]=f13

        f12=[]
        for i in range(len(f1[1])):
            for j in range(len(f2[0])):
                if f1[1][i] == f2[0][j]:
                    f2[0][j].add_cell(f1[1][i].cells[0])
                    f2[3].append(f2[0][j])
                    f12.append(f2[0][j])
                    break
                j=j+1
            if j==len(f2[0]) and j!=0:
                f2[1].append(f1[1][i])
            i=i+1
            # for j in range(len(f2[1])):
            #     if f1[1][i] == f2[1][j]:
            #         f2[1][j].add_cell(f1[1][i].cells[0])
            #         break
            #     j = j + 1
            # if j == len(f2[1]):
            #     f2[1].append(f1[1][i])
            #     break
            i=i+1
        f14=[]
        for face in f2[0]:
            if face not in f12:
                f14.append(face)
        f2[0]=f14
        #wall的合并
        f15=[]
        for i in range(len(f1[2])):
            for j in range(len(f2[2])):
                if f1[2][i] == f2[2][j]:
                    f2[2][j].add_cell(f1[2][i].cells[0])
                    f2[3].append(f2[2].pop(j))
                    break
                j = j + 1
            if j == len(f2[2]):
                for k in range(len(f2[4])):
                    if f1[2][i]==f2[4][k]:
                        f2[4][k].add_cell(f1[2][i].cells[0])
                        f2[3].append(f2[4][k])
                        f15.append(f2[4][k])
                        break
                    k=k+1
                if k == len(f2[4]):
                    f2[2].append(f1[2][i])
            i = i + 1
        f16=[]
        for face in f2[4]:
            if face not in f15:
                f16.append(face)
        f2[4]=f16
        # interface
        for i in range(len(f1[4])):
            for j in range(len(f2[4])):
                if f1[4][i] == f2[4][j]:
                    f2[4][j].add_cell(f1[4][i].cells[0])
                    f2[3].append(f2[2].pop(j))
                    break
                j = j + 1
            if j == len(f2[4]):
                f2[4].append(f1[4][i])
            i = i + 1
        #default的合并
        for i in range(len(f1[3])):
            f2[3].append(f1[3][i])



        #重新对面做一个排序
        resort_num=1
        for i in range(len(f2[0])):
            f2[0][i].num=resort_num
            resort_num=resort_num+1
            i=i+1
        for i in range(len(f2[1])):
            f2[1][i].num=resort_num
            resort_num=resort_num+1
            i=i+1
        for i in range(len(f2[2])):
            f2[2][i].num=resort_num
            resort_num=resort_num+1
            i=i+1
        for i in range(len(f2[3])):
            f2[3][i].num=resort_num
            resort_num=resort_num+1
            i=i+1




    c_combine(h1.c,h2.c)
    p_combine(h1.p,h2.p)
    f_combine(h1.f,h2.f)
    print("point: %d" % (len(h2.p)-1))
    print("face: %d" % (len(h2.f[0]) + len(h2.f[1]) + len(h2.f[2]) + len(h2.f[3])))
    print("outlet face: %d" % (len(h2.f[0])))
    print("inlet face: %d" % ( len(h2.f[1]) ))
    print("wall face: %d" % (len(h2.f[2])))
    print("default face: %d" % (len(h2.f[3])))
    print("cell: %d" % (len(h2.c)-1))
