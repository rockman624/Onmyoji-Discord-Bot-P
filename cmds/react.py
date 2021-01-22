# -*- coding: utf-8 -*-
import discord
import json,asyncio,datetime
from discord.ext import commands
from core.classes import Cog_Extension

class React(Cog_Extension):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        async def time_task1():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(790977190027460678)
            while not self.bot.is_closed():
                nowtime = datetime.datetime.now().strftime('%H%M%S')
                nowdate = datetime.datetime.today().weekday()
                with open('./onmyoji/setting.json','r',encoding='utf8') as jfile:
                    jdata = json.load(jfile)
                if nowtime == jdata['time1'] and nowdate in [0,1,2,3]:
                    await self.channel.send(f'{self.channel.mention}狩獵戰倒數5分鐘...')
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
                    pass
        self.bg_task = self.bot.loop.create_task(time_task1())
        async def time_task2():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(790977190027460678)
            while not self.bot.is_closed():
                nowtime = datetime.datetime.now().strftime('%H%M%S')
                with open('./onmyoji/setting.json','r',encoding='utf8') as jfile:
                    jdata = json.load(jfile)
                if nowtime == jdata['time2']:
                    await self.channel.send(f'{self.channel.mention}寮車倒數5分鐘...')
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
                    pass
        self.bg_task = self.bot.loop.create_task(time_task2())
        async def time_task3():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(790977190027460678)
            while not self.bot.is_closed():
                nowtime = datetime.datetime.now().strftime('%H%M%S')
                nowdate = datetime.datetime.today().weekday()
                with open('./onmyoji/setting.json','r',encoding='utf8') as jfile:
                    jdata = json.load(jfile)
                if nowtime == jdata['time3'] and nowdate in [5,6]:
                    await self.channel.send(f'{self.channel.mention}吃寮飯倒數5分鐘...')
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
                    pass
        self.bg_task = self.bot.loop.create_task(time_task3())
        async def time_task4():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(790977190027460678)
            while not self.bot.is_closed():
                nowtime = datetime.datetime.now().strftime('%H%M%S')
                nowdate = datetime.datetime.today().weekday()
                with open('./onmyoji/setting.json','r',encoding='utf8') as jfile:
                    jdata = json.load(jfile)
                if nowtime == jdata['time4'] and nowdate == 5:
                    await self.channel.send(f'{self.channel.mention}首領退治倒數5分鐘...')
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
                    pass
        self.bg_task = self.bot.loop.create_task(time_task4())
        
    
    @commands.command()
    async def setchannel(self,ctx,ch:int):
        self.channel = self.bot.get_channel(ch)
        self.guild = self.bot.get_guild(561567676476948510)
        self.role = self.guild.get_role(688756070898073635)
        await ctx.send(f'Set Channel: {self.role.mention}')
            
def setup(bot):
    bot.add_cog(React(bot))