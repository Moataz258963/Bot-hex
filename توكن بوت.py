import os
import zipfile
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# مسار الملفات
zip_path =  game_patch_3.7.0.19732.zip 
skin_file_path =  Skin Code ( English ).h 

def extract_and_search_hex(hex_value, update):
    hex_value = hex_value.lower()

    try:
        bytes.fromhex(hex_value)
    except ValueError:
        return "⚠️ تأكد من إدخال قيمة هكس صحيحة!"

    results = []

    if not os.path.exists(zip_path):
        return f"❌ الملف {zip_path} غير موجود."

    with zipfile.ZipFile(zip_path,  r ) as zip_file:
        for file_name in zip_file.namelist():
            try:
                with zip_file.open(file_name) as file:
                    content = file.read().hex()

                    if hex_value in content:
                        results.append(f"✅ تم العثور على القيمة في: {file_name}")
                        update.message.reply_document(document=zip_file.open(file_name), filename=file_name)

            except Exception as e:
                results.append(f"❌ خطأ عند قراءة الملف: {file_name} - {e}")

    return "\n".join(results) if results else "❌ لم يتم العثور على أي نتائج."

def search_skin_name(name, update):
    if not os.path.exists(skin_file_path):
        return f"❌ الملف {skin_file_path} غير موجود."

    results = []

    with open(skin_file_path,  r , encoding= utf-8 ) as file:
        lines = file.readlines()

        for i, line in enumerate(lines, start=1):
            if name.lower() in line.lower():
                results.append(f"✅ تم العثور على الاسم في السطر {i}: {line.strip()}")

    return "\n".join(results) if results else "❌ لم يتم العثور على أي نتائج."

def hex_command(update: Update, context: CallbackContext) -> None:
    if not context.args:
        update.message.reply_text("🟡 استخدم الأمر هكذا: /hex <قيمة_الهكس>")
        return

    hex_value = context.args[0].strip()
    update.message.reply_text("🔍 جاري البحث عن القيمة...")

    result = extract_and_search_hex(hex_value, update)
    update.message.reply_text(result)

def name_command(update: Update, context: CallbackContext) -> None:
    if not context.args:
        update.message.reply_text("🟡 استخدم الأمر هكذا: /name <اسم_السكِن>")
        return

    skin_name = " ".join(context.args).strip()
    update.message.reply_text("🔍 جاري البحث عن اسم السكن...")

    result = search_skin_name(skin_name, update)
    update.message.reply_text(result)

def start_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("🤖 مرحبًا! يمكنك استخدام الأوامر التالية:\n" 
                              "/hex <قيمة_الهكس> - للبحث عن الهكس في الملف المضغوط\n" 
                              "/name <اسم_السكِن> - للبحث عن اسم السكن في ملف الأكواد")

def main():
    TOKEN = "7592313536:AAEb8dEdkDsaINZs1HeQFpLv-CKSTZH-TvE"

    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("hex", hex_command))
    dispatcher.add_handler(CommandHandler("name", name_command))
    dispatcher.add_handler(CommandHandler("start", start_command))

    print("🚀 البوت يعمل...")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()

