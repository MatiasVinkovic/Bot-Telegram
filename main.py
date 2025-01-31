import os
import json
import random
from datetime import datetime
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler, CallbackContext
from telegram import Update
from manageUsers import *
from manageBoardAlcool import *

# Charger les variables d'environnement
load_dotenv()
token = os.getenv('TOKEN', '7851705895:AAHPJSrRRbHrt1erfhHhVL1KZ9Gsroompg4')

# Afficher l'heure actuelle
current_time = datetime.now().strftime("%H:%M:%S")
print(f"Current time: {current_time}")





# Command /start
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("""Bienvenue sur votre bot Telegram, voici la liste des fonctions disponibles :
                                        /noleche
                                        /site""")

# Command /noleche
async def no_leche_func(update: Update, context: CallbackContext):
    users = load_users()  # Charger la liste à chaque exécution
    if len(users) < 2:
        await update.message.reply_text("❌ Pas assez de membres enregistrés.")
        return

    current_date = datetime.now().strftime("%A %d %B %Y")
    await update.message.reply_text(random.choice(users) + " a sucé " + random.choice(users) + " le " + current_date)



if __name__ == '__main__':
    # Construire l'application
    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('noleche', no_leche_func))
    app.add_handler(CommandHandler("adduser", add_user))
    app.add_handler(CommandHandler("removeuser", remove_user))
    app.add_handler(CommandHandler("listuser", list_users))
    app.add_handler(CommandHandler("random", random_user))
    
    #leaderBoard drink
    app.add_handler(CommandHandler("addcuite", add_cuite))
    app.add_handler(CommandHandler("showcuite", drinks_leaderboard))


    # Démarrer le bot en mode polling
    app.run_polling(poll_interval=5)
