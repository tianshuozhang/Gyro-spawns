import os
import math
from cube import *
class cirque():
    def __init__(self,beishu,r1 , r2 ,h ,beta,x = 0,y = 0, z=0,work="环",folder="0"):
        #("begin")
        xlsbpath = r"./datastore/"+folder+"/"
        r=min(r1,r2)
        h = h*r
        r1 = r1 * beishu
        r2 = r2 * beishu
        # work = input("please input you work id:")
        xlsbpath = xlsbpath + work + ".msh"
        t=0
        file = open(xlsbpath, 'w')
        # r1 = int(input('圆柱环底面内径：'))*beishu
        # r2 = int(input('圆柱环底面外径：'))*beishu
        # t = 0
        # h = int(input('圆柱高度：')) + t
        # # 环向分隔数目，beta由输入决定，a是在每个方向上的分段，便于内部正方形的划分
        # beta = int(input('环向分隔(最好是4的倍数）：'))
        # x=int(input("基准x坐标: "))
        # y=int(input("基准y坐标: "))
        # z = int(input("基准z坐标: "))

        self.p=[]
        f1=[]
        f2=[]
        f3=[]
        f4=[]
        f5=[]
        self.f=[f1,f2,f3,f4,f5]
        self.c = []
        cell_num = (r2 - r1) * beta * h
        for k in range(0, cell_num + 1):
            self.c.append(Cell(k))
            k=k+1

        



        def out_solve():
            file.write('(13(3 ' + hex(1)[2:] + ' ' + hex((r2 - r1) * beta)[2:] + ' 5 0)(\n')
            face_num=1
            for height in range(1):
                for angle in range(beta):
                    for radius in range(r1, r2 ):
                        face_a = Face(self.p[height * ((r2 - r1+1) * beta)  + (angle + 1) % beta * (r2 - r1+1) + radius - r1+1], self.p[
                                              height * ( (r2 - r1+1) * beta)  + (
                                                      angle + 1) % beta * (r2 - r1+1) + radius -r1+2], self.p[
                                              height * ((r2 - r1+1) * beta) +  angle * (
                                                      r2-r1+1) + radius - r1+2], self.p[
                                              height * (0 + (r2-r1+1) * beta)  + angle * (
                                                      r2-r1+1) + radius - r1+1],face_num,5)
                        face_num = 1 + face_num
                        self.c[height * (0 + beta * (r2-r1)) + 0 + angle * (r2-r1) + radius - r1+1].add_face(face_a)
                        self.f[0].append(face_a)


                        file.write('4 ' + hex(
                                height * (0 + (r2-r1+1) * beta) + 0 + (
                                            angle + 1) % beta * (
                                        r2-r1+1) + radius - r1+1)[2:] + ' ' + hex(
                                height * (0 + (r2-r1+1) * beta) + 0 + (
                                            angle + 1) % beta * (
                                        r2-r1+1) + radius - r1+2)[2:] + ' ' + hex(
                                height * (0 + (r2-r1+1) * beta) + 0 + angle * (
                                        r2-r1+1) + radius - r1+2)[2:] + ' ' + hex(
                                height * (0 + (r2-r1+1) * beta) + 0 + angle * (
                                        r2-r1+1) + radius - r1+1)[2:] + ' ' + hex(
                                height * (0 + beta * (r2-r1)) + 0 + angle * (r2-r1) + radius - r1+1)[2:] + ' 0\n')

                        radius = radius + 1
                    angle = angle + 1
                    radius = r1
                height = height + 1
                angle = 0
            file.write('))\n')


        def in_solve():
            file.write(
                '(13(4 ' + hex( (r2-r1) * beta + 1)[2:] + ' ' + hex( (r2-r1) * beta * 2)[2:] + ' 4 0)(\n')
            face_num=(r2-r1) * beta + 1
            for height in range(h, h + 1):
                for angle in range(beta):
                    for radius in range(r1, r2):
                        face_a = Face(self.p[height * (0 + (r2-r1+1) * beta) + 0 + (
                                    angle + 1) % beta * (r2-r1+1) + radius - r1+2], self.p[
                                              height * (0 + (r2-r1+1) * beta) + 0 + (
                                                      angle + 1) % beta * (r2-r1+1) + radius - r1+1], self.p[
                                              height * (0 + (r2-r1+1) * beta)  + angle * (
                                                      r2-r1+1) + radius - r1+1], self.p[
                                              height * (0 + (r2-r1+1) * beta)  + angle * (
                                                      r2-r1+1) + radius - r1+2],face_num,4)
                        face_num = 1 + face_num
                        self.c[(height - 1) * (0 + beta * (r2-r1)) + 0 + angle * (r2-r1) + radius - r1+1].add_face(
                                face_a)
                        self.f[1].append(face_a)

                        file.write('4 ' + hex(
                                height * (0 + (r2-r1+1) * beta) + 0 + (
                                            angle + 1) % beta * (
                                        r2-r1+1) + radius - r1+2)[2:] + ' ' + hex(
                                height * (0 + (r2-r1+1) * beta) + 0 + (
                                            angle + 1) % beta * (
                                        r2-r1+1) + radius - r1+1)[2:] + ' ' + hex(
                                height * (0 + (r2-r1+1) * beta) + 0 + angle * (
                                        r2-r1+1) + radius - r1+1)[2:] + ' ' + hex(
                                height * (0 + (r2-r1+1) * beta) + 0 + angle * (
                                        r2-r1+1) + radius - r1+2)[2:] + ' ' + hex(
                                (height - 1) * (0 + beta * (r2-r1)) + 0 + angle * (
                                            r2-r1) + radius - r1+1)[2:] + ' 0\n')

                        radius = radius + 1
                    angle = angle + 1
                    radius = r1
                height = height + 1
                angle = 0
            file.write('))\n')

        def wall_solve():
            face_num= (r2-r1) * beta * 2 + 1
            file.write(
                '(13(5 ' + hex((r2-r1) * beta * 2 + 1)[2:] + ' ' + hex(
                    (r2-r1) * beta * 2 + beta * h)[2:] + ' 3 0)(\n')
            for height in range(h):
                for angle in range(beta):#外面的墙
                    face_a = Face(self.p[height * (0 + (r2-r1+1) * beta) + 0 + angle * (r2-r1+1) + r2-r1+1],
                                      self.p[height * (0 + (r2-r1+1) * beta) + 0 + (angle + 1) % beta * (
                                                  r2-r1+1) + r2-r1+1],
                                      self.p[(height + 1) * (0 + (r2-r1+1) * beta) + 0 + (angle + 1) % beta * (
                                                  r2-r1+1) + r2-r1+1],
                                      self.p[(height + 1) * (0 + (r2-r1+1) * beta) + 0 + angle * (r2-r1+1) + r2-r1+1],
                                      face_num, 3)
                    face_num = face_num + 1
                    self.c[height * (0 + beta * (r2 - r1)) + 0 + angle * (r2 - r1) + r2 - r1].add_face(face_a)
                    self.f[2].append(face_a)

                    file.write('4 ' + hex(
                            height * (0 + (r2-r1+1) * beta) + 0 + angle * (
                                    r2 - r1 + 1) + r2-r1+1)[
                                          2:] + ' ' + hex(
                            height * (0 + (r2-r1+1) * beta) + 0 + (angle + 1) % beta * (
                                    r2-r1+1) + r2-r1+1)[2:] + ' ' + hex(
                            (height + 1) * (0 + (r2-r1+1) * beta) + 0 + (
                                    angle + 1) % beta * (
                                    r2-r1+1) + r2-r1+1)[2:] + ' ' + hex(
                            (height + 1) * (0 + (r2-r1+1) * beta) + 0 + angle * (
                                    r2-r1+1) + r2-r1+1)[2:] + ' ' + hex(
                            height * (0 + beta * (r2 - r1)) + 0 + angle * (r2 - r1) + r2 - r1)[2:] + ' 0\n')
            file.write('))\n')
            file.write(#内部的墙
                '(13(8 ' + hex((r2 - r1) * beta * 2 + 1+beta*h)[2:] + ' ' + hex(
                    (r2 - r1) * beta * 2 + beta * h * 2)[2:] + ' 3 0)(\n')
            for height in range(h):
                for angle in range(beta):
                    face_a = Face(self.p[height * (0 + (r2-r1+1) * beta) + 0 + (angle + 1) % beta * (r2-r1+1) + 1],
                                  self.p[height * (0 + (r2-r1+1) * beta) + 0 + angle * (r2-r1+1) + 1],
                                  self.p[(height + 1) * (0 + (r2-r1+1) * beta) + 0 + angle * (r2-r1+1) + 1],
                                  self.p[(height + 1) * (0 + (r2-r1+1) * beta) + 0 + (angle + 1) % beta * (r2-r1+1) + 1],face_num,3)
                    face_num=face_num+1
                    self.c[height * (0 + beta * (r2-r1)) + 0 + angle * (r2-r1) + 1].add_face(face_a)
                    self.f[4].append(face_a)


                    file.write('4 ' + hex(
                            height * (0 + (r2-r1+1) * beta) + 0 + (angle + 1) % beta * (
                                    r2-r1+1) + 1)[2:] + ' ' +  hex(
                            height * (0 + (r2-r1+1) * beta) + 0 + angle * (
                                    r2 - r1 + 1) + 1)[
                               2:]+ ' ' + hex(
                            (height + 1) * (0 + (r2-r1+1) * beta) + 0 + angle * (
                                    r2 - r1 + 1) + 1)[2:] + ' ' + hex(
                            (height + 1) * (0 + (r2-r1+1) * beta) + 0 + (
                                        angle + 1) % beta * (
                                    r2-r1+1) + 1)[2:] + ' ' + hex(
                            height * ( beta * (r2-r1)) + 0 + angle * (r2-r1) + 1)[2:] + ' 0\n')
            file.write('))\n')

        def default_solve():


            face_num=(r2-r1) * beta * 2 + beta * h *2+ 1
            file.write('(13(7 ' + hex(face_num)[2:] + ' ' + hex(
                (r2-r1)*beta*(h + 1)+beta*h*((r2-r1)*2+1))[2:] + ' 2 0)(\n')



            for height in range(1, h):
                for angle in range(beta):
                    for radius in range(r1, r2):
                        face_a = Face(self.p[height * (0 + (r2-r1+1) * beta) + 0 + (
                                    angle + 1) % beta * (r2-r1+1) + radius - r1+1],
                                          self.p[height * (0 + (r2-r1+1) * beta) + 0 + (
                                                  angle + 1) % beta * (r2-r1+1) + radius - r1+2],
                                          self.p[height * (0 + (r2-r1+1) * beta)  + angle * (
                                                    r2-r1+1) + radius - r1+2],
                                          self.p[height * (0 + (r2-r1+1) * beta) + angle * (
                                                    r2-r1+1) + radius - r1+1],face_num,2)
                        face_num = 1 + face_num
                        self.c[height * (0 + beta * (r2-r1)) + 0 + angle * (r2-r1) + radius - r1+1].add_face(face_a)
                        self.c[(height - 1) * (0 + beta * (r2-r1)) + 0 + angle * (r2-r1) + radius - r1+1].add_face(
                                face_a)
                        self.f[3].append(face_a)

                        file.write('4 ' + hex(
                                height * (0 + (r2-r1+1) * beta) + 0 + (
                                            angle + 1) % beta * (
                                        r2-r1+1) + radius - r1+1)[2:] + ' ' + hex(
                                height * (0 + (r2-r1+1) * beta) + 0 + (
                                            angle + 1) % beta * (
                                        r2-r1+1) + radius - r1+2)[2:] + ' ' + hex(
                                height * (0 + (r2-r1+1) * beta) + 0 + angle * (
                                        r2-r1+1) + radius - r1+2)[2:] + ' ' + hex(
                                height * ( (r2-r1+1) * beta) + angle * (
                                        r2-r1+1) + radius - r1+1)[2:] + ' ' + hex(
                                height * (0 + beta * (r2-r1)) + 0 + angle * (
                                            r2-r1) + radius - r1+1)[2:] + ' ' + hex(
                                (height - 1) * (0 + beta * (r2-r1)) + 0 + angle * (r2-r1) + radius - r1+1)[2:] + '\n')
                        radius = radius + 1
                    angle = angle + 1
                    radius = r1
                height = height + 1
                angle = 0
            height = 0
            for height in range(h):

                for angle in range(beta):

                    for radius in range(r1, r2-1):
                        face_a = Face(
                            self.p[height * ( (r2-r1+1) * beta) +  angle * (
                                    r2-r1+1) + radius - r1+2],
                            self.p[height * ( (r2-r1+1) * beta) + (angle + 1) % beta * (
                                    r2-r1+1) + radius - r1+2],
                            self.p[(height + 1) * (0 + (r2-r1+1) * beta) + 0 + (
                                    angle + 1) % beta * (
                                      r2-r1+1) + radius - r1+2],
                            self.p[(height + 1) * (0 + (r2-r1+1) * beta) + 0 + angle * (
                                    r2-r1+1) + radius - r1+2],face_num,2)
                        face_num = 1 + face_num
                        self.c[height * (0 + beta * (r2-r1)) +  angle * (r2-r1) + radius - r1+1].add_face(face_a)
                        self.c[height * (0 + beta * (r2-r1)) +  angle * (r2-r1) + radius - r1+2].add_face(face_a)
                        self.f[3].append(face_a)

                        file.write('4 ' + hex(
                            height * ((r2-r1+1) * beta) +  angle * (
                                    r2-r1+1) + radius - r1+2)[
                                          2:] + ' ' + hex(
                            height * ((r2-r1+1) * beta) + (angle + 1) % beta * (
                                    r2-r1+1) + radius - r1+2)[2:] + ' ' + hex(
                            (height + 1) * ((r2-r1+1) * beta) + (
                                        angle + 1) % beta * (
                                    r2-r1+1) + radius - r1+2)[2:] + ' ' + hex(
                            (height + 1) * (0 + (r2-r1+1) * beta) + 0 + angle * (
                                    r2-r1+1) + radius - r1+2)[2:] + ' ' + hex(
                            height * (beta * (r2-r1)) + angle * (r2-r1) + radius - r1+1)[2:] + ' ' + hex(
                            height * (beta * (r2-r1)) + angle * (r2-r1) + radius - r1+2)[2:] + '\n')  # file.write('4 ' + hex(height * (0 + (r2-r1) * beta) + 0 + angle * (r2-r1) + r2-r1)[2:] + ' ' + hex(height * (0 + (r2-r1) * beta) + 0 + (angle + 1) % beta * (r2-r1) + r2-r1)[2:] + ' ' + hex((height + 1) * (0 + (r2-r1) * beta) + 0 + (angle + 1) % beta * (r2-r1) + r2-r1)[2:] + ' ' + hex((height + 1) * (0 + (r2-r1) * beta) + 0 + angle * (r2-r1) + r2-r1)[2:] + ' ' + hex(height * (0 + beta * (r2-r1)) + 0 + angle * (r2-r1) + r2-r1) + ' 0\n')
                        radius = radius + 1




                    for radius in range(r1, r2):
                        face_a = Face(
                            self.p[height * (0 + (r2-r1+1) * beta) + 0 + angle * (
                                        r2-r1+1) + radius-r1+2],
                            self.p[height * (0 + (r2-r1+1) * beta) + 0 + angle * (
                                    r2-r1+1) + radius - r1+1],
                            self.p[(height + 1) * (0 + (r2-r1+1) * beta) + 0 + angle * (
                                    r2 - r1 + 1) + radius - r1+1], self.p[
                                (height + 1) * (0 + (r2-r1+1) * beta) + 0 + angle * (
                                        r2 - r1 + 1) + radius-r1+2],face_num,2)
                        face_num = 1 + face_num
                        self.c[height * (0 + beta * (r2-r1)) + 0 + (angle - 1) % beta * (r2-r1) + radius-r1+1].add_face(
                            face_a)
                        self.c[height * (0 + beta * (r2-r1)) + 0 + angle * (r2-r1) + radius-r1+1].add_face(face_a)
                        self.f[3].append(face_a)

                        file.write('4 ' + hex(
                            height * (0 + (r2-r1+1) * beta) + 0 + angle * (
                                        r2-r1+1) + radius-r1+2)[
                                          2:] + ' ' + hex(
                            height * (0 + (r2-r1+1) * beta) + 0 + angle * (
                                    r2-r1+1) + radius - r1+1)[
                                                      2:] + ' ' + hex(
                            (height + 1) * (0 + (r2-r1+1) * beta) + 0 + angle * (
                                    r2 - r1 + 1) + radius - r1+1)[2:] + ' ' + hex(
                            (height + 1) * (0 + (r2-r1+1) * beta) + 0 + angle * (
                                    r2-r1+1) + radius-r1+2)[
                                                                     2:] + ' ' + hex(
                            height * (0 + beta * (r2-r1)) + 0 + (angle - 1) % beta * (
                                    r2-r1) + radius-r1+1)[2:] + ' ' + hex(
                            height * (0 + beta * (r2-r1)) + 0 + angle * (r2-r1) + radius-r1+1)[2:] + '\n')

                        radius = radius + 1
                    angle = angle + 1
                    radius = r1
                height = height + 1
                angle = 0

            file.write('))\n')
        def p_solve():
            file.write('(0 "team to Fluent File")\n')
            file.write('(0 "Dimension:")\n')
            file.write('(2 3)\n')
            file.write('(10 (0 1 ' + hex((r2-r1+1) * beta * (h + 1))[2:] + ' 1 3))\n')
            file.write('(10 (1 1 ' + hex((r2-r1+1) * beta * (h + 1))[2:] + ' 1 3)(\n')
            # 对于每一层，先对内部的正方形进行计数
            p_num = 1
            self.p.append(Point(x, y, z,0))
            for height in range(h + 1 - t):
                if height*2<h:
                    hh=math.log(1+height/h/0.6*2)/math.log(1+1/0.6)*h/2
                else :
                    hh=h-math.log(1+(h-height)/h/0.6*2)/math.log(1+1/0.6)*h/2
                for angle in range(beta):
                    for radius in range(r1, r2 + 1):
                        point_a = Point(radius * math.cos((angle / beta - 3 / 8) * 2 * math.pi)/beishu+x,
                                        radius * math.sin((angle / beta - 3 / 8) * 2 * math.pi)/beishu+y, hh/r+z,p_num)
                        p_num=p_num+1
                        file.write(str(point_a.x) + ' ' + str(point_a.y) + ' ' + str(point_a.z) + '\n')
                        self.p.append(point_a)
                        radius = radius + 1
                    angle = angle + 1
                    radius = r1
                height = height + 1
                angle = 0
            for height in range(h + 1 - t, h + 1):
                for angle in range(beta):
                    for radius in range(r1, r2 + 1):
                        point_a = Point(radius * math.cos((angle / beta - 3 / 8) * 2 * math.pi) * math.pow(
                            1 - (height - h + t) * (height - h + t) / t / t, 0.5)+x,
                                        radius * math.sin((angle / beta - 3 / 8) * 2 * math.pi) * math.pow(
                                            1 - (height - h + t) * (height - h + t) / t / t, 0.5)+y, height+z,p_num)
                        p_num=p_num+1
                        file.write(str(point_a.x) + ' ' + str(point_a.y) + ' ' + str(point_a.z) + '\n')
                        self.p.append(point_a)
                        radius = radius + 1
                    angle = angle + 1
                    radius = r1
                height = height + 1
                angle = 0
            file.write('))\n')

        def face_solve():
            file.write('(0 "Faces:")\n(13(0 1 ' + hex(
                (r2-r1) * beta * (h + 1) + beta * h *((r2-r1) * 2+1))[2:] + ' 0))\n')
            out_solve()
            in_solve()
            wall_solve()
            default_solve()

        def cell_solve():
            file.write('(0 "Cells:")\n(12 (0 1 ' + hex((r2-r1) * beta * h)[2:] + ' 0))\n(12 (2 1 ' + hex(
                0 * h + (r2-r1) * beta * h)[2:] + ' 1 4))\n')



        def zone_solve():
            file.write(
                '(0 "Zones:")\n(45 (2 fluid fluid)())\n(45 (3 pressure-outlet pressure_outlet.3)())\n(45 (4 velocity-inlet velocity_inlet.2)())\n(45 (5 wall wall.1)())\n(45 (7 interior default-interior)())\n(45 (8 interface interface.4)())')


        def do_it():
            p_solve()
            face_solve()
            cell_solve()
            zone_solve()
            file.close()
            print("point: %d" %(len(self.p)-1))
            print("face: %d" %(len(self.f[0])+len(self.f[1])+len(self.f[2])+len(self.f[3])+len(self.f[4])))
            print("cell: %d" %(len(self.c)-1))

        do_it()


