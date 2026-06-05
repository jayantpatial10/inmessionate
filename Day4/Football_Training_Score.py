def football_report(hours):
    print("Enter the number of hours you trained this week: ")
    hours = int(input())
    if hours < 5:
        print("Beginner")
    elif hours >= 5 and hours <= 10:
        print("Intermediate")
    elif hours > 10:
        print("Advanced")

football_report(0)