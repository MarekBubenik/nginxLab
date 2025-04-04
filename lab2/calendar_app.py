import calendar

def main():
    cal_year = int(input("Please enter any year: "))
    cal_month = int(input("Please enter any month number: "))
    print(calendar.month(cal_year, cal_month))

if __name__ == "__main__":
    main()
