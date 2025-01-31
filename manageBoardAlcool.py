import os
import json
import random
from datetime import datetime
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler, CallbackContext
from telegram import Update
from main import *

import json

BOARD_DRINK_FILE = "alcoolBoard.json"

# Charger les scores des boissons
def load_drinks():
    try:
        with open(BOARD_DRINK_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}  # Retourne un dict vide si le fichier n'existe pas
    except json.JSONDecodeError:
        return {}  # En cas d'erreur de lecture, retourne un dict vide

# Sauvegarder les scores dans drinks.json
def save_drinks(drinks):
    with open(BOARD_DRINK_FILE, "w", encoding="utf-8") as file:
        json.dump(drinks, file, indent=4)

#adding score to someone
async def add_cuite(update: Update, context: CallbackContext):
    if not context.args:
        await update.message.reply_text("❌ Utilisation : /adddrink <Prénom>")
        return

    name = " ".join(context.args)  # Permet de prendre un prénom composé
    drinks = load_drinks()

    if name in drinks:
        drinks[name] += 1
        save_drinks(drinks)  # Mise à jour en temps réel
        await update.message.reply_text(f"🍺 {name} a bu un verre ! Total : {drinks[name]}")
    else:
        await update.message.reply_text(f"❌ {name} n'est pas dans la liste des buveurs !")

#displaying the leaderboard
async def drinks_leaderboard(update: Update, context: CallbackContext):
    drinks = load_drinks()

    if drinks:
        sorted_drinks = sorted(drinks.items(), key=lambda x: x[1], reverse=True)
        ranking = "\n".join([f"{user}: {count} 🍻" for user, count in sorted_drinks])
        await update.message.reply_text(f"🏆 **Classement des buveurs :**\n{ranking}")
    else:
        await update.message.reply_text("❌ Aucun score enregistré.")