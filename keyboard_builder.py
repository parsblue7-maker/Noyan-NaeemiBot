import json
from pathlib import Path

FILE = Path("keyboards.json")


def load():
    if FILE.exists():
        return json.loads(FILE.read_text(encoding="utf-8"))
    return {}


def save(data):
    FILE.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )


def create():
    data = load()

    name = input("نام کیبورد: ").strip()

    if not name:
        print("❌ نام وارد نشده")
        return

    count = int(input("تعداد دکمه‌ها: "))

    buttons = []

    for i in range(1, count + 1):
        print(f"\n--- دکمه {i} ---")

        text = input("متن دکمه: ").strip()
        url = input("لینک: ").strip()

        buttons.append({
            "text": text,
            "url": url
        })

    data[name] = buttons
    save(data)

    print(f"\n✅ کیبورد «{name}» ذخیره شد.")


def show():
    data = load()

    if not data:
        print("هیچ کیبوردی وجود ندارد.")
        return

    for name, buttons in data.items():
        print(f"\n📌 {name}")

        for button in buttons:
            print(
                f"  • {button['text']} → {button['url']}"
            )


def delete():
    data = load()

    name = input("نام کیبورد برای حذف: ").strip()

    if name not in data:
        print("❌ پیدا نشد.")
        return

    del data[name]
    save(data)

    print("✅ حذف شد.")


def main():
    while True:
        print("\n====================")
        print(" Keyboard Manager")
        print("====================")
        print("1) ساخت کیبورد")
        print("2) نمایش کیبوردها")
        print("3) حذف کیبورد")
        print("4) خروج")

        choice = input("انتخاب: ").strip()

        if choice == "1":
            create()

        elif choice == "2":
            show()

        elif choice == "3":
            delete()

        elif choice == "4":
            break

        else:
            print("❌ گزینه نامعتبر")


if __name__ == "__main__":
    main()
