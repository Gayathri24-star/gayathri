def calculate_distance(x1,x2,y1,y2):
    """
calculate the distance between two points(x1,y1) and(x2,y2)
 calculate the compound interest.
    :param x1:x coordinate of the first point(float or int).
    :param y1:y coordinate of the first point(float or int).
    :param x2:x coordinate of the second point(float or int).
    :param y2:y coordinate of the second point(float or int).
    :return:The distance between two points(float).
    """
    distance=math.sqrt((x2-x1)**2+(y2-y1)**2)
# Input values
x1=float(input("Enter x-coordinate of the first point:"))
y1=float(input("Enter y-coordinate of the first point:"))
x2=float(input("Enter x-coordinate of the second point:"))
y2=float(input("Enter y-coordinate of the second point:"))



# Calculate compound interest
distance=calculate_distance(x1,x2,y1,y2)

# Output the results
print(f"The distance between the points({x1},{y1},{x2},{y2}) is:{distance:.2f}")
