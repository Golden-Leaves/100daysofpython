def calculate_percentage_difference(day1, day2):
    try:
        difference = ((day2 - day1) / abs(day1)) * 100
        if difference > 0:
            return f"Rise of {difference:.2f}%"
        elif difference < 0:
            return f"Fall of {abs(difference):.2f}%"
        else:
            return "No change (0%)"
    except ZeroDivisionError:
        return "Input a valid number, division by zero is not allowed."

if __name__ == "__main__":
    print(calculate_percentage_difference(50, 100))  # Expected: Rise of 100.00%
    print(calculate_percentage_difference(12.52, 67.86))  # Expected: Rise of 441.92%
    print(calculate_percentage_difference(67.86, 12.52))  # Expected: Fall of 81.55%