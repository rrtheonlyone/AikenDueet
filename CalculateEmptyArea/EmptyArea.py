import math

def circle(sha, rad):

    epsilon = 1e-5

    def calculate_triangle(centre, p0, p1):
        # Calculate area of a triangle
        theta0 = math.atan2(p0[1] - centre[1], p0[0] - centre[0])
        theta1 = math.atan2(p1[1] - centre[1], p1[0] - centre[0])

        side0 = math.hypot(p0[0] - centre[0], p0[1] - centre[1])
        side1 = math.hypot(p1[0] - centre[0], p1[1] - centre[1])

        theta = theta1 - theta0
        if theta > math.pi:
            theta -= 2 * math.pi
        elif theta < -math.pi:
            theta += 2 * math.pi

        # value = side0 * side1 * math.sin(theta) / 2
        # print("Centre = " + str(centre) + ", radius = " + str(radius) + ", p0 = " + str(p0) +
        #       ", p1 = " + str(p1) + ", theta = " + str(theta))
        # print("Tri-Area = " + str(value))
        return side0 * side1 * math.sin(theta) / 2


    def calculate_sector(centre, radius, p0, p1):
        # Calculate area of a sector
        theta0 = math.atan2(p0[1] - centre[1], p0[0] - centre[0])
        theta1 = math.atan2(p1[1] - centre[1], p1[0] - centre[0])

        theta = theta1 - theta0
        if theta > math.pi:
            theta -= 2 * math.pi
        elif theta < -math.pi:
            theta += 2 * math.pi

        # value = radius ** 2 * theta / 2
        # print("Centre = " + str(centre) + ", radius = " + str(radius) + ", p0 = " + str(p0) +
        #       ", p1 = " + str(p1) + ", theta = " + str(theta))
        # print("Sec-Area = " + str(value))
        return radius ** 2 * theta / 2


    # Scan input
    xR = con[0]
    yR = con[1]
    width = condim[0]
    height = condim[1]
    xC = float(sha[0])
    yC = float(sha[1])
    radius = float(rad)

    # Create array of rectangle coordinates
    rectangle = [(xR, yR),
                 (xR + width, yR),
                 (xR + width, yR + height),
                 (xR, yR + height)]

    ans = 0.0

    for i in range(4):
        j = (i + 1) % 4

        # print("\nChecking from points: " + str(rectangle[i]) + " " + str(rectangle[j]))

        # Prepare values
        # The line of the rectangle is l1 + t * lM
        xI = rectangle[i][0]
        yI = rectangle[i][1]

        xJ = rectangle[j][0]
        yJ = rectangle[j][1]

        xM = xJ - xI
        yM = yJ - yI

        # Construct quadratic equation
        A = xM ** 2 + yM ** 2
        B = 2 * xM * (xI - xC) + 2 * yM * (yI - yC)
        C = (xI - xC) ** 2 + (yI - yC) ** 2 - radius ** 2

        if math.fabs(math.hypot(xI - xC, yI - yC) - radius) < epsilon:
            # The point li is on the circle. Will it go in, or out?
            theta0 = math.atan2(yC - yI, xC - xI)
            theta1 = math.atan2(yJ - yI, xJ - xI)

            theta = theta1 - theta0
            if theta > math.pi:
                theta -= 2 * math.pi
            elif theta < -math.pi:
                theta += 2 * math.pi

            points = [rectangle[i]]
            if -math.pi/2 < theta < math.pi/2:
                # It goes in!
                in_circle = True
            else:
                # Wait no!
                in_circle = False
        elif math.hypot(xI - xC, yI - yC) < radius - epsilon:
            # The point li is in the circle
            in_circle = True
            points = [rectangle[i]]
        else:
            # The point li is outside the circle
            in_circle = False

            # Find the point between li and the centre
            theta = math.atan2(yI - yC, xI - xC)
            points = [(xC + radius * math.cos(theta), yC + radius * math.sin(theta))]

        if B ** 2 - 4 * A * C > 0:
            # Solve for t
            t1 = (-B + math.sqrt(B ** 2 - 4 * A * C)) / (2 * A)
            t2 = (-B - math.sqrt(B ** 2 - 4 * A * C)) / (2 * A)

            t_values = sorted([t1, t2])

            # Insert new intersection points into points[].
            for t in t_values:
                if 0 < t < 1:
                    points.append((xI + t * xM, yI + t * yM))

        if math.hypot(xJ - xC, yJ - yC) < radius + epsilon:
            # The point lj is in the circle
            points.append(rectangle[j])
        else:
            # The point lj is outside the circle
            # Find the point between lj and the centre
            theta = math.atan2(yJ - yC, xJ - xC)
            points.append((xC + radius * math.cos(theta), yC + radius * math.sin(theta)))

        # print("Points = " + str(points))

        for p0, p1 in zip(points, points[1:]):
            # Calculate area
            if in_circle:
                ans += calculate_triangle((xC, yC), p0, p1)
            else:
                ans += calculate_sector((xC, yC), radius, p0, p1)

            # Flip parity
            in_circle ^= True

    print("{0:.2f}".format(math.fabs(width * height - math.fabs(ans))))

def rectangle(sha, shadim):
    left = max (con[0], sha[0])
    right = min (con[0] + condim[0], sha[0] + shadim[0])
    bottom = max (con[1], sha[1])
    top = min (con[1] + condim[1], sha[1] + shadim[1])
    
    if (left < right and bottom < top):
        return condim[0] * condim[1] - (right-left)*(top-bottom)
    return 0

ph = raw_input()
con = [int(x) for x in ph.split()] #Container Coordinates
ph = raw_input()
condim = [int(x) for x in ph.split()] #Height and width

t = raw_input() #Is the shape of child container

if t == "square":
    ph = raw_input()
    c = [int(x) for x in ph.split()] #Container Coordinates
    ph = int(raw_input())
    cp = [ph, ph] #Height and width
    print rectangle(c, cp)

elif t == "rectangle":
    ph = raw_input()
    c = [int(x) for x in ph.split()] #Container Coordinates
    ph = raw_input()
    cp = [int(x) for x in ph.split()] #Height and width
    print rectangle(c, cp)

elif t == "circle":
    ph = raw_input()
    c = [int(x) for x in ph.split()] #Container Coordinates
    ph = int(raw_input())
    print circle(c, ph)

else:
    print "Non type"

