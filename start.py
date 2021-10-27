import silnik.kalkulator

if __name__ == "__main__":

    silnik.kalkulator.menu()

    x = float(input("Wpisz liczbę: "))
    y = x

    while True:
        z = input("""Wpisz co chcesz zrobić:
                "+"     -   dodawanie,
                "-"     -   odejmowanie,
                "*"     -   mnożenie,
                "/"     -   dzielenie,
                "**"    -   potęgowanie,
                "stop"  -   zatrzymanie,
                "x"     -   wróć do początku.
                """)
        if z == 'stop':
            break
        elif z == '+':
            x2 = float(input("Wpisz kolejną liczbę: "))
            y = silnik.kalkulator.dodawanie(y, x2)
            print("""
            ...dodaję...
            """)
        elif z == '-':
            x2 = float(input("Wpisz kolejną liczbę: "))
            y = silnik.kalkulator.odejmowanie(y, x2)
            print("""
            ...odejmuję...
            """)
        elif z == '*':
            x2 = float(input("Wpisz kolejną liczbę: "))
            y = silnik.kalkulator.mnozenie(y, x2)
            print("""
            ...mnożę...
            """)
        elif z == '/':
            x2 = float(input("Wpisz kolejną liczbę: "))
            if x2 != 0:
                y = silnik.kalkulator.dzielenie(y, x2)
                print("""
                ...dzielę...
                """)
            else:
                print("NIE WOLNO DZIELIC PRZEZ 0 !!!")
                continue
        elif z == "**":
            x2 = float(input("Wpisz kolejną liczbę: "))
            y = silnik.kalkulator.pierwiastkowanie(y, x2)
            print("""
            ...potęguję...
            """)
        elif z == "x":
            x = float(input("Wpisz liczbę: "))
            y = x
        else:
            print("""Proszę dokonać prawidłowego wyboru:
                "+"     -   dodawanie,
                "-"     -   odejmowanie,
                "*"     -   mnożenie,
                "/"     -   dzielenie,
                "**"    -   potęgowanie,
                "stop"  -   zatrzymanie,
                "x"     -   wróć do początku.
                """)
            continue
        print("Aktualny wynik to: %.2f" % y)

    print("Wynik końcowy to: %.2f" % y)
