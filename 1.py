def main():
    sas = [4, 23, 53, 6, 2, 123, 46]
    n = len(sas)
    for i in range(0, n - 1):
        for j in range(0, n - 1):
            if sas[j] > sas[j + 1]:
                sys = sas[j]
                sas[j] = sas[j + 1]
                sas[j + 1] = sys
        print(sas)


if __name__ == "__main__":
    main()
