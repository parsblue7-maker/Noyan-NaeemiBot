import json
from pathlib import Path

DATA_FILE = Path("keyboards.json")


def load_keyboards():
    if not DATA_FILE.exists():
        return {}

    try:
        return json.loads(DATA_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}


def save_keyboards(keyboards):
    DATA_FILE.write_text(
        json.dumps(keyboards, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )


def create_keyboard():
    print("\n=== ساخت کیبورد جدید ===")

    name = input("نام کیبورد: ").strip()

    if not name:
        print("❌ نام کیبورد خالی است.")
        return

    try:
        count = int(input("تعداد دکمه‌ها: "))
    except ValueError:
        print("❌ تعداد باید عدد باشد.")
        return

    if count < 1:
        print("❌ حداقل یک دکمه لازم است.")
        return

    buttons = []

    for i in range(1, count + 1):
        print(f"\n--- دکمه {i} ---")

        text = input("متن دکمه: ").strip()
        url = input("لینک دکمه: ").strip()

        if not text or not url:
            print("❌ متن و لینک نمی‌توانند خالی باشند.")
            return

        if not url.startswith(("http://", "https://")):
            print("❌ لینک باید با http:// یا https:// شروع شود.")
            return

        buttons.append({
            "text": text,
            "url": url
        })

    keyboards = load_keyboards()

    keyboards[name] = {
        "buttons": buttons
    }

    save_keyboards(keyboards)

    print(f"\n✅ کیبورد «{name}» ذخیره شد.")


def list_keyboards():
    keyboards = load_keyboards()

    if not keyboards:
        print("\nهیچ کیبوردی ساخته نشده.")
        return

    print("\n=== کیبوردهای موجود ===")

    for name, keyboard in keyboards.items():
        print(f"\n📌 {name}")

        for i, button in enumerate(keyboard["buttons"], 1):
            print(f"   {i}. {button['text']} → {button['url']}")


def delete_keyboard():
    keyboards = load_keyboards()

    if not keyboards:
        print("\nهیچ کیبوردی وجود ندارد.")
        return

    name = input("نام کیبورد برای حذف: ").strip()

    if name not in keyboards:
        print("❌ چنین کیبوردی پیدا نشد.")
        return

    del keyboards[name]
    save_keyboards(keyboards)

    print(f"✅ کیبورد «{name}» حذف شد.")


def main():
    while True:
        print("\n==============================")
        print("      Keyboard Manager")
        print("==============================")
        print("1. ساخت کیبورد")
        print("2. نمایش کیبوردها")
        print("3. حذف کیبورد")
        print("4. خروج")

        choice = input("\nانتخاب: ").strip()

        if choice == "1":
            create_keyboard()

        elif choice == "2":
            list_keyboards()

        elif choice == "3":
            delete_keyboard()

        elif choice == "4":
            print("خروج...")
            break

        else:
            print("❌ گزینه نامعتبر است.")


if __name__ == "__main__":
    main()
