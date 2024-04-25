def amoeba (hours):

	cells = 1
	for i in range(hours, 0, -3):
		cells = cells * 2
	return cells

print(amoeba(24))