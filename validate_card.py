from validate import validate_card_number

def main():
    print("💳 Luhn Kart Nömrəsi Yoxlayıcısı")
    print("Çıxmaq üçün 'q' yazın.\n")

    while True:
        card = input("Kart nömrəsini daxil edin: ").strip()

        if card.lower() == 'q':
            print("Çıxılır...")
            break

        try:
            result = validate_card_number(card)
            print(f"➡️  {card}: {'✅ Doğrudur' if result else '❌ Yanlışdır'}")
        except ValueError as e:
            print(f"⚠️  Xəta: {e}")

        # Yeni sorğu
        again = input("\nBaşqa kart yoxlamaq istəyirsiniz? (bəli / xeyr): ").strip().lower()
        if again not in ['bəli', 'beli', 'hə', 'he', 'yes', 'y']:
            print("Proqram sonlandırıldı.")
            break
        print("")  # boş sətir ayırmaq üçün

if __name__ == "__main__":
    main()
