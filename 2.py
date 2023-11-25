def main():
    sss = [4, 23, 53, 6, 2, 123, 46]
    for i in range(1, len(sss)):
        for j in range(i, 0, -1):
            if sss[j] < sss[j - 1]:
                sss[j], sss[j - 1] = sss[j - 1], sss[j]
            else:
                break
        print(sss)


if __name__ == "__main__":
    main()
