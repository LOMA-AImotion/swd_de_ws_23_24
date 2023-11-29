def lese_woerter_aus_txt(file_name: str) -> list:
    """
    Liest Wörter aus einer Textdatei, wobei jedes Wort in einer eigenen Zeile steht.

    Parameters:
    - file_name (str): Der Dateipfad zur Textdatei.

    Returns:
    - list: Eine Liste von Wörtern aus der Datei.
    """
    try:
        with open(file_name, 'r') as file:
            # Lese alle Zeilen aus der Datei und entferne Leerzeichen und Zeilenumbrüche
            woerter = [line.strip() for line in file.readlines()]

        return woerter
    except FileNotFoundError:
        print(f"Die Datei '{file_name}' wurde nicht gefunden.")
        return []

