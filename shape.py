# time to migrate this to java...
import math
import random
from coordinate import coordinate

def pentagon():
    pent = shape()
    pentagon = [ coordinate(.3,.5),coordinate(.4,.7),coordinate(.6,.7),coordinate(.7,.5),coordinate(.5,.35) ]
    for cd in pentagon:
        pent.add(cd.x,cd.y)
    return pent

def square():
    sq = shape()
    square = [ coordinate(.3,.3), coordinate(.3,.7), coordinate(.7,.7), coordinate(.7,.3) ]
    for cd in square:
        sq.add(cd.x,cd.y)
    
    return sq

def rnd(size):
    cds = shape()
    j = 0
    while j < size:
        cds.add(random.random(), random.random())
        j += 1

    return cds

def median(x,y,x2,y2):
    return [(x+x2)/2, (y+y2)/2]

# degrees = tan^-1 (rise/run)
def get_angle(c1, c2):
    rise    = max(c1.y, c2.y) - min(c1.y, c2.y)
    run     = max(c1.x, c2.x) - min(c1.x, c2.x)

    try:
        dg = math.degrees(math.atan(rise/run))
    except:
        dg = 0.0

    return dg

"""
NAME    : relative_angles
DESC    :
    Accepts a coordinate and a shape. Iterates through all coordinates in
    the shape, calling the get_angle function with each shape.coordinates
    member and the coordinate passed as a parameter. All angles are appended
    to an array and returned.
RTRN    : angles[]
PARM    : coordinate object, shape object
"""
def relative_angles(coord, shape):
    angles = []
    for cd in shape.coordinates:
        angles.append(get_angle(coord, cd))

    return angles

class shape:
    coordinates = []

    # inits coordinates array
    def __init__(self):
        self.coordinates = []

    """
    NAME    :
        add
    DESC    :
        Appends the shape instance's coordinates array with a new coordinate object
        init'd with the x and y coordinates passed.
    RTRN    : //
    PARM    : self,x,y
    """
    def add(self, x, y):
        self.coordinates.append(coordinate(x,y))

    def pop(self, index=-1):
        if index == -1:
            return self.coordinates.pop()
        else:
            return self.coordinates.pop(index)

    """
    HOLY HECK LET'S TALK

    So I want to make a wireframe. How will I go about doing that? How would I
    go about ensuring that I'm taking the median of the correct coordinates, to
    form an undeviated shape (i.e. no crossing perimeter lines)? The best way,
    I concluded, was to sort the shape's coordinates member by the order in which
    you want those perimeter outlines to be drawn. This ensures that our shape
    is unmolested, however requires some diligence when making a shape.

    NAME    : get_medians
    DESC    :
        This function is not exhaustive, however its current functionality is
        sufficient. Let me explain.

        When drawing the perimeter for a shape object, it's unclear how we establish
        which coordinates to draw lines between. If we do it without a check of any
        kind, we risk making a messy web instead of a nice cohesive shape. We could
        collect every median between every point, and thus have a cohesive shape with
        a web wireframe in the middle; but we may not want this. Thus we don't iterate
        over the coordinates a kajillion times to get this.

        Instead, we go over each coordinate and calculate the median coordinate using
        it and the next coordinate in the array. If it is the last element of the array,
        we calculate the median of the final array element and the first array element.

        Each is appended to the medians array and is returned as a shape object.
    RTRN    : shape
    PARM    : self
    """
    def get_medians(self):
        if len(self.coordinates) < 2:
            return False
        medians = []
        i = 0
        while i < len(self.coordinates):
            if i == len(self.coordinates) - 1:
                j = 0
            else: j = i + 1

            x1=self.coordinates[i].x
            y1=self.coordinates[i].y
            x2=self.coordinates[j].x
            y2=self.coordinates[j].y

            if median( x1,y1,x2,y2 ) not in medians:
                medians.append(median( x1,y1,x2,y2 ))
            i+=1

        rtrn = shape()
        # convert array of arrays to array of coordinate objs
        # bad fix, don't care
        for m in medians:
            rtrn.add(m[0], m[1])
        return rtrn

    """
    NAME    : get_median
    DESC    :
        Gets the median coordinate given all the x,y entries in
        the shape instance.
    RTRN    : coordinate
    PARM    : self
    """
    def get_median(self):
        x = 0
        y = 0
        for cd in self.coordinates:
            x += cd.x
            y += cd.y

        x = x / len(self.coordinates)
        y = y / len(self.coordinates)

        return coordinate(x,y)

    # checks if x is the median of the max and min x values, checks if y is the median of max and min y values
    def is_max_median(self, x, y):
        if (self.get_smallest_y() + self.get_largest_y()) / 2 == y and ( self.get_largest_x() + self.get_smallest_x() ) / 2 == x:
            return True
        return False

    # generates the median value of all x coordinates
    def median_x(self):
        x_sum = 0
        for c in self.coordinates:
            x_sum += c.x

        return x_sum / len(self.coordinates)
    
    # generates the median value of all y coordinates
    def median_y(self):
        y_sum = 0
        for c in self.coordinates:
            y_sum += c.y

        return y_sum / len(self.coordinates)

    # checks if a coordinate passed is the median x coordinate, within a given range
    def is_median(self, x, y, range = 0):
        if self.median_x() - range <= x <= self.median_x() + range and self.median_y() - range <= y <= self.median_y() + range:
            return True
        return False

    # checks if a coordinate is within the max and min xy ranges
    def is_within_range(self, x, y, inclusive=True):
        if self.get_smallest_y() <= y <= self.get_largest_y() and self.get_smallest_x() < x < self.get_largest_x():
            return True
        return False

    # checks if a coordinate exists within the shape
    def is_coordinate(self, x, y, range = 0):
        for cd in self.coordinates:
            if (cd.x - range) <= x <= (cd.x + range) and (cd.y - range) <= y <= (cd.y + range):
                return True
        
        return False

    def get_largest_x(self):
        lrg = 0.0
        for cd in self.coordinates:
            if cd.x > lrg:
                lrg = cd.x

        return lrg

    def get_largest_y(self):
        lrg = 0.0
        for cd in self.coordinates:
            if cd.y > lrg:
                lrg = cd.y

        return lrg

    def get_smallest_x(self):
        sml = 1.0
        for cd in self.coordinates:
            if cd.x < sml:
                sml = cd.x

        return sml

    def get_smallest_y(self):
        sml = 1.0
        for cd in self.coordinates:
            if cd.y < sml:
                sml = cd.y

        return sml