import os
import json
import random
from datetime import datetime
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler, CallbackContext
from telegram import Update
import main #j'importe le fichier main du bot


USER_FILE = "users.json"

def load_users():
    try:
        with open(USER_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# saving users to the Json external file
def save_users(users):
    with open(USER_FILE, "w", encoding="utf-8") as file:
        json.dump(users, file, indent=4)

async def add_user(update: Update, context: CallbackContext):
    if not context.args:
        await update.message.reply_text("❌ Utilisation : /adduser Nom de l'utilisateur")
        return

    user = " ".join(context.args)  # Récupère le nom complet
    users = load_users()

    if user in users:
        await update.message.reply_text(f"⚠️ {user} est déjà dans la liste.")
    else:
        users.append(user)  # Ajoute l'utilisateur à la liste
        save_users(users)  # Sauvegarde dans users.json
        await update.message.reply_text(f"✅ {user} ajouté à la liste.")

async def remove_user(update: Update, context: CallbackContext):
    if not context.args:
        await update.message.reply_text("❌ Utilisation : /removeuser Nom de l'utilisateur")
        return

    user = " ".join(context.args)
    users = load_users()

    if user in users:
        users.remove(user)  # Supprime l'utilisateur
        save_users(users)  # Met à jour le fichier JSON
        await update.message.reply_text(f"✅ {user} supprimé de la liste.")
    else:
        await update.message.reply_text(f"❌ {user} n'est pas dans la liste.")


async def list_users(update: Update, context: CallbackContext):
    users = load_users()
    if not users:
        await update.message.reply_text("❌ Aucun utilisateur enregistré.")
    else:
        user_list = "\n".join(users)
        await update.message.reply_text(f"Liste des utilisateurs enregistrés :\n{user_list}")

async def random_user(update : Update, context : CallbackContext):
    users = load_users() #je recupere la liste des users du canal telegram
    if not users:
        await update.message.reply_text("❌ Aucun utilisateur enregistré.")
    else:
        random_user = random.choice(users)
        await update.message.reply_text(f"Personne choisie random  : {random_user}")
