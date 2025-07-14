from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

TOKEN = "7419657981:AAE89OgkCKSdnlLjW3fv48aWpbQSvL8uRak"
ID_CHAT_DESTINO = 1978627529

PALABRAS_CLAVE = ["USDT", "USDC", "BTTC", "SOL", "BNB", "BTC"]

async def filtrar_y_reenviar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensaje = update.message.text
    if mensaje and any(palabra in mensaje.upper() for palabra in PALABRAS_CLAVE):
        await context.bot.send_message(chat_id=ID_CHAT_DESTINO, text=mensaje)

app = Application.builder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), filtrar_y_reenviar))

print("✅ BOT ESCUCHANDO MENSAJES DEL GRUPO...")
app.run_polling()
