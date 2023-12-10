target = int(input())
for number in range(1, target + 1):
  if number % 3 == 0 or number % 5 == 0:    # had to change from an 'or' comparison to an 'and'
    print("FizzBuzz")
  elif number % 3 == 0:     # had to change to an elif
    print("Fizz")
  elif number % 5 == 0:     # had to change to an elif
    print("Buzz")
  else:
    print(number)   # had to remove the [] from around number so it didn print as a list of 1 item
