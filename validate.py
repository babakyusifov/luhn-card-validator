from typing import Union

def validate_card_number(card_number: Union[str, int]) -> bool:
    """
    Verilmiş kart nömrəsinin Luhn alqoritminə əsasən düzgünlüyünü yoxlayır.

    Parametrlər:
        card_number (str | int): 16 rəqəmli kart nömrəsi

    Qayıdır:
        bool: Əgər kart nömrəsi düzgündürsə True, əks halda False
    """

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
