import csv
import os

# Definicja listy produktów
items = []

# Lista sprzedanych produktów
sold_items = []

# Funkcja wyświetlająca listę produktów
def get_items():
    print("Nazwa\tIlość\tJednostka\tCena (PLN)")
    for item in items:
        print(f"{item['Nazwa']}\t{item['Ilość']}\t\t{item['Jednostka']}\t{item['Cena']}")


# Funkcja dodająca nowy produkt do magazynu
def add_item(name, unit, quantity, unit_price):
    new_item = {
        "Nazwa": name,
        "Ilość": quantity,
        "Jednostka": unit,
        "Cena": unit_price
    }
    items.append(new_item)
    export_items_to_csv() 

# Funkcja sprzedająca towar z magazynu
def sell_item(name, sold_quantity):
    for item in items:
        if item['Nazwa'] == name:
            if item['Ilość'] >= sold_quantity:
                item['Ilość'] -= sold_quantity
                sold_items.append({
                    "Nazwa": name,
                    "Jednostka": sold_quantity,
                    "Ilość": item['Ilość'],
                    "Cena": item['Cena']
                })
                print(f"Sprzedano {sold_quantity} jednostek {name}.")
                return
            else:
                print("Nie ma wystarczającej ilości towaru w magazynie.")
                return
    print("Nie znaleziono towaru o podanej nazwie.")

def get_costs():
    return round(sum(item['Ilość'] * item['Cena'] for item in items), 2)

# Funkcja zliczająca wartość sprzedanych towarów
def get_income():
    return round(sum(item['Ilość'] * item['Cena'] for item in sold_items), 2)

# Funkcja wyświetlająca przychody, koszty i zarobek
def show_revenue():
    costs = get_costs()
    income = get_income()
    profit = round(income - costs, 2)
    print(f"Przychody: {income} PLN")
    print(f"Koszty: {costs} PLN")
    print(f"Zarobek: {profit} PLN")

# Funkcja eksportująca dane do pliku CSV
def export_items_to_csv():
    file_path = os.path.expanduser('~/Desktop/Kodilla/nauka_gita/Magazyn/magazyn.csv')  # Ścieżka do pliku
    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Nazwa', 'Jednostka', 'Ilość', 'Cena']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(items)

# Funkcja wczytująca dane z pliku CSV do listy items
def load_items_from_csv():
    file_path = os.path.expanduser('~/Desktop/Kodilla/nauka_gita/Magazyn/magazyn.csv')  # Ścieżka do pliku
    try:
        with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            items.clear()

            for row in reader:
                items.append({
                    'Nazwa': row['Nazwa'],
                    'Jednostka': row['Jednostka'],
                    'Ilość': int(row['Ilość']),
                    'Cena': float(row['Cena'])
                })
    except FileNotFoundError:
        print("Nie znaleziono pliku CSV.")
    except Exception as e:
        print(f"Wystąpił błąd podczas importu danych: {e}")

def main_menu():
    load_items_from_csv()
    print("\n\t\tWitaj! Wybierz opcję:")
    print("\t1. Wykonaj operację")
    print("\t2. Zobacz coś innego")
    print("\t3. Wyświetl listę produktów")
    print("\t4. Dodaj nowy towar")
    print("\t5. Sprzedaj towar")
    print("\t6. Monitorowanie zysków")
    print("\t7. Wyjście z programu")
    
def perform_operation():
    print("Wykonywanie operacji...")

while True:
    main_menu()
    choice = input("\n\tPodaj opcję: ")

    if choice == "1":
        perform_operation()
    elif choice == "2":
        print("Wybrano opcję zobaczenia czegoś innego.")
    elif choice == "3":
        get_items()
    elif choice == "4":
        print("Dodawanie nowego towaru:")
        name = input("Podaj nazwę towaru: ")
        unit = input("Podaj jednostkę miary: ")
        quantity = int(input("Podaj ilość dostępną: "))
        unit_price = float(input("Podaj cenę jednostkową: "))
        add_item(name, unit, quantity, unit_price)
        print("\nStan magazynu po dodaniu nowego towaru:")
        get_items()
    elif choice == "5":
        print("Sprzedaż towaru:")
        name = input("Podaj nazwę towaru: ")
        quantity = int(input("Podaj ilość sprzedaną: "))
        sell_item(name, quantity)
        export_items_to_csv()
        print("\nStan magazynu po sprzedaży:")
        get_items()

    elif choice == "6":
        print("Monitorowanie zysków:")
        show_revenue()
    elif choice == "7":
        export_items_to_csv()
        print("Zamykanie programu...")
        break
    else:
        print("Nieprawidłowa opcja, spróbuj ponownie.")
