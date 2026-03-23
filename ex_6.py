from solution import Point

p = Point((3,-7))
print(p)
a = Point()
print(a)
print(a.get_x())
print(p.get_y())
c = Point((-2, 4))
print(p.distance(c))
d = c.sum(p)
print(d)
