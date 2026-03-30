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
		print("\n--- Analyse abgeschlossen --")
		print("Anzahl der Fehler: ", error_count)
		print("Anzahl der untersuchten Zeilen: ", line_count)
		if line_count > 0:
			error_rate = (error_count / line_count) * 100
			print("Fehlerrate: ", round(error_rate, 2), "%")
		break
	except FileNotFoundError:
		print("Fehler: Datei nicht gefunden.")


print("\nAnalyse erfolgreich abgeschlossen.")
