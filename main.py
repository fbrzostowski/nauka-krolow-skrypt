import os

# katalog, w którym znajduje się skrypt
folder_path = os.path.dirname(os.path.abspath(__file__))

# --- 1. WYŚWIETLENIE ASCII ART ---
ascii_file = os.path.join(folder_path, "magyarorszag.txt")

if os.path.exists(ascii_file):
    with open(ascii_file, "r", encoding="utf-8") as f:
        print(f.read())
else:
    print("Brak pliku magyarorszag.txt\n")

print("\n=== WYBIERZ TRYB GRY ===\n")
print("1. Wszystko (każda linia)")
print("2. Władcy (co 3 linia: 1,4,7...)")

while True:
    mode_choice = input("\nWybierz tryb (1 lub 2): ")
    if mode_choice in ["1", "2"]:
        break
    print("Podaj 1 albo 2.")

print("\n=== WYBIERZ LISTĘ DO NAUKI ===\n")

# --- 2. LISTA PLIKÓW TXT ---
txt_files = [
    f for f in os.listdir(folder_path)
    if f.endswith(".txt") and f != "magyarorszag.txt"
]

if not txt_files:
    print("Brak plików .txt do nauki.")
    exit()

for i, file in enumerate(txt_files):
    print(f"{i+1}. {file}")

while True:
    try:
        choice = int(input("\nWybierz numer pliku: "))
        if 1 <= choice <= len(txt_files):
            break
        else:
            print("Podaj poprawny numer.")
    except ValueError:
        print("Wpisz liczbę.")

selected_file = os.path.join(folder_path, txt_files[choice - 1])

# --- 3. WCZYTANIE LISTY ---
with open(selected_file, "r", encoding="utf-8") as f:
    all_lines = [line.strip() for line in f if line.strip()]

# --- 4. WYBÓR LINII W ZALEŻNOŚCI OD TRYBU ---
if mode_choice == "1":
    lines = all_lines
else:
    lines = all_lines[0::3]  # co 3 linia (1,4,7...)

print("\n🔥 Tryb Hardcore: Błąd = wracasz na początek 🔥\n")

# --- 5. NAUKA ---
i = 0

while i < len(lines):
    print(f"\nPytanie {i+1}:")
    answer = input("Wpisz: ")

    if answer.strip() == lines[i]:
        print("✅ Dobrze!")
        i += 1
    elif answer.strip() == "goto":
        i=int(input("line: "))
        i = i - 1
    else:
        print(f"❌ Źle! Poprawna odpowiedź to:\n   {lines[i]}")
        print("🔁 Wracasz na początek!\n")
        i = 0

print("\n🎉 Gratulacje! Opanowałeś wybrany tryb.")

