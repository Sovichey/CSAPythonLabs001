# Application 1
user_input = input("Enter any words: ")
user_input1 = list(user_input)
user_input2 = list(user_input)

user_input1_2 = [None]*(len(user_input1)+len(user_input2))
user_input1_2[::2] = user_input1
user_input1_2[1::2] = user_input2

user_str = ''. join(user_input1_2)
print(user_str)

# Application 2
alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

user_input = input("Enter a range of letters (e.g., a-z):")
start, end = user_input.split("-")
start_letter = alpha.index(start)
end_letter = alpha.index(end)
result_string = alpha[start_letter:end_letter+1]

print(result_string)


