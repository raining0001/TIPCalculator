from Body import Main

print("Welcome to the Tip Calculator")

calculator = Main()
calculator.ask_user()

if calculator.tip_yn.upper() == 'N':
    calculator.no_tip()
    print(f"Each person should pay: {round(calculator.final_total, 2)}")
else:
    calculator.tip_calculator()
    print(f"Each person should pay: {round(calculator.total_f, 2)}")