def char(a, b):
  new_a = b[:5] + a[5:]
  new_b = a[:5] + b[5:]

  return new_a + ' ' + new_b
print(char('Aditya', 'Rathwa'))