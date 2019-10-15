#!/bin/bash

# KEY="745326201:AAEuz8CW3e5kGeDOj2Qirec2RECoPZaHlG0"
KEY="diisi_token_bot"
URL="https://api.telegram.org/bot$KEY/sendMessage"

TARGET="diisi_chat_id" # Telegram ID of the conversation with the bot, get it from /getUpdates API

TEXT=" *New Articles*
$(bash send_telegram.sh)

Date :  *$(date '+%Y-%m-%d %H:%M:%S %Z')* "

PAYLOAD="chat_id=$TARGET&text=$TEXT&parse_mode=Markdown&disable_web_page_preview=true"

# Run in background so the script could return immediately without blocking PAM
curl -s --max-time 10 --retry 5 --retry-delay 2 --retry-max-time 10 -d "$PAYLOAD" $URL > /dev/null 2>&1 &


