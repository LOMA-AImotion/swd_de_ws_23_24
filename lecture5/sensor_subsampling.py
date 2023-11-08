# nimm eine Liste von Sensorwerten
# führe Slicing durch, sodass:
# - Nur jeder zweite Wert genommen wird.
# - Nur die erste Hälfte betrachtet wird.
sensor_werte = [3.2, 10.0, 2.8, 4.5, 6.4, -3.2, 2.9, 5.6, -1.2]
# sollte ausgeben: [3.2, 2.8, 6.4]

reduzierte_werte = sensor_werte[ : int(len(sensor_werte) / 2) + 1 : 2]
print(reduzierte_werte)