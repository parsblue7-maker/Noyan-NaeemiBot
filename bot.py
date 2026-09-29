import asyncio
import getpass
import json
from pathlib import Path

from rubika_bot_api.api import Robot
from rubika_bot_api import filters


KEYBOARDS_FILE = Path("keyboards.json")


def load_keyboards():
    if not KEYBOARDS_FILE.exists():
        return {}

    try:
        return json.loads(
            KEYBOARDS_FILE.read_text(encoding="utf-8")
        )
    except Exception:
        return {}


def get_token():
    token = getpass.getpass(
        "🔐 توکن ربات روبیکا را وارد کنید: "
    ).strip()

    if not token:
        raise ValueError("توکن وارد نشده است.")

    return token


TOKEN = get_token()
bot = Robot(token=TOKEN)


@bot.on_message(filters=filters.pv)
async def handle_message(bot_instance, message):

    text = (message.text or "").strip()

    print("\n==============================")
    print("📩 پیام جدید")
    print(f"👤 Sender: {message.sender_id}")
    print(f"💬 Chat: {message.chat_id}")
    print(f"📝 Text: {text}")
    print("==============================")

    if text == "/start":
        await message.reply(
            "🤖 سلام!\n\n"
            "ربات با موفقیت فعال است.\n\n"
            "/start - شروع\n"
            "/help - راهنما"
        )
        return

    if text == "/help":
        await message.reply(
            "📚 راهنمای ربات\n\n"
            "/start\n"
            "/help"
        )
        return

    if text:
        await message.reply(
            f"✅ پیام شما دریافت شد:\n{text}"
        )


async def main():

    print("\n==============================")
    print("        RUBIKA BOT")
    print("==============================")
    print("🟢 ربات در حال اجراست...")
    print("🛑 برای توقف: Ctrl + C")
    print("==============================\n")

    while True:
        try:
            await bot.run()

        except KeyboardInterrupt:
            print("\n🛑 ربات متوقف شد.")
            break

        except Exception as error:
            print(f"\n⚠️ خطا: {error}")
            print("🔄 اتصال مجدد تا 5 ثانیه دیگر...")
            await asyncio.sleep(5)


if __name__ == "__main__":
    asyncio.run(main())
