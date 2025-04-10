from telethon.sync import TelegramClient
from telethon.tl.types import MessageMediaPhoto, MessageMediaDocument

# بيانات حسابك
api_id = 27496796
api_hash = '78a1f947e41858accade99d72d44c09a'

# اسم الجلسة (بيتحفظ فيه تسجيل الدخول)
session_name = 'my_session'

# روابط القنوات
source_channel = 'https://t.me/ABTVAB'
target_channel = 'https://t.me/cahnnelsccc'

# إعدادات متقدمة
limit_messages = 10  # عدد الرسائل اللي هتتسحب (تقدر تغيره زي ما تحب)
allowed_types = ['text', 'photo']  # اختيارات: text, photo, document, all

# بدء الاتصال
with TelegramClient(session_name, api_id, api_hash) as client:
    count = 0
    for message in client.iter_messages(source_channel, limit=limit_messages):
        if not message:
            continue

        # إرسال حسب النوع
        if 'text' in allowed_types and message.text and not message.media:
            client.send_message(target_channel, message.text)
            count += 1

        elif 'photo' in allowed_types and isinstance(message.media, MessageMediaPhoto):
            client.send_file(target_channel, message.media, caption=message.text or '')
            count += 1

        elif 'document' in allowed_types and isinstance(message.media, MessageMediaDocument):
            client.send_file(target_channel, message.media, caption=message.text or '')
            count += 1

    print(f"تم نقل {count} رسالة بنجاح.")
