
PARTNER_0_NAME = "Krste" #TODO: Change to Partner 0's name
""" If y is less than or equal to 1, return "pushed"
	otherwise, return y * y """
def zero_func(y):
	# TODO: Partner 0 completes

PARTNER_1_NAME = "Randy" #TODO: Change to Partner 1's name
""" If y is less than or equal to 1, return "pulled"
	otherwise, return y + y """
def one_func(y):
	# TODO: Partner 1 completes


def foo(x, y):
	if x == 0:
		if y > 6:
			return zero_func(y)
		elif y > 1:
			return PARTNER_0_NAME + " " + str(zero_func(x)) + " to the remote!"
		else:
			return PARTNER_0_NAME + " " + str(one_func(x)) + " from the remote!"
	elif x == 1:
		if y > 6:
			return one_func(y)
		elif y > 1:
			return PARTNER_1_NAME + " " + str(one_func(x)) + " from the remote!"
		else:
			return PARTNER_1_NAME + " " + str(zero_func(x)) + " to the remote!"
	else:
		return "61C"

def main():
	print("The magic sequence:")
	y = 0b011010
	while y > 0:
		x = y & 1
		print(foo(x, y))

		y = y >> 1

	print(foo(0, y))

if __name__ == '__main__':
	main()