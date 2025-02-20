import math as mt

vector_number = int(input("Enter the number of points: "))

points = []
for i in range(vector_number):
    x = int(input(f" Enter the value x{i+1}: "))
    y = int(input(f" Enter the value y{i+1}: "))
    points.append((x,y))

def euclideanDistance(point1, point2):
    d = mt.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)
    return d

distances = []
for i in range(len(points)):
    for j in range(i+1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

min_distance = min(distances)

print(f"Distances : {distances}")
print(f"Minimum distance: {min_distance:.2f}")