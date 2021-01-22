# -*- coding: utf-8 -*-
import discord
import json,asyncio,datetime
from discord.ext import commands

class Cog_Extension(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
