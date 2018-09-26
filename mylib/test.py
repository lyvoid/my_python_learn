def test_y(x):
    for i in range(10):
        yield i * x


if __name__ == "__main__":
    a = test_y(10)
    print(next(a))
    print(next(a))
