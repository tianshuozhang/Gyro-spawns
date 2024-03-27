'''
    在 Cube 类的构造函数中，我们遍历所有的面并检查它们是否已经在 face_to_cube 字典中。如果面还没有与任何立方体对象关联，
    则我们创建一个新的键并将其关联的值设置为一个空列表。然后，我们将当前立方体对象添加到该面的立方体列表中。
'''
'''
这些函数使用
Python
中的特殊方法
`__eq__()`
来检测两个对象是否相等。在
`Point`
类中，我们检查另一个对象是否是
`Point`
类型，并比较三个坐标值是否都相等。在
`Face`
类中，我们使用集合来比较两个面是否包含相同的四个点。在
`Cube`
类中，我们使用集合来比较两个立方体是否包含相同的六个面。

'''
class Point:
    def __init__(self, x, y, z,num):
        self.x = x
        self.y = y
        self.z = z
        self.faces = []
        self.cells = []
        self.num=num
    def add_face(self, face):
        if face not in self.faces:
            self.faces.append(face)

    def add_cell(self, cell):
        if cell not in self.cells:
            self.cells.append(cell)

    def __str__(self):
        # print(self.x+self.y+self.z)
        # print(self.faces.num)
        # print(self.cells.num)
       return ("x: {}; y: {}; z: {}".format(self.x, self.y, self.z))

    def __eq__(self, other):
        #if isinstance(other, Point):
            return abs(self.x -other.x)<0.00001 and abs(self.y -other.y)<0.00001 and self.z == other.z
        #return False

class Face:
    def __init__(self, p1, p2, p3,p4,num,type):
        self.points = [p1, p2, p3,p4]
        self.cells = []
        self.num=num
        p1.add_face(self)
        p2.add_face(self)
        p3.add_face(self)
        p4.add_face(self)
        self.type=type
    def __str__(self):
        return ("Point1: x: {}; y: {}; z: {}\nPoint2: x: {}; y: {}; z: {}\nPoint3: x: {}; y: {}; z: {}\nPoint4: x: {}; y: {}; z: {}\n".
                format(self.points[0].x,self.points[0].y,self.points[0].z,
                       self.points[1].x,self.points[1].y,self.points[1].z,
                       self.points[2].x,self.points[2].y,self.points[2].z,
                       self.points[3].x,self.points[3].y,self.points[3].z,))

    def add_cell(self, cell):
        # if cell not in self.cells:
            self.cells.append(cell)

    def __eq__(self, other):
        if isinstance(other, Face):
            for i in range(4):
                flag = 0
                for j in range(4):
                    if self.points[i]==other.points[j]:
                        flag=1
                        break
                    j=j+1
                if flag==0:
                    return False
                i=i+1
        return True

class Cell:
    def __init__(self,num):
        self.points = []
        self.faces = []
        self.num=num
    def add_point(self, point):
        if point not in self.points:
            self.points.append(point)
        point.add_cell(self)
        return point

    def add_face(self, face):
        if face not in self.faces:
            self.faces.append(face)
            for point in face.points:
                self.add_point(point)
        face.add_cell(self)

