nric = input('Enter an NRIC number: ')

# Type your code below
nric = nric.upper()
check = 0
checknum = 0
check_char = "a"
weights = [2,7,6,5,4,3,2]
if nric[0] in ["S", "T", "F", "G"]:

  if nric[1:-1].isdigit():

    if len(nric[8:]) == 1 and nric[-1].isalpha():

      check = 1
      for digit in range(1,8):
        checknum += (int(nric[digit]) * weights[digit-1])
        

      if nric[0] in ["T", "G"]:
        checknum += 4
      remainder = checknum % 11
      if nric[0] in ["S", "T"]:
        char_table = "J  Z  I  H  G  F  E  D  C  B  A".split("  ")
        check_char = char_table[remainder]
      elif nric[0] in ["F", "G"]:
        char_table = "X  W  U  T  R  Q  P  N  M  L  K".split("  ")
        check_char = char_table[remainder]
      if nric[-1] == check_char:
        check = 1
      else:
        check = 0
else:
  check += 0

if check == 1:
  print("NRIC is valid.")
elif check == 0:
  print("NRIC is invalid.")
