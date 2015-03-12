
count = 1

for a in range(3):	#100p

	for b in range(5 - a*2):	#50p

		for c in range(11 - b*2 - a*5):	#20p

			for d in range(21 - c*2 - b*5 - a*10):	#10p

				for e in range(41 - d*2 - c*4 - b*10 - a*20):	#5p

					for f in range(101 - e*2 - d*5 - c*10 - b*25 - a*50):	#2p

						for g in range(201 - f*2 - e*5 - d*10 - c*20 - b*50 - a*100):	#1p

							if a*100 + b*50 + c*20 + d*10 + e*5 + f*2 + g*1 == 200:

								count += 1
								# print("100p: " + str(a) + " 50p: " + str(b) + " 20p: " + str(c) + " 10p: " + str(d) + " 5p: " + str(e) + " 2p: " + str(f) + " 1p: " + str(g))

			print(c)

print(count)
