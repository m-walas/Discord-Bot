# bot.py
import asyncio
import os
import discord
import logging
import logging.handlers

import responses
import tictactoe

from dotenv import load_dotenv
from discord.ext import commands
from PIL import Image


async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if not is_private \
            else await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():
    # loading token from .env file
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    # handler_discord = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

    # system logger
    logger = logging.getLogger('discord')
    logger.setLevel(logging.DEBUG)
    logging.getLogger('discord.http').setLevel(logging.INFO)

    handler = logging.handlers.RotatingFileHandler(
        filename='discord.log',
        encoding='utf-8',
        maxBytes=32 * 1024 * 1024,  # 32 MiB
        backupCount=5,  # Rotate through 5 files
    )
    dt_fmt = '%Y-%m-%d %H:%M:%S'
    formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}', dt_fmt, style='{')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # creating bot
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix='.', intents=intents)

    @bot.event
    async def on_ready():
        print(f'{bot.user} has connected to Discord!')
        print(f'{bot.user} is now running')

    @bot.event
    async def on_message(message):
        # important! checking if message is from bot
        if message.author == bot.user:
            return

        # kind of logging
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        print(f'{username} sent a message in {channel}: {user_message}')

        # checking if message is a command
        if message.content.startswith('.'):
            await bot.process_commands(message)
            return

        # checking if message is a private message
        if user_message[0:3] == 'pv,':
            user_message = user_message[3:]
            await send_message(message, user_message, is_private=False)
        else:
            await send_message(message, user_message, is_private=True)

    @bot.command(name='clear', aliases=['clc', 'cls'], description='Czyszczenie czatu')
    async def clear(ctx, ilosc: int):
        await ctx.channel.purge(limit=ilosc)

    # func to delete messages sent by bot
    @bot.command(name='delete', aliases=['del', 'delete_messages'], description='Usuwanie wiadomości wysłanych przez '
                                                                                'bota')
    async def delete(ctx, ilosc: int):
        await ctx.channel.purge(limit=ilosc, check=lambda m: m.author == bot.user)

    # command to play tic-tac-toe game where the instructions are displayed in the chat,
    # and you have to enter start to start the game
    @bot.command(name='play_tictactoe', aliases=['start', 'ttt', 'play_ttt', 'playttt'], description="Gra w kółko i"
                                                                                                     "krzyżyk "
                                                                                                     "przeciwko "
                                                                                                     "komputerowi")
    async def play_tictactoe(ctx):

        # display welcome message and instructions to player
        message = await ctx.send("\n`Let's play Tic Tac Toe!`\n"
                                 "*Enter the row and column number separated by a space to make your move.*\n"
                                 "*Example: 0 0*\n"
                                 "Enter **exit** to end the game.\n"
                                 "You have **30 sec** for move.\n\n"
                                 "If you are ready enter start\n\n"
                                 "***Good luck!***\n\n")
        try:
            response = await bot.wait_for('message', check=lambda msg: msg.author == ctx.author, timeout=30)
            if response.content == 'start':
                await start_ttt(ctx)
            elif response.content == 'exit':
                await message.edit(content="`Game ended!`")
                return
            else:
                await ctx.send("\n`Enter valid command!`\n")
        except asyncio.TimeoutError:
            await message.edit(content="Game ended!")
            return

    async def start_ttt(ctx):

        # loading images
        tictactoe.tictactoe_board = Image.open('images/tictactoe_board.png')
        tictactoe.tictactoe_board.save('images/tictactoe_board_with_piece.png')
        tictactoe.tictactoe_board.close()
        tictactoe.tictactoe_board_with_piece = Image.open('images/tictactoe_board_with_piece.png')

        # tictactoe.circle1 = Image.open('images/circle1.png')
        tictactoe.cross1 = Image.open('images/cross1.png')
        tictactoe.circle2 = Image.open('images/circle2.png')
        # tictactoe.cross2 = Image.open('images/cross2.png')
        # tictactoe.line = Image.open('images/line.png')

        message = await ctx.send("`You first!`")
        # await ctx.send(tictactoe.print_board_discord())
        await ctx.send(file=discord.File('images/tictactoe_board_with_piece.png'))
        while True:
            # player's turn
            while True:
                try:
                    response = await bot.wait_for('message', check=lambda msg: msg.author == ctx.author, timeout=30)

                    if response.content == 'exit':
                        await message.edit(content="`Game ended!`")
                        await ctx.send(content="`Game ended!`")
                        return
                    else:
                        row, col = map(int, response.content.split())
                    if 0 <= row <= 2 and 0 <= col <= 2:
                        if tictactoe.board[row][col] == ' ':
                            tictactoe.board[row][col] = tictactoe.player
                            tictactoe.generate_board(row, col)
                            break
                        else:
                            # await message.edit(
                            #     content="`This place is already filled!`\n\n" + tictactoe.print_board_discord())
                            await ctx.send("`This place is already filled!`")
                            await ctx.send(file=discord.File('images/tictactoe_board_with_piece.png'))
                    else:
                        # await message.edit(
                        #     content="`Enter valid row and column!`\n\n" + tictactoe.print_board_discord())
                        await ctx.send("`Enter valid row and column!`")
                        await ctx.send(file=discord.File('images/tictactoe_board_with_piece.png'))
                except asyncio.TimeoutError:
                    # await message.edit(
                    #     content="`Timeout! You took too long to respond.`\n\n" + tictactoe.print_board_discord())
                    await ctx.send("`Timeout! You took too long to respond.`")
                    await ctx.send(file=discord.File('images/tictactoe_board_with_piece.png'))
                    return
                except ValueError:
                    # await message.edit(content="`Enter valid row and column!`\n\n" + tictactoe.print_board_discord())
                    await ctx.send("`Enter valid row and column!`")
                    await ctx.send(file=discord.File('images/tictactoe_board_with_piece.png'))

            # await message.edit(content=" \n" + tictactoe.print_board_discord())
            await ctx.send("`Your turn:`")
            await ctx.send(file=discord.File('images/tictactoe_board_with_piece.png'))

            if tictactoe.check_win(tictactoe.board, tictactoe.player):
                # await ctx.send("Good game!\n" + tictactoe.print_board_discord() + "\n***You won***!\n\n")
                await ctx.send("`Good game!`")
                # tictactoe.draw_line(tictactoe.win_position(tictactoe.board, tictactoe.player))
                await ctx.send(file=discord.File('images/tictactoe_board_with_piece.png'))
                await ctx.send("***You won!***")
                break
            if not any(' ' in row for row in tictactoe.board):
                # await ctx.send("Lucky!\n" + tictactoe.print_board_discord() + "\n*It's a draw*!\n\n")
                await ctx.send("`Lucky!`")
                await ctx.send("*It's a draw!*")
                break

            # computer's turn
            row, col = tictactoe.best_move(tictactoe.board)
            tictactoe.board[row][col] = tictactoe.computer
            tictactoe.generate_board(row, col)
            # await message.edit(content="\nComputer's turn:\n\n" + tictactoe.print_board_discord())
            await ctx.send("`Computer's turn:`")
            await ctx.send(file=discord.File('images/tictactoe_board_with_piece.png'))
            if tictactoe.check_win(tictactoe.board, tictactoe.computer):
                # await ctx.send("Game over!\n" + tictactoe.print_board_discord() + "\n***You lost***!\n\n")
                await ctx.send("`Game over!`")
                # tictactoe.draw_line(tictactoe.win_position(tictactoe.board, tictactoe.computer))
                await ctx.send(file=discord.File('images/tictactoe_board_with_piece.png'))
                await ctx.send("***You lost!***")
                break
            if not any(' ' in row for row in tictactoe.board):
                # await ctx.send("Lucky!\n" + tictactoe.print_board_discord() + "\n*It's a draw*!\n\n")
                await ctx.send("`Lucky!`")
                await ctx.send("*It's a draw!*")
                break

        tictactoe.tictactoe_board_with_piece.close()
        tictactoe.cross1.close()
        # tictactoe.cross2.close()
        # tictactoe.circle1.close()
        tictactoe.circle2.close()
        # tictactoe.line.close()
        tictactoe.clear_board()

    # on the end of the whole function run the bot
    bot.run(TOKEN, log_handler=handler)
