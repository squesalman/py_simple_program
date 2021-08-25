while True:
    check_hit = input("Hit or Stand?")
    if check_hit[0].capitalize() == 'H' or check_hit[0].capitalize() == 'S':
      break
    else:
      print('Pls Enter correct input')