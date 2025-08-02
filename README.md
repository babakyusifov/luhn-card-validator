# 💳 Luhn Card Validator (Python, CLI, Termux-friendly)

Bu sadə Python skripti vasitəsilə bank kartlarının **Luhn alqoritmi** ilə düzgünlüyünü yoxlaya bilərsiniz.  
Həm **interaktiv (input)**, həm də **fayldan çoxlu kart yoxlama** dəstəklənir.

---

## 🚀 Xüsusiyyətlər

- ✅ 16 rəqəmli kart nömrələrinin düzgünlüyünü yoxlayır
- 🧠 Luhn alqoritmi ilə yoxlama aparır
- 📂 `cards.txt` faylından oxuyaraq çoxlu kart yoxlayır
- 📱 Android Termux-da problemsiz işləyir

---

## 🔧 Quraşdırma (Termux və ya Linux)

```bash
pkg install python
git clone https://github.com/istifadeci-ad/luhn-card-validator.git
cd luhn-card-validator
python validate_card.py
