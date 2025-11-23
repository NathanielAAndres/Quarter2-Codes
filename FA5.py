destinations = []
print("Please enter your 5 travel destinations:")
for i in range(5):
    dest = input(f"Destination {i + 1}: ")
    destinations.append(dest)

print("Your travel destinations are:")
for dest in destinations:
    print(dest)

print("Let's update your 2nd and 5th destinations.")

new_dest_2 = input("Enter a new destination for position 2: ")
destinations[1] = new_dest_2
new_dest_5 = input("Enter a new destination for position 5: ")
destinations[4] = new_dest_5

print("Your updated travel destinations are:")
for dest in destinations:
    print(dest)

