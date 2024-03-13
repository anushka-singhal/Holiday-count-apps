def count_holidays(N, festival_days):
    holidays = 0
    for i in range(1, 31):
        if i % 7 == 6 or i % 7 == 0:  
            holidays += 1
        elif i in festival_days:
            holidays += 1
    return holidays

def main():
    T = int(input().strip())
    for _ in range(T):
        N = int(input().strip())
        festival_days = list(map(int, input().strip().split()))
        print(count_holidays(N, festival_days))

if __name__ == "__main__":
    main()
