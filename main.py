# 📘 Telegram-ассистент "Личный дневник роста"
# ================================
# 📖 Пошаговая инструкция для запуска ассистента (на русском для новичка)
# ================================

"""
[инструкция без изменений]
"""

# [Далее идёт основной код ассистента]
import os
from dotenv import load_dotenv
import sys
import aioschedule
import speech_recognition as sr
from notion_client import Client as NotionClient

# Загружаем переменные из .env
load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
NOTION_INTEGRATION_TOKEN = os.getenv("NOTION_INTEGRATION_TOKEN")
NOTION_DATABASE_ID = os.getenv("NOTION_DATABASE_ID")

# Проверка на наличие всех токенов
missing = []
if not TELEGRAM_BOT_TOKEN:
    missing.append("TELEGRAM_BOT_TOKEN")
if not OPENAI_API_KEY:
    missing.append("OPENAI_API_KEY")
if not NOTION_INTEGRATION_TOKEN:
    missing.append("NOTION_INTEGRATION_TOKEN")
if not NOTION_DATABASE_ID:
    missing.append("NOTION_DATABASE_ID")

if missing:
    print("❌ Ошибка: отсутствуют следующие переменные в .env файле:")
    for var in missing:
        print(f"- {var}")
    print("Проверь файл .env и перезапусти программу.")
    sys.exit(1)

# Инициализация Notion
notion = NotionClient(auth=NOTION_INTEGRATION_TOKEN)

# (и остальной код ниже без изменений)...
