# test.py

def greet(name):
    """
    Gibt eine Begrüßung für den angegebenen Namen aus.
    """
    return f"Hallo, {name}!"

def add(a, b):
    """
    Addiert zwei Zahlen und gibt das Ergebnis zurück.
    """
    return a + b

def main():
    """
    Führt einige Tests durch und gibt Ergebnisse aus.
    """
    print("Test der Funktion 'greet':")
    name = "Alice"
    print(f"Greeting for {name}: {greet(name)}")

    print("\nTest der Funktion 'add':")
    num1, num2 = 5, 7
    print(f"Summe von {num1} und {num2}: {add(num1, num2)}")

if __name__ == "__main__":
    main()
