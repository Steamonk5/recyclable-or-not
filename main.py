import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
@bot.command()
async def rep(ctx,gar):
    rec={'office_paper':'This item is a recycling product, you can throw it away in the blue dumpster.',
        'newspaper':'This item is a recycling product, you can throw it away in the blue dumpster.',
         'magazine':'This item is a recycling product, you can throw it away in the blue dumpster.',
         'cardboard':'This item is a recycling product, you can throw it away in the blue dumpster.',
         'mail':'This item is a recycling product, you can throw it away in the blue dumpster.',
         'paper_bag':'This item is a recycling product, you can throw it away in the blue dumpster.',
         'plastic_bottle':'This item is a recycling product, you can throw it away in the blue dumpster.',
         'milk_jug':'This item is a recycling product, you can throw it away in the blue dumpster.',
         'detergent_container':'This item is a recycling product, you can throw it away in the blue dumpster.',
         'plastic_container':'This item is a recycling product, you can throw it away in the blue dumpster.',
         'bottle':'This item is a recycling product, you can throw it away in the blue dumpster.',
         'jar':'This item is a recycling product, you can throw it away in the blue dumpster.',
         'aluminum_can':'This item is a recycling product, you can throw it away in the blue dumpster.',
         'steel_can':'This item is a recycling product, you can throw it away in the blue dumpster.',
         'tin_can':'This item is a recycling product, you can throw it away in the blue dumpster.',
         'aluminum_foil':'This item is a recycling product, you can throw it away in the blue dumpster.',
         'corrugated_cardboard_box':'This item is a recycling product, you can throw it away in the blue dumpster.',
         'paperboard':'This item is a recycling product, you can throw it away in the blue dumpster.',
         'electronic':'This item is a recycling product, you can throw it away in the blue dumpster.',
         'battery':'This item is a recycling product, you can throw it away in the blue dumpster.',
         'clothes':'This item is a recycling product, you can throw it away in the blue dumpster.',
         'plastic_bag':'This item is not a recycling product, you can throw it away in the green dumpster.',
         'film':'This item is not a recycling product, you can throw it away in the green dumpster.',
         'styrofoam':'This item is not a recycling product, you can throw it away in the green dumpster.',
         'food':'This item is not a recycling product, you can throw it away in the green dumpster.',
         'paint':'This item is not a recycling product, you can throw it away in the green dumpster.',
         'chemicals':'This item is not a recycling product, you can throw it away in the green dumpster.',
         'pesticides':'This item is not a recycling product, you can throw it away in the green dumpster.',
         'pyrex':'This item is not a recycling product, you can throw it away in the green dumpster.',
         'window_glass':'This item is not a recycling product, you can throw it away in the green dumpster.',
         'ceramic':'This item is not a recycling product, you can throw it away in the green dumpster.',
         'mirror':'This item is not a recycling product, you can throw it away in the green dumpster.'}
    await ctx.send(rec[gar])
bot.run("MTI3MTE0MDcwMzkyNTQ0MDY0NA.GATXoS.5qQlAFu_g3HXndc0EgQgx56g-b5VMs9RTevei8")
