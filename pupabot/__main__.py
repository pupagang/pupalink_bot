import io

from pyrogram import Client, filters
from pyrogram.types import (
    InlineQuery,
    InlineQueryResult,
    InlineQueryResultArticle,
    InputTextMessageContent,
    Message,
)

from .helpers.helpers import get_readable_file_size

from . import bot, search_service, pupa_service, messages


@bot.on_message(filters.command("start"))
async def start(client: Client, msg: Message):
    await msg.reply(messages.WELCOME_MSG)


@bot.on_message(filters.command("help"))
async def info(client: Client, msg: Message):
    await msg.reply(messages.HELP_MSG)


@bot.on_message(filters.command("info"))
async def help(client: Client, msg: Message):
    await msg.reply(messages.INFO_MSG)


@bot.on_inline_query()
async def inline(client: Client, query: InlineQuery):

    results: list[InlineQueryResult] = []

    if query.query:
        books = await pupa_service.search_book(query.query)
        for book in books:
            authors = ", ".join(str(x) for x in book.authors)
            results += (
                InlineQueryResultArticle(
                    title=book.name,
                    input_message_content=InputTextMessageContent(book.gen_dl_link()),
                    description=f"Authors: {authors}",
                    thumb_url=book.get_cover(),
                ),
            )

    if results:
        try:
            await query.answer(results)
        except TypeError:
            pass


@bot.on_message(filters.regex(r"https?://(?:link\.)?springer\.com/(?:content*.*)"))
async def book_link(client: Client, msg: Message):
    try:
        print(msg.matches[0].group())
        book = pupa_service.download_book(msg.matches[0].group())
        bytes_io = io.BytesIO(book)
    except Exception:
        await msg.reply("Not found")
        return


bot.run()
bot.loop.run_until_complete(pupa_service.close())
