while True:
    check_hit = input("Hit or Stand?")
    if check_hit[0].capitalize() == 'H' or check_hit[0].capitalize() == 'S':
      print(check_hit[0].capitalize())
      break
    else:
      print('Pls Enter correct input')