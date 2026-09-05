
gen_index = 0
user_input = ""

def generate_multiplication_table(user_input):
    num = int(user_input)
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

if gen_index == 0:
        user_input = input("Enter a number to generate its times table (press 'q' to quit): ")
        if user_input != "q":
            generate_multiplication_table(user_input)
            gen_index =+ 1

if gen_index != 0:
     while True:
        user_input = input("Enter another number to generate its times table (press 'q' to quit): ")

        if user_input == "q":
            print("Program stopped.")
            break
        else:
             generate_multiplication_table(user_input)
             gen_index =+ 1

