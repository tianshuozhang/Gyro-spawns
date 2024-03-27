import os
import math
from cube import *
class round_table():
    def __init__(self,beishu,r,re,h ,beta,x=0,y=0,z=0,work="台",folder="0"):
        xlsbpath = r"./datastore/"+folder+"/"
        print(xlsbpath)
        # work = input("please input you work id:")
        r=r*beishu
        re=re*beishu
        h=h*4
        xlsbpath = xlsbpath + work + ".msh"
        file = open(xlsbpath, 'w')
        # r = int(input('圆柱下底面半径：'))*beishu
        # re = int(input('圆柱上底面半径： '))*beishu
        # h = int(input('圆柱高度：'))

        down = False
        if (h < 0):
            h = -h
            down = True
            r1=r
            r=re
            re=r1
        alpha = float(re-r)/h
        # 环向分隔数目，beta由输入决定，a是在每个方向上的分段，便于内部正方形的划分
        # beta = int(input('环向分隔(最好是4的倍数）：'))
        # x=int(input("基准x坐标: "))
        # y=int(input("基准y坐标: "))

        a = int(beta / 4)
        self.p=[]
        f1=[]
        f2=[]
        f3=[]
        f4=[]
        f5=[]
        self.f=[f1,f2,f3,f4,f5]
        self.c = []
        cell_num = a * a * h + (r - 1) * beta * h
        for k in range(0, cell_num + 1):
            self.c.append(Cell(k))
            k=k+1

        def transfer(angle, height):
            n = int(angle / a)
            m = angle % a
            if n == 0:
                return hex(angle + 1 + height * ((a + 1) * (a + 1) + (r - 1) * beta))[2:]
            if n == 1:
                return hex((1 + angle % a) * (a + 1) + height * ((a + 1) * (a + 1) + (r - 1) * beta))[2:]
            if n == 2:
                return hex((a + 1) * (a + 1) - m + height * ((a + 1) * (1 + a) + (r - 1) * beta))[2:]
            if n == 3:
                return hex(1 + (a + 1) * (a - m) + height * ((a + 1) * (a + 1) + (r - 1) * beta))[2:]

        def cell_tran(angle, height):
            n = int(angle / a)
            m = angle % a
            if n == 0:
                return hex(angle + 1 + height * (a * a + (r - 1) * beta))[2:]
            if n == 1:
                return hex((1 + m) * a + height * (a * a + (r - 1) * beta))[2:]
            if n == 2:
                return hex(a * a + -m + height * (a * a + (r - 1) * beta))[2:]
            if n == 3:
                return hex(1 + a * (a - m - 1) + height * (a * a + (r - 1) * beta))[2:]

        def is_cell(n):
            if n in range(1, a * a * h + (r - 1) * beta * h + 1):
                return hex(n)[2:]
            else:
                return '0'



        def out_solve():
            file.write('(13(3 ' + hex(1)[2:] + ' ' + hex(a * a + (r - 1) * beta)[2:] + ' 5 0)(\n')
            face_num=1
            for height in range(1):
                for i in range(a):
                    for l in range(a):
                        face_a = Face(self.p[height * (a + 1) * (a + 1) + (i + 1) * (a + 1) + l + 1],self.p[height * (a + 1) * (a + 1) + (i + 1) * (a + 1) + l + 2],self.p[height * (a + 1) * (a + 1) + i * (a + 1) + l + 2],self.p[height * (a + 1) * (a + 1) + i * (a + 1) + l + 1],face_num,5)
                        face_num = 1+face_num
                        self.f[0].append(face_a)
                        self.c[height * a * a + i * a + l + 1].add_face(self.f[0][-1])

                        file.write('4 ' + hex(height * (a + 1) * (a + 1) + (i + 1) * (a + 1) + l + 1)[2:] + ' ' + hex(
                            height * (a + 1) * (a + 1) + (i + 1) * (a + 1) + l + 2)[2:] + ' ' + hex(
                            height * (a + 1) * (a + 1) + i * (a + 1) + l + 2)[2:] + ' ' + hex(
                            height * (a + 1) * (a + 1) + i * (a + 1) + l + 1)[2:] + ' ' + is_cell(
                            height * a * a + i * a + l + 1) + ' 0\n')

                        l = l + 1
                    i = i + 1
                    l = 0
                if r > 1:
                    for angle in range(beta):
                        radius = 2

                        face_a = Face(self.p[int(transfer((angle + 1) % beta, height), 16)], self.p[
                            height * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (a + 1) + (angle + 1) % beta * (
                                    r - 1) + radius - 1], self.p[
                                          height * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (a + 1) + angle * (
                                                  r - 1) + radius - 1], self.p[int(transfer(angle, height), 16)],face_num,5)
                        face_num = 1 + face_num
                        self.c[height * (a * a + beta * (r - 1)) + a * a + angle * (r - 1) + radius - 1].add_face(face_a)
                        self.f[0].append(face_a)


                        file.write('4 ' + transfer((angle + 1) % beta, height) + ' ' + hex(
                            height * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (a + 1) + (angle + 1) % beta * (
                                    r - 1) + radius - 1)[2:] + ' ' + hex(
                            height * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (a + 1) + angle * (
                                    r - 1) + radius - 1)[
                                                                     2:] + ' ' + transfer(angle,
                                                                                          height) + ' ' + is_cell(
                            height * (a * a + beta * (r - 1)) + a * a + angle * (r - 1) + radius - 1) + ' 0\n')

                        for radius in range(3, r + 1):
                            face_a = Face(self.p[height * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (a + 1) + (
                                    angle + 1) % beta * (r - 1) + radius - 2], self.p[
                                              height * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (a + 1) + (
                                                      angle + 1) % beta * (r - 1) + radius - 1], self.p[
                                              height * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (
                                                          a + 1) + angle * (
                                                      r - 1) + radius - 1], self.p[
                                              height * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (
                                                          a + 1) + angle * (
                                                      r - 1) + radius - 2],face_num,5)
                            face_num = 1 + face_num
                            self.c[height * (a * a + beta * (r - 1)) + a * a + angle * (r - 1) + radius - 1].add_face(face_a)
                            self.f[0].append(face_a)


                            file.write('4 ' + hex(
                                height * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (a + 1) + (
                                            angle + 1) % beta * (
                                        r - 1) + radius - 2)[2:] + ' ' + hex(
                                height * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (a + 1) + (
                                            angle + 1) % beta * (
                                        r - 1) + radius - 1)[2:] + ' ' + hex(
                                height * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (a + 1) + angle * (
                                        r - 1) + radius - 1)[2:] + ' ' + hex(
                                height * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (a + 1) + angle * (
                                        r - 1) + radius - 2)[2:] + ' ' + is_cell(
                                height * (a * a + beta * (r - 1)) + a * a + angle * (r - 1) + radius - 1) + ' 0\n')

                            radius = radius + 1
                        angle = angle + 1
                        radius = 0
                height = height + 1
                angle = 0
            file.write('))\n')


        def in_solve():
            file.write(
                '(13(4 ' + hex(a * a + (r - 1) * beta + 1)[2:] + ' ' + hex(a * a * 2 + (r - 1) * beta * 2)[
                                                                       2:] + ' 4 0)(\n')
            face_num=a * a + (r - 1) * beta + 1
            for height in range(h, h + 1):
                for i in range(a):
                    for l in range(a):
                        face_a = Face(self.p[height * ((a + 1) * (a + 1) + (r - 1) * beta) + i * (a + 1) + l + 1],
                                      self.p[(height * ((a + 1) * (a + 1) + (r - 1) * beta) + i * (a + 1) + l + 2)], self.p[(
                                    height * ((a + 1) * (a + 1) + (r - 1) * beta) + (i + 1) * (a + 1) + l + 2)],
                                      self.p[(height * ((a + 1) * (a + 1) + (r - 1) * beta) + (i + 1) * (a + 1) + l + 1)],face_num,4)
                        face_num = 1 + face_num
                        self.c[(height - 1) * (a * a + beta * (r - 1)) + i * a + l + 1].add_face(face_a)

                        self.f[1].append(face_a)

                        file.write(
                            '4 ' + hex(height * ((a + 1) * (a + 1) + (r - 1) * beta) + i * (a + 1) + l + 1)[
                                   2:] + ' ' + hex(
                                height * ((a + 1) * (a + 1) + (r - 1) * beta) + i * (a + 1) + l + 2)[2:] + ' ' + hex(
                                height * ((a + 1) * (a + 1) + (r - 1) * beta) + (i + 1) * (a + 1) + l + 2)[
                                                                                                                 2:] + ' ' + hex(
                                height * ((a + 1) * (a + 1) + (r - 1) * beta) + (i + 1) * (a + 1) + l + 1)[
                                                                                                                             2:] + ' ' + is_cell(
                                (height - 1) * (a * a + beta * (r - 1)) + i * a + l + 1) + ' 0\n')

                        l = l + 1
                    i = i + 1
                    l = 0
                if r > 1:
                    for angle in range(beta):
                        radius = 2

                        face_a = Face(self.p[int(transfer(angle, height), 16)], self.p[
                            height * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (a + 1) + angle * (
                                    r - 1) + radius - 1],
                                      self.p[height * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (a + 1) + (
                                              angle + 1) % beta * (r - 1) + radius - 1],
                                      self.p[int(transfer((angle + 1) % beta, height), 16)],face_num,4)
                        face_num = 1 + face_num
                        self.c[(height - 1) * (a * a + beta * (r - 1)) + a * a + angle * (r - 1) + radius - 1].add_face(
                            face_a)

                        self.f[1].append(face_a)

                        file.write('4 ' + transfer(angle, height) + ' ' + hex(
                            height * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (a + 1) + angle * (
                                    r - 1) + radius - 1)[
                                                                          2:] + ' ' + hex(
                            height * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (a + 1) + (angle + 1) % beta * (
                                    r - 1) + radius - 1)[2:] + ' ' + transfer((angle + 1) % beta,
                                                                              height) + ' ' + is_cell(
                            (height - 1) * (a * a + beta * (r - 1)) + a * a + angle * (r - 1) + radius - 1) + ' 0\n')

                        for radius in range(3, r + 1):
                            face_a = Face(self.p[height * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (a + 1) + (
                                    angle + 1) % beta * (r - 1) + radius - 1], self.p[
                                              height * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (a + 1) + (
                                                      angle + 1) % beta * (r - 1) + radius - 2], self.p[
                                              height * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (
                                                          a + 1) + angle * (
                                                      r - 1) + radius - 2], self.p[
                                              height * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (
                                                          a + 1) + angle * (
                                                      r - 1) + radius - 1],face_num,4)
                            face_num = 1 + face_num
                            self.c[(height - 1) * (a * a + beta * (r - 1)) + a * a + angle * (r - 1) + radius - 1].add_face(
                                face_a)
                            self.f[1].append(face_a)

                            file.write('4 ' + hex(
                                height * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (a + 1) + (
                                            angle + 1) % beta * (
                                        r - 1) + radius - 1)[2:] + ' ' + hex(
                                height * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (a + 1) + (
                                            angle + 1) % beta * (
                                        r - 1) + radius - 2)[2:] + ' ' + hex(
                                height * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (a + 1) + angle * (
                                        r - 1) + radius - 2)[2:] + ' ' + hex(
                                height * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (a + 1) + angle * (
                                        r - 1) + radius - 1)[2:] + ' ' + is_cell(
                                (height - 1) * (a * a + beta * (r - 1)) + a * a + angle * (
                                            r - 1) + radius - 1) + ' 0\n')

                            radius = radius + 1
                        angle = angle + 1
                        radius = 0
                height = height + 1
                angle = 0
            file.write('))\n')

        def wall_solve():
            face_num=a * a * 2 + (r - 1) * beta * 2 + 1
            file.write(
                '(13(5 ' + hex(a * a * 2 + (r - 1) * beta * 2 + 1)[2:] + ' ' + hex(
                    a * a * 2 + (r - 1) * beta * 2 + beta * h)[
                                                                           2:] + ' 3 0)(\n')
            for height in range(h):
                for angle in range(beta):
                    face_a = Face(self.p[height * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (a + 1) + angle * (r - 1) + r - 1],
                                  self.p[height * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (a + 1) + (angle + 1) % beta * (r - 1) + r - 1],
                                  self.p[(height + 1) * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (a + 1) + (angle + 1) % beta * (r - 1) + r - 1],
                                  self.p[(height + 1) * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (a + 1) + angle * (r - 1) + r - 1],face_num,3)
                    face_num=face_num+1
                    self.c[height * (a * a + beta * (r - 1)) + a * a + angle * (r - 1) + r - 1].add_face(face_a)
                    self.f[2].append(face_a)


                    file.write(
                        '4 ' + hex(
                            height * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (a + 1) + angle * (
                                        r - 1) + r - 1)[
                               2:] + ' ' + hex(
                            height * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (a + 1) + (angle + 1) % beta * (
                                    r - 1) + r - 1)[2:] + ' ' + hex(
                            (height + 1) * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (a + 1) + (
                                        angle + 1) % beta * (
                                    r - 1) + r - 1)[2:] + ' ' + hex(
                            (height + 1) * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (a + 1) + angle * (
                                    r - 1) + r - 1)[
                                                                2:] + ' ' + is_cell(
                            height * (a * a + beta * (r - 1)) + a * a + angle * (r - 1) + r - 1) + ' 0\n')
            file.write('))\n')

        def default_solve():
            face_num=a * a * 2 + (r - 1) * beta * 2 + beta * h + 1
            file.write('(13(7 ' + hex(a * a * 2 + (r - 1) * beta * 2 + beta * h + 1)[2:] + ' ' + hex(
                (a * a + (r - 1) * beta) * (h + 1) + beta * h * (r - 1) * 2 + h * a * (a + 1) * 2)[2:] + ' 2 0)(\n')
            for height in range(1, h):
                for i in range(a):
                    for l in range(a):
                        face_a = Face(self.p[height * ((a + 1) * (a + 1) + (r - 1) * beta) + (i + 1) * (a + 1) + l + 1],
                                      self.p[height * ((a + 1) * (a + 1) + (r - 1) * beta) + (i + 1) * (a + 1) + l + 2],
                                      self.p[height * ((a + 1) * (a + 1) + (r - 1) * beta) + i * (a + 1) + l + 2],
                                      self.p[height * ((a + 1) * (a + 1) + (r - 1) * beta) + i * (a + 1) + l + 1],face_num,2)
                        face_num = 1 + face_num
                        self.c[height * (a * a + (r - 1) * beta) + i * a + l + 1].add_face(face_a)

                        self.c[(height - 1) * (a * a + (r - 1) * beta) + i * a + l + 1].add_face(face_a)

                        self.f[3].append(face_a)


                        file.write(
                            '4 ' + hex(height * ((a + 1) * (a + 1) + (r - 1) * beta) + (i + 1) * (a + 1) + l + 1)[
                                   2:] + ' ' + hex(
                                height * ((a + 1) * (a + 1) + (r - 1) * beta) + (i + 1) * (a + 1) + l + 2)[
                                               2:] + ' ' + hex(
                                height * ((a + 1) * (a + 1) + (r - 1) * beta) + i * (a + 1) + l + 2)[2:] + ' ' + hex(
                                height * ((a + 1) * (a + 1) + (r - 1) * beta) + i * (a + 1) + l + 1)[
                                                                                                                 2:] + ' ' + is_cell(
                                height * (a * a + (r - 1) * beta) + i * a + l + 1) + ' ' + is_cell(
                                (height - 1) * (a * a + (r - 1) * beta) + i * a + l + 1) + '\n')

                        l = l + 1
                    i = i + 1
                    l = 0
                if r > 1:
                    for angle in range(beta):
                        face_a = Face(self.p[int(transfer((angle + 1) % beta, height), 16)], self.p[
                            height * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (a + 1) + (angle + 1) % beta * (
                                    r - 1) + 1], self.p[
                                          height * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (a + 1) + angle * (
                                                  r - 1) + 1], self.p[int(transfer(angle, height), 16)],face_num,2)
                        face_num = 1 + face_num
                        self.c[height * (a * a + beta * (r - 1)) + a * a + angle * (r - 1) + 1].add_face(face_a)
                        self.c[(height - 1) * (a * a + beta * (r - 1)) + a * a + angle * (r - 1) + 1].add_face(face_a)
                        self.f[3].append(face_a)

                        file.write('4 ' + transfer((angle + 1) % beta, height) + ' ' + hex(
                            height * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (a + 1) + (angle + 1) % beta * (
                                    r - 1) + 1)[2:] + ' ' + hex(
                            height * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (a + 1) + angle * (r - 1) + 1)[
                                                            2:] + ' ' + transfer(angle, height) + ' ' +
                                   is_cell(
                                       height * (a * a + beta * (r - 1)) + a * a + angle * (r - 1) + 1) + ' ' + is_cell(
                            (height - 1) * (a * a + beta * (r - 1)) + a * a + angle * (r - 1) + 1) + '\n')

                        for radius in range(3, r + 1):
                            face_a = Face(self.p[height * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (a + 1) + (
                                    angle + 1) % beta * (r - 1) + radius - 2],
                                          self.p[height * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (a + 1) + (
                                                  angle + 1) % beta * (r - 1) + radius - 1],
                                          self.p[height * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (
                                                      a + 1) + angle * (
                                                    r - 1) + radius - 1],
                                          self.p[height * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (
                                                      a + 1) + angle * (
                                                    r - 1) + radius - 2],face_num,2)
                            face_num = 1 + face_num
                            self.c[height * (a * a + beta * (r - 1)) + a * a + angle * (r - 1) + radius - 1].add_face(face_a)
                            self.c[(height - 1) * (a * a + beta * (r - 1)) + a * a + angle * (r - 1) + radius - 1].add_face(
                                face_a)
                            self.f[3].append(face_a)

                            file.write('4 ' + hex(
                                height * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (a + 1) + (
                                            angle + 1) % beta * (
                                        r - 1) + radius - 2)[2:] + ' ' + hex(
                                height * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (a + 1) + (
                                            angle + 1) % beta * (
                                        r - 1) + radius - 1)[2:] + ' ' + hex(
                                height * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (a + 1) + angle * (
                                        r - 1) + radius - 1)[
                                                                         2:] + ' ' + hex(
                                height * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (a + 1) + angle * (
                                        r - 1) + radius - 2)[
                                                                                     2:] + ' ' + is_cell(
                                height * (a * a + beta * (r - 1)) + a * a + angle * (
                                            r - 1) + radius - 1) + ' ' + is_cell(
                                (height - 1) * (a * a + beta * (r - 1)) + a * a + angle * (r - 1) + radius - 1) + '\n')
                            radius = radius + 1
                        angle = angle + 1
                        radius = 0
                height = height + 1
                angle = 0
            height = 0
            for height in range(h):
                for i in range(1, a):
                    for j in range(a):
                        face_a = Face(self.p[height * ((a + 1) * (a + 1) + (r - 1) * beta) + i * (a + 1) + j + 1],
                                      self.p[height * ((a + 1) * (a + 1) + (r - 1) * beta) + i * (a + 1) + j + 2],
                                      self.p[(height + 1) * ((a + 1) * (a + 1) + (r - 1) * beta) + i * (a + 1) + j + 2],
                                      self.p[(height + 1) * ((a + 1) * (a + 1) + (r - 1) * beta) + i * (a + 1) + j + 1],face_num,2)
                        face_num = 1 + face_num
                        self.c[height * (a * a + (r - 1) * beta) + i * a + j + 1].add_face(face_a)
                        self.c[height * (a * a + (r - 1) * beta) + (i - 1) * a + j + 1].add_face(face_a)
                        self.f[3].append(face_a)

                        file.write(
                            '4 ' + hex(height * ((a + 1) * (a + 1) + (r - 1) * beta) + i * (a + 1) + j + 1)[
                                   2:] + ' ' + hex(
                                height * ((a + 1) * (a + 1) + (r - 1) * beta) + i * (a + 1) + j + 2)[2:] + ' ' + hex(
                                (height + 1) * ((a + 1) * (a + 1) + (r - 1) * beta) + i * (a + 1) + j + 2)[
                                                                                                                 2:] + ' ' + hex(
                                (height + 1) * ((a + 1) * (a + 1) + (r - 1) * beta) + i * (a + 1) + j + 1)[
                                                                                                                             2:] + ' ' + is_cell(
                                height * (a * a + (r - 1) * beta) + i * a + j + 1) + ' ' + is_cell(
                                height * (a * a + (r - 1) * beta) + (i - 1) * a + j + 1) + '\n')
                for j in range(1, a):
                    for i in range(a):
                        face_a = Face(self.p[height * ((a + 1) * (a + 1) + (r - 1) * beta) + i * (a + 1) + j + 1],
                                      self.p[height * ((a + 1) * (a + 1) + (r - 1) * beta) + (i + 1) * (a + 1) + j + 1],
                                      self.p[(height + 1) * ((a + 1) * (a + 1) + (r - 1) * beta) + (i + 1) * (
                                                  a + 1) + j + 1],
                                      self.p[(height + 1) * ((a + 1) * (a + 1) + (r - 1) * beta) + i * (a + 1) + j + 1],face_num,2)
                        self.c[height * (a * a + (r - 1) * beta) + i * a + j].add_face(face_a)
                        self.c[height * (a * a + (r - 1) * beta) + i * a + j + 1].add_face(face_a)
                        self.f[3].append(face_a)

                        file.write(
                            '4 ' + hex(height * ((a + 1) * (a + 1) + (r - 1) * beta) + i * (a + 1) + j + 1)[
                                   2:] + ' ' + hex(
                                height * ((a + 1) * (a + 1) + (r - 1) * beta) + (i + 1) * (a + 1) + j + 1)[
                                               2:] + ' ' + hex(
                                (height + 1) * ((a + 1) * (a + 1) + (r - 1) * beta) + (i + 1) * (a + 1) + j + 1)[
                                                           2:] + ' ' + hex(
                                (height + 1) * ((a + 1) * (a + 1) + (r - 1) * beta) + i * (a + 1) + j + 1)[
                                                                       2:] + ' ' + is_cell(
                                height * (a * a + (r - 1) * beta) + i * a + j) + ' ' + is_cell(
                                height * (a * a + (r - 1) * beta) + i * a + j + 1) + '\n')
                for angle in range(beta):
                    radius = 2

                    face_a = Face(self.p[int(transfer(angle, height), 16)], self.p[int(transfer((angle + 1) % beta, height), 16)],
                                  self.p[int(transfer((angle + 1) % beta, height + 1), 16)],
                                  self.p[int(transfer(angle, height + 1), 16)],face_num,2)
                    face_num = 1 + face_num
                    self.c[int(cell_tran(angle, height), 16)].add_face(face_a)
                    self.c[height * (a * a + beta * (r - 1)) + a * a + angle * (r - 1) + radius - 1].add_face(face_a)
                    self.f[3].append(face_a)

                    file.write(
                        '4 ' + transfer(angle, height) + ' ' + transfer((angle + 1) % beta, height) + ' ' + transfer(
                            (angle + 1) % beta, height + 1) + ' ' + transfer(angle, height + 1) + ' ' + cell_tran(angle,
                                                                                                                  height) + ' ' + is_cell(
                            height * (a * a + beta * (r - 1)) + a * a + angle * (r - 1) + radius - 1) + '\n')

                    for radius in range(2, r):
                        face_a = Face(
                            self.p[height * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (a + 1) + angle * (
                                    r - 1) + radius - 1],
                            self.p[height * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (a + 1) + (angle + 1) % beta * (
                                    r - 1) + radius - 1],
                            self.p[(height + 1) * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (a + 1) + (
                                    angle + 1) % beta * (
                                      r - 1) + radius - 1],
                            self.p[(height + 1) * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (a + 1) + angle * (
                                    r - 1) + radius - 1],face_num,2)
                        face_num = 1 + face_num
                        self.c[height * (a * a + beta * (r - 1)) + a * a + angle * (r - 1) + radius - 1].add_face(face_a)
                        self.c[height * (a * a + beta * (r - 1)) + a * a + angle * (r - 1) + radius].add_face(face_a)
                        self.f[3].append(face_a)

                        file.write('4 ' + hex(
                            height * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (a + 1) + angle * (
                                    r - 1) + radius - 1)[
                                          2:] + ' ' + hex(
                            height * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (a + 1) + (angle + 1) % beta * (
                                    r - 1) + radius - 1)[2:] + ' ' + hex(
                            (height + 1) * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (a + 1) + (
                                        angle + 1) % beta * (
                                    r - 1) + radius - 1)[2:] + ' ' + hex(
                            (height + 1) * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (a + 1) + angle * (
                                    r - 1) + radius - 1)[2:] + ' ' + is_cell(
                            height * (a * a + beta * (r - 1)) + a * a + angle * (r - 1) + radius - 1) + ' ' + is_cell(
                            height * (a * a + beta * (r - 1)) + a * a + angle * (
                                    r - 1) + radius) + '\n')  # file.write('4 ' + hex(height * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (a + 1) + angle * (r - 1) + r - 1)[2:] + ' ' + hex(height * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (a + 1) + (angle + 1) % beta * (r - 1) + r - 1)[2:] + ' ' + hex((height + 1) * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (a + 1) + (angle + 1) % beta * (r - 1) + r - 1)[2:] + ' ' + hex((height + 1) * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (a + 1) + angle * (r - 1) + r - 1)[2:] + ' ' + is_cell(height * (a * a + beta * (r - 1)) + a * a + angle * (r - 1) + r - 1) + ' 0\n')
                        radius = radius + 1

                    radius = 2

                    face_a = Face(
                        self.p[(height * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (a + 1) + angle * (
                                r - 1) + radius - 1)],
                        self.p[int(transfer(angle, height), 16)], self.p[int(transfer(angle, height + 1), 16)], self.p[
                            (height + 1) * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (a + 1) + angle * (
                                    r - 1) + radius - 1],face_num,2)
                    face_num = 1 + face_num
                    self.c[height * (a * a + beta * (r - 1)) + a * a + (angle - 1) % beta * (r - 1) + radius - 1].add_face(
                        face_a)
                    self.c[height * (a * a + beta * (r - 1)) + a * a + angle * (r - 1) + radius - 1].add_face(face_a)
                    self.f[3].append(face_a)

                    file.write('4 ' + hex(
                        (height * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (a + 1) + angle * (
                                    r - 1) + radius - 1))[
                                      2:] + ' ' + transfer(angle, height) + ' ' + transfer(angle,
                                                                                           height + 1) + ' ' + hex(
                        (height + 1) * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (a + 1) + angle * (
                                r - 1) + radius - 1)[
                                                                                                               2:] + ' ' + is_cell(
                        height * (a * a + beta * (r - 1)) + a * a + (angle - 1) % beta * (
                                r - 1) + radius - 1) + ' ' + is_cell(
                        height * (a * a + beta * (r - 1)) + a * a + angle * (r - 1) + radius - 1) + '\n')

                    for radius in range(2, r):
                        face_a = Face(
                            self.p[height * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (a + 1) + angle * (
                                        r - 1) + radius],
                            self.p[height * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (a + 1) + angle * (
                                    r - 1) + radius - 1],
                            self.p[(height + 1) * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (a + 1) + angle * (
                                    r - 1) + radius - 1], self.p[
                                (height + 1) * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (a + 1) + angle * (
                                        r - 1) + radius],face_num,2)
                        face_num = 1 + face_num
                        self.c[height * (a * a + beta * (r - 1)) + a * a + (angle - 1) % beta * (r - 1) + radius].add_face(
                            face_a)
                        self.c[height * (a * a + beta * (r - 1)) + a * a + angle * (r - 1) + radius].add_face(face_a)
                        self.f[3].append(face_a)

                        file.write('4 ' + hex(
                            height * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (a + 1) + angle * (
                                        r - 1) + radius)[
                                          2:] + ' ' + hex(
                            height * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (a + 1) + angle * (
                                    r - 1) + radius - 1)[
                                                      2:] + ' ' + hex(
                            (height + 1) * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (a + 1) + angle * (
                                    r - 1) + radius - 1)[2:] + ' ' + hex(
                            (height + 1) * ((a + 1) * (a + 1) + (r - 1) * beta) + (a + 1) * (a + 1) + angle * (
                                    r - 1) + radius)[
                                                                     2:] + ' ' + is_cell(
                            height * (a * a + beta * (r - 1)) + a * a + (angle - 1) % beta * (
                                    r - 1) + radius) + ' ' + is_cell(
                            height * (a * a + beta * (r - 1)) + a * a + angle * (r - 1) + radius) + '\n')

                        radius = radius + 1
                    angle = angle + 1
                    radius = 0
                height = height + 1
                angle = 0

            file.write('))\n')
        def p_solve():
            file.write('(0 "team to Fluent File")\n')
            file.write('(0 "Dimension:")\n')
            file.write('(2 3)\n')
            file.write('(10 (0 1 ' + hex(((a + 1) * (a + 1) + (r - 1) * beta) * (h + 1))[2:] + ' 1 3))\n')
            file.write('(10 (1 1 ' + hex(((a + 1) * (a + 1) + (r - 1) * beta) * (h + 1))[2:] + ' 1 3)(\n')
            # 对于每一层，先对内部的正方形进行计数
            p_num = 1
            self.p.append(Point(x, y, z,0))
            for height in range(h + 1 ):
                if not down:
                    r1 = float(height / h) *(re-r)+r
                else:
                    r1 = float((h-height)/ h)*(r-re)+re
                for j in range(a + 1):
                    for l in range(a + 1):
                        point_a = Point((l / a - 0.5)*(r1*0.65)/beishu+x, (j / a - 0.5)*(r1*0.65)/beishu+y, height/4+z,p_num)
                        p_num=p_num+1
                        file.write(str(point_a.x) + ' ' + str(point_a.y) + ' ' + str(point_a.z) + '\n')
                        self.p.append(point_a)
                        l = l + 1
                    j = j + 1
                for angle in range(beta):
                    for radius in range(2, r + 1):
                        if(radius==2):
                            xx=(self.p[int(transfer(angle, height), 16)].x+(radius /r*r1/2+r1/2)* math.cos((angle / beta - 3 / 8) * 2 * math.pi)/beishu+x)/2
                            yy=(self.p[int(transfer(angle, height), 16)].y+(radius /r*r1/2+r1/2)* math.sin((angle / beta - 3 / 8) * 2 * math.pi)/beishu+y)/2
                            point_a=Point(xx,yy,height/4+z,p_num)
                        elif radius==3:
                            xx=(self.p[p_num-1].x+(radius /r*r1/2+r1/2)* math.cos((angle / beta - 3 / 8) * 2 * math.pi)/beishu+x)/2
                            yy=(self.p[p_num-1].y+(radius /r*r1/2+r1/2)* math.sin((angle / beta - 3 / 8) * 2 * math.pi)/beishu+y)/2
                            point_a = Point(xx, yy, height/4 + z, p_num)
                        else:
                            point_a = Point((radius / r * r1 / 2 + r1 / 2) * math.cos(
                                (angle / beta - 3 / 8) * 2 * math.pi) / beishu + x,
                                            (radius / r * r1 / 2 + r1 / 2) * math.sin(
                                                (angle / beta - 3 / 8) * 2 * math.pi) / beishu + y, height/4 + z, p_num)
                        p_num=p_num+1
                        file.write(str(point_a.x) + ' ' + str(point_a.y) + ' ' + str(point_a.z) + '\n')
                        self.p.append(point_a)
                        radius = radius + 1
                    angle = angle + 1
                    radius = 1
                height = height + 1
                angle = 0

            file.write('))\n')

        def face_solve():
            file.write('(0 "Faces:")\n(13(0 1 ' + hex(
                (a * a + (r - 1) * beta) * (h + 1) + beta * h * (r - 1) * 2 + h * a * (a + 1) * 2)[2:] + ' 0))\n')
            out_solve()
            in_solve()
            wall_solve()
            default_solve()

        def cell_solve():
            file.write('(0 "Cells:")\n(12 (0 1 ' + hex(a * a * h + (r - 1) * beta * h)[2:] + ' 0))\n(12 (2 1 ' + hex(
                a * a * h + (r - 1) * beta * h)[2:] + ' 1 4))\n')



        def zone_solve():
            file.write(
                '(0 "Zones:")\n(45 (2 fluid fluid)())\n(45 (3 pressure-outlet pressure_outlet.3)())\n(45 (4 velocity-inlet velocity_inlet.2)())\n(45 (5 wall wall.1)())\n(45 (7 interior default-interior)())')


        def do_it():
            p_solve()
            face_solve()
            cell_solve()
            zone_solve()
            file.close()
            print("point: %d" %(len(self.p)-1))
            print("face: %d" %(len(self.f[0])+len(self.f[1])+len(self.f[2])+len(self.f[3])))
            print("cell: %d" %(len(self.c)-1))

        do_it()






