# nimm eine Liste von Sensorwerten
# führe Slicing durch, sodass:
# - Nur jeder zweite Wert genommen wird.
# - Nur die erste Hälfte betrachtet wird.
def sensor_subsampling(sensor_werte):
    reduzierte_werte = sensor_werte[ : int(len(sensor_werte) / 2) + 1 : 2]
    return reduzierte_werte
    
sensor_werte = [3.2, 10.0, 2.8, 4.5, 6.4, -3.2, 2.9, 5.6, -1.2]
# sollte ausgeben: [3.2, 2.8, 6.4]

def test_sensor_subsampling(werte, expected):
    actual = sensor_subsampling(werte)
    if actual == expected:
        print("Bestanden")
    else:
        print(f"Failure! Sollte {expected} sein, ist aber {actual}")

test_sensor_subsampling(sensor_werte, [3.2, 2.8, 6.4])
test_sensor_subsampling([-5.4, -100, 3.2, 10.0, 2.8, 4.5, 6.4, -3.2, 2.9, 5.6, -1.2], 
                        [-5.4, 3.2, 2.8])
test_sensor_subsampling([], 
                        [])
test_sensor_subsampling([3.2, 10.0, 2.8, 4.5, 6.4, -3.2, 2.9, 5.6], 
                        [3.2, 2.8])