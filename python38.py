def get_valid_input(prompt, options):
    my_string = input(prompt)
    my_options = ', '.join(options)
    while  my_string.lower() not in options:
        print(f"Invalid input. Choose from: {my_options}")
        my_string = input(prompt)

    return my_string.lower()


answer = get_valid_input("Continue pipeline? ", ["yes", "no"])
print(f"Answer: {answer}")
region = get_valid_input("Select region: ", ["north", "south", "east"])
print(f"Region: {region}")
'''
Write a function called get_valid_input that keeps asking the user
for input until they enter a valid value.

The function should:
1. Accept a prompt string and a list of valid options
2. Keep looping until the user enters one of the valid options
3. Be case insensitive - "YES", "yes", "Yes" should all be accepted
4. Print an error message each time invalid input is entered
5. Return the cleaned input in lowercase

Then call it twice:
answer = get_valid_input("Continue pipeline? ", ["yes", "no"])
region = get_valid_input("Select region: ", ["north", "south", "east"])

And print the results:
print(f"Answer: {answer}")
print(f"Region: {region}")

Example interaction:
Continue pipeline? maybe
Invalid input. Choose from: yes, no
Continue pipeline? YES
Answer: yes
Select region: west
Invalid input. Choose from: north, south, east
Select region: North
Region: north
'''