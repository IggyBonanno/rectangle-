import math
import sys

def load_coordinates_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            coordinates = []
            for line in lines:
                x, y = map(float, line.strip().split())
                coordinates.append((x, y))
            return coordinates
    except FileNotFoundError:
        print("Datoteka nije pronađena.")
        return None
    except ValueError:
        print("Pogrešan format koordinata u datoteci.")
        return None

def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def is_rectangle(vertices):
    if len(vertices) != 4:
        return False
    
    side_lengths = [distance(vertices[i], vertices[(i + 1) % 4]) for i in range(4)]
    diagonal_lengths = [distance(vertices[i], vertices[(i + 2) % 4]) for i in range(4)]

    side_lengths.sort()
    diagonal_lengths.sort()

    if side_lengths[0] != side_lengths[1] or side_lengths[1] != side_lengths[2] or side_lengths[2] != side_lengths[3]:
        return False

    if diagonal_lengths[0] != diagonal_lengths[1]:
        return False

    if side_lengths[0] >= diagonal_lengths[0]:
        return False

    return True


def is_inside_rectangle(vertices, point):
    min_x = min(vertices[0][0], vertices[1][0], vertices[2][0], vertices[3][0])
    max_x = max(vertices[0][0], vertices[1][0], vertices[2][0], vertices[3][0])
    min_y = min(vertices[0][1], vertices[1][1], vertices[2][1], vertices[3][1])
    max_y = max(vertices[0][1], vertices[1][1], vertices[2][1], vertices[3][1])
    
    return min_x <= point[0] <= max_x and min_y <= point[1] <= max_y


def main():
    coordinates = [(1.5, 2.5), (4.5, 2.5), (4.5, 5.5), (1.5, 5.5)]  # Provided coordinates
    A, B, C = coordinates[:-1]  # First three coordinates
    X = coordinates[-1]  # Last coordinate

    print("Coordinates of point X:", X)

    diagonal_lengths = [distance(A, C), distance(B, X)]
    print("Diagonal lengths:", diagonal_lengths)

    if not is_rectangle([A, B, C]):
        print("These points cannot form a rectangle.")
        return

    if is_inside_rectangle([A, B, C], X):
        print("Point X is inside the rectangle ABC.")
    else:
        print("Point X is not inside the rectangle ABC.")

if __name__ == "__main__":
    main()