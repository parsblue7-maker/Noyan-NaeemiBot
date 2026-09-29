import asyncio
import getpass

from rubika_bot_api.api import Robot
from rubika_bot_api import filters


def get_token():
    token = getpass.getpass("🔐 توکن ربات روبیکا: ").strip()

    if not token:
        raise ValueError("توکن وارد نشده است.")

    return token


TOKEN = get_token()

bot = Robot(token=TOKEN)


@bot.on_message(filters=filters.pv)
async def handle_message(bot_instance, message):
    text = (message.text or "").strip()

    print(
        f"\n📩 پیام جدید"
        f"\nChat ID: {message.chat_id}"
        f"\nSender ID: {message.sender_id}"
        f"\nText: {text}\n"
    )

    if text == "/start":
        await message.reply(
            "سلام 👋\n"
            "ربات با موفقیت فعال شد.\n\n"
            "دستورها:\n"
            "/start - شروع ربات\n"
            "/help - راهنما"
        )
        return

    if text == "/help":
        await message.reply(
            "🤖 راهنمای ربات\n\n"
            "/start\n"
            "/help\n\n"
            "قابلیت‌های بعدی را می‌توانیم به همین فایل اضافه کنیم."
        )
        return

    # فعلاً پیام معمولی را برمی‌گرداند
    if filters.text(message):
        await message.reply(f"پیام شما دریافت شد:\n{text}")


async def main():
    print("================================")
    print("🤖 Rubika Bot")
    print("🟢 در حال اتصال...")
    print("================================")

    while True:
        try:
            print("🔌 ربات در حال اجراست...")
            await bot.run()

        except KeyboardInterrupt:
            print("\n🛑 ربات متوقف شد.")
            break

        except Exception as error:
            print(f"⚠️ خطا: {error}")
            print("🔄 تلاش مجدد تا 5 ثانیه دیگر...")
            await asyncio.sleep(5)


if __name__ == "__main__":
    asyncio.run(main())
