# biNum = input(put your binary number here)
# list(biNum)
# numaric = 0
# if: biNum[i] for i in range(0 , len(biNum)) = 1  biNum[i] for i in range(0 , len(biNum)) = 0
# 	numaric = numaric + biNum[i]
# else:





# import sys
# import stdio

# # Accept integer n as a command-line argument. Write the binary
# # representation of n to standard output.

# # Limitation: Does not handle negative integers.

# n = int(sys.argv[1])

# # Compute v as the largest power of 2 <= n.
# v = 1
# while v <= n//2:
#     v *= 2

# # Cast out powers of 2 in decreasing order.
# while v > 0:
#     if n < v:
#         stdio.write(0)
#     else:
#         stdio.write(1)
#         n -= v
#     v //= 2

# stdio.writeln()

binary = raw_input('enter a number: ')
decimal = 0
for digit in binary:
    decimal = decimal*2 + int(digit)
print decimal