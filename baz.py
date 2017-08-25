""" Returns name of your favorite 61C professor as a string.
	If your partner 0, return "Randy Katz".
	If your partner 1, return "Krste Asanovic". """
def getFavoriteProf():
	# Some random code
	x = 1
	i = 0
	while x > 2**32:
		x = x << 1
		i += 1

	FAVORITE_PROF = ""
	return FAVORITE_PROF

def main():
	favorite = getFavoriteProf()
	print("We seem to be in disagreement over our favorite 61C professor.")
	print("But we've resolved our conflicts and merged on a single opinion")
	print(favorite + " is our favorite professor!")

if __name__ == '__main__':
	main()