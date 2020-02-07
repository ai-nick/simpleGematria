# Gets user input and converts to lowercase
user_input = input("Please enter a word or phrase you would like to find the simple english gematria of: ")
word = user_input.lower()

alphabet_conspiracy_string = "abcdefghijklmnopqrstuvwxyz"

total = 0
for n in word:

	numerical_value = alphabet_conspiracy_string.find(n)

	if n != -1:
		total += numerical_value
		print("{} = {}".format(n, numerical_value)) 
	
	if n == 'a':
		total.append(1)
		print('A = 1')

print(f"Your word's simple english gematria sums to: {total}")

	
	



