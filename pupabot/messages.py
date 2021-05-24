from __future__ import annotations

from . import config, __version__

CREATORS = "@aykut and @billaids"
BOT_NAME = config["core"]["bot_name"]

WELCOME_MSG = f"📚 Welcome to {BOT_NAME}" "Click /help for more information."

INFO_MSG = f"👤 Creators: {CREATORS}"

DOWNLOAD_MSG = "Downloading…"
UPLOAD_MSG = "Uploading…"
END_MSG = "Finished."

BOOK_MSG = "📘 Book: {book_name}\n" "👤 Author: {authors}\n" "🔖 ISBN: {isbn}\n"


HELP_MSG = f"Search by name or isbn only\n\n\
            **List of all commands:**\n\
            /start - Get the welcome message\n\
            /help - Get instructions\n\
            /info - Get some informatiions about the bot\n\n\
            start inline search with @{BOT_NAME}"
