import sys


def distance(vec1: list, vec2: list):
    return (sum([(vec1[i] - vec2[i]) ** 2 for i in range(len(vec1))])) ** 0.5


def kmeans(vectors, n, d, k, iters, eps) -> list:
    clusters = vectors[:k]
    return []


def main():
    args = sys.argv
    file_name = args[3]
    eps = 0.001
    file = open(file_name, "r")
    data = file.readlines()
    vectors = [[float(value) for value in line.strip().split(",")] for line in data]
    n = len(vectors)
    d = len(vectors[0]) if n else 0
    try:
        k = int(args[1])
        if k <= 1 or k >= n:
            raise ValueError
    except Exception as e:
        print("Invalid number of clusters!")
        return
    try:
        iters = int(args[2])
        if iters <= 1 or iters >= 1000:
            raise ValueError
    except Exception as e:
        print("Invalid maximum iteration!")
        return
    print(kmeans(vectors, n, d, k, iters, eps))


if __name__ == "__main__":
    main()
