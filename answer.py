# ------------------------ VERSION RECURSIVA ----------------------------- #
def F(n: int) -> int:
  if n >= 0 and n < 12:
    return n
  else:
    return F(n - 4) + F(n - 8) + F(n - 12)

# ------------------------ VERSION RECURSIVA DE COLA ----------------------------- #
def tail_F(n: int) -> int:
  def generator(acc1: int, acc2: int, acc3: int, counter) -> int:
    if counter <= 0:
      return acc1
    else:
      return generator(acc1 + acc2 + acc3, acc1, acc2, counter - 1)
      
  start_value = n % 4

  return generator(start_value + 8, start_value + 4, start_value, (n - 12) / 4 + 1)

# ------------------------ VERSION ITERATIVA ----------------------------- #
def iterative_F(n: int) -> int:
  start = n % 4
  acc1, acc2, acc3 = start + 8, start + 4, start

  i = (n - 12) / 4 + 1
  while i > 0:
    acc1, acc2, acc3 = acc1 + acc2 + acc3, acc1, acc2
    i -= 1

  return acc1

# ------------------------ EJEMPLOS ----------------------------- #

print(F(24))
print(tail_F(24))
print(iterative_F(24))