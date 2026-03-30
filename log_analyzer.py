while True:
	file_path = input("Welche Logdatei möchtest du analysieren?: ")

	error_count = 0
	line_count = 0

	try:
		with open(file_path, "r") as file:
			for line in file:
				line_count += 1
				if "error" in line.lower():
					error_count += 1
		print("Anzahl der Fehler: ", error_count)
		print("Anzahl der untersuchten Zeilen: ", line_count)
		break
	except FileNotFoundError:
		print("Fehler: Datei nicht gefunden.")


