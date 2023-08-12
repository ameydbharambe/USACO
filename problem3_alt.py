import sys


def cost(h, f):
    o = 0
    for i in range(n - 1):
        if h[i] > f:
            sub = min(h[i], h[i + 1]) - f
            h[i] -= sub
            h[i + 1] -= sub
            o += sub * 2
    for i in range(n - 1):
        if h[i] != h[i + 1]:
            return float("inf")
    return o


def exe():
    global n
    n = int(input())
    h = list(map(int, input().split()))
    mn = float("inf")
    ans = float("inf")
    for i in h:
        mn = min(mn, i)
    for f in range(mn + 1):
        ans = min(ans, cost(h, f))
    return -1 if ans == float("inf") else ans


def main():
    sys.stdin.readline()
    for line in sys.stdin:
        print(exe())

if __name__ == "__main__":
    main()
