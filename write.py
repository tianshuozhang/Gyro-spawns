def ww(h,work="he",folder="0"):
    xlsbpath = r"./datastore/"+folder+"/"
    # work = input("please input you work id:")
    xlsbpath = xlsbpath + work + ".msh"
    file = open(xlsbpath, 'w')
    length_min = 255
    length_max = -255
    for point in h.p:
        length_min = min(point.z, length_min)
        length_max = max(point.z, length_max)
    f0=[]
    for i in range(len(h.f[0])):
        if h.f[0][i].points[0].z != length_min :
            h.f[4].append(h.f[0][i])
        else:
            f0.append(h.f[0][i])
    h.f[0]=f0

    f1=[]
    for i in range(len(h.f[1])):
        if h.f[1][i].points[0].z != length_max:
            h.f[4].append(h.f[1][i])
        else:
            f1.append(h.f[1][i])
    h.f[1]=f1

    def p_solve(p):
        file.write('(0 "team to Fluent File")\n')
        file.write('(0 "Dimension:")\n')
        file.write('(2 3)\n')
        file.write('(10 (0 1 ' + hex(len(p)-1)[2:] + ' 1 3))\n')
        file.write('(10 (1 1 ' + hex(len(p)-1)[2:] + ' 1 3)(\n')
        p_len=len(p)
        for i in range(1,p_len):
            file.write(str(p[i].x)+' '+str(p[i].y)+' '+str(p[i].z)+'\n')
        file.write('))\n')
    def face_solve(f):
        file.write('(0 "Faces:")\n(13(0 1 ' + hex(len(f[0])+len(f[1])+len(f[2])+len(f[3])+len(f[4]))[2:] + ' 0))\n')

        #outlet
        file.write('(13(3 ' + hex(1)[2:] + ' ' + hex(len(f[0]))[2:] + ' 5 0)(\n')
        for i in range(len(f[0])):
            file.write('4 ' + hex(f[0][i].points[0].num)[2:] + ' ' + hex(f[0][i].points[1].num)[2:] + ' ' + hex(
                    f[0][i].points[2].num)[2:] + ' ' + hex(f[0][i].points[3].num)[2:] + ' ' + hex(f[0][i].cells[0].num)[2:] + ' 0\n')
        file.write('))\n')

        #inlet
        file.write('(13(4 ' + hex(1+len(f[0]))[2:] + ' ' + hex(len(f[0]+f[1]))[2:] + ' 4 0)(\n')
        for i in range(len(f[1])):
            file.write('4 ' + hex(f[1][i].points[0].num)[2:] + ' ' + hex(f[1][i].points[1].num)[2:] + ' ' + hex(
                        f[1][i].points[2].num)[2:] + ' ' + hex(f[1][i].points[3].num)[2:] + ' ' + hex(
                        f[1][i].cells[0].num)[2:] + ' 0\n')
        file.write('))\n')
        #wall
        file.write('(13(5 ' + hex(len(f[0])+len(f[1])+1)[2:] + ' ' + hex(len(f[0])+len(f[1])+len(f[2]))[2:] + ' 3 0)(\n')
        for i in range(len(f[2])):
            file.write('4 ' + hex(f[2][i].points[0].num)[2:] + ' ' + hex(f[2][i].points[1].num)[2:] + ' ' + hex(
                f[2][i].points[2].num)[2:] + ' ' + hex(f[2][i].points[3].num)[2:] + ' ' + hex(
                f[2][i].cells[0].num)[2:] + ' 0\n')
        file.write('))\n')
        #interior
        file.write('(13(7 ' + hex(len(f[0])+len(f[1])+len(f[2])+1)[2:] + ' ' + hex(len(f[0])+len(f[1])+len(f[2])+len(f[3]))[2:] + ' 2 0)(\n')
        for i in range(len(f[3])):
            if len(f[3][i].cells)==2:
                file.write('4 ' + hex(f[3][i].points[0].num)[2:] + ' ' + hex(f[3][i].points[1].num)[2:] + ' ' + hex(
                    f[3][i].points[2].num)[2:] + ' ' + hex(f[3][i].points[3].num)[2:] + ' ' + hex(
                    f[3][i].cells[0].num)[2:] + ' '+hex(
                    f[3][i].cells[1].num)[2:]+'\n')
            else:
                file.write('4 ' + hex(f[3][i].points[0].num)[2:] + ' ' + hex(f[3][i].points[1].num)[2:] + ' ' + hex(
                    f[3][i].points[2].num)[2:] + ' ' + hex(f[3][i].points[3].num)[2:] + ' ' + hex(
                    f[3][i].cells[0].num)[2:] + '  0\n')
        file.write('))\n')
        #new
        file.write('(13(8 ' + hex(len(f[0]) + len(f[1]) + len(f[2]) + 1+len(f[3]))[2:] + ' ' + hex(
            len(f[0]) + len(f[1]) + len(f[2]) + len(f[3])+len(f[4]))[2:] + ' 2 0)(\n')
        for face in f[4]:
            file.write('4 ' + hex(face.points[0].num)[2:] + ' ' + hex(face.points[1].num)[2:] + ' ' + hex(
                face.points[2].num)[2:] + ' ' + hex(face.points[3].num)[2:] + ' ' + hex(
                face.cells[0].num)[2:] + '  0\n')
        file.write('))\n')

    def cell_solve(c):
        file.write('(0 "Cells:")\n(12 (0 1 ' + hex(len(c)-1)[2:] + ' 0))\n(12 (2 1 ' + hex(len(c)-1)[2:] + ' 1 4))\n')
    def zone_solve():
        file.write('(0 "Zones:")\n(45 (2 fluid fluid)())\n(45 (3 pressure-outlet pressure_outlet.3)())\n(45 (4 velocity-inlet velocity_inlet.2)())\n(45 (5 wall wall.1)())\n(45 (7 interior interior)())\n(45 (8 interface interface.4)())')
    p_solve(h.p)
    face_solve(h.f)
    cell_solve(h.c)
    zone_solve()