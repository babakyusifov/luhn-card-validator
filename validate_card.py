from typing import Union

def validate_card_number(card_number: Union[str, int]) -> bool:
    card_str = str(card_number).replace(" ", "")
    
    if not card_str.isdigit():
        raise ValueError("Kart nömrəsi yalnız rəqəmlərdən ibarət olmalıdır.")
    if len(card_str) != 16:
        raise ValueError("Kart nömrəsi 16 rəqəmdən ibarət olmalıdır.")

    total = 0
    reverse_digits = card_str[::-1]

    for i, digit in enumerate(reverse_digits):
        n = int(digit)
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        total += n

    return total % 10 == 0


def process_cards_file(file_path: str):
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"❌ Fayl tapılmadı: {file_path}")
        return

    for line in lines:
        card = line.strip()
        if not card:
            continue
        try:
            if validate_card_number(card):
                print(f"✅ {card} - düzgündür.")
            else:
                print(f"❌ {card} - düzgün deyil.")
        except ValueError as e:
            print(f"⚠️  {card} - xəta: {e}")


if __name__ == "__main__":
    mode = input("📌 Bir kart yoxlamaq (1) yoxsa fayldan oxumaq (2)? [1/2]: ").strip()

    if mode == "1":
        card = input("Kart nömrəsini daxil et: ")
        try:
            if validate_card_number(card):
                print("✅ Kart nömrəsi düzgündür.")
            else:
                print("❌ Kart nömrəsi düzgün deyil.")
        except ValueError as e:
            print("⚠️  Xəta:", e)
    elif mode == "2":
        process_cards_file("cards.txt")
    else:
        print("⚠️  Seçim düzgün deyil.")
