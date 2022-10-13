from django.conf import settings
from deals.models import Deal, AdminPanel
import random
from pycoingecko import CoinGeckoAPI


def conservativ():
    cg = CoinGeckoAPI()
    price = cg.get_price(ids=['bitcoin', 'litecoin', 'ethereum',
                              'binance-bitcoin', 'ripple', 'cardano',
                              'solana', 'tron'], vs_currencies='usd')
    btc = price.get('bitcoin').get('usd')
    eth = price.get('ethereum').get('usd')
    ltc = price.get('litecoin').get('usd')
    bnb = price.get('binance-bitcoin').get('usd')
    xrp = price.get('ripple').get('usd')
    ada = price.get('cardano').get('usd')
    sol = price.get('solana').get('usd')
    trx = price.get('tron').get('usd')
    btc = round(btc, 2)
    eth = round(eth, 2)
    ltc = round(ltc, 2)
    bnb = round(bnb, 2)
    ada = round(ada, 2)
    xrp = round(xrp, 2)
    ada = round(ada, 2)
    sol = round(sol, 2)
    trx = round(trx, 2)
    panel = AdminPanel.objects.get(pk=4)
    if panel.profit_all <= 4:
        events = ['Growth', 'Fall', 'Growth', 'Growth']
        cryptos = ['btc', 'eth', 'ltc', 'bnb', 'xrp', 'ada', 'sol', 'doge', 'shib', 'trx']
        exchange = ['Binance', 'FTX', 'Kraken', 'Kukoin', 'Gate.io','Coinbase','Bitrex','Bitmart']
        deal_type = 'Conserve'
        event = random.choice(events)
        crypto = random.choice(cryptos)
        profit = random.randrange(500, 999)
        profit = "0." + str(profit)
        profit = float(profit)
        if event == "Growth":
            if crypto == 'btc':
                entry_price = btc - (btc * profit / 100)
                entry_price = round(entry_price, 3)
                panel.profit_all = panel.profit_all + profit
                panel.save()
                b = Deal(crypto='BTC', entry_price=entry_price, sell_price=btc, profit=profit,exchange=random.choice(exchange), type=deal_type)
                b.save()
            if crypto == 'eth':
                entry_price = eth - (eth * profit / 100)
                entry_price = round(entry_price, 3)
                b = Deal(crypto='ETH', entry_price=entry_price, sell_price=eth, profit=profit,exchange=random.choice(exchange), type=deal_type)
                panel.profit_all = panel.profit_all + profit
                panel.save()
                b.save()
            if crypto == 'ltc':
                entry_price = ltc - (ltc * profit / 100)
                entry_price = round(entry_price, 3)
                b = Deal(crypto='LTC', entry_price=entry_price, sell_price=ltc, profit=profit,exchange=random.choice(exchange), type=deal_type)
                panel.profit_all = panel.profit_all + profit
                panel.save()
                b.save()
            if crypto == 'bnb':

                entry_price = bnb - (bnb * profit / 100)
                entry_price = round(entry_price, 3)
                b = Deal(crypto='BNB', entry_price=entry_price, sell_price=bnb, profit=profit,exchange=random.choice(exchange), type=deal_type)
                panel.profit_all = panel.profit_all + profit
                panel.save()
                b.save()
            if crypto == 'xrp':

                entry_price = xrp - (xrp * profit / 100)
                entry_price = round(entry_price, 3)
                b = Deal(crypto='XRP', entry_price=entry_price, sell_price=xrp, profit=profit,exchange=random.choice(exchange), type=deal_type)
                panel.profit_all = panel.profit_all + profit
                panel.save()
                b.save()
            if crypto == 'ada':

                entry_price = ada - (ada * profit / 100)
                entry_price = round(entry_price, 3)
                b = Deal(crypto='ADA', entry_price=entry_price, sell_price=ada, profit=profit,exchange=random.choice(exchange), type=deal_type)
                panel.profit_all = panel.profit_all + profit
                panel.save()
                b.save()
            if crypto == 'sol':

                entry_price = sol - (sol * profit / 100)
                entry_price = round(entry_price,3)
                b = Deal(crypto='SOL', entry_price=entry_price, sell_price=sol, profit=profit,exchange=random.choice(exchange), type=deal_type)
                panel.profit_all = panel.profit_all + profit
                panel.save()
                b.save()

            if crypto == 'trx':

                entry_price = trx - (trx * profit / 100)
                entry_price = round(entry_price,3)
                panel.profit_all = panel.profit_all + profit
                panel.save()
                b = Deal(crypto='TRX', entry_price=entry_price, sell_price=trx, profit=profit,exchange=random.choice(exchange), type=deal_type)
                b.save()
        else:
            profit = '-'+ str(profit)
            profit = float(profit)
            if crypto == 'btc':

                entry_price = btc - (btc * profit / 100)
                entry_price = round(entry_price,3)
                panel.profit_all = panel.profit_all + profit
                panel.save()
                b = Deal(crypto='BTC', entry_price=entry_price, sell_price=btc, profit=profit, event='Fall',exchange=random.choice(exchange), type=deal_type)
                b.save()
            if crypto == 'eth':

                entry_price = eth - (eth * profit / 100)
                entry_price = round(entry_price,3)
                panel.profit_all = panel.profit_all + profit
                panel.save()
                b = Deal(crypto='ETH', entry_price=entry_price, sell_price=eth, profit=profit,event='Fall',exchange=random.choice(exchange), type=deal_type)
                b.save()
            if crypto == 'ltc':

                entry_price = ltc - (ltc * profit / 100)
                entry_price = round(entry_price,3)
                panel.profit_all = panel.profit_all + profit
                panel.save()
                b = Deal(crypto='LTC', entry_price=entry_price, sell_price=ltc, profit=profit, event='Fall',exchange=random.choice(exchange), type=deal_type)
                b.save()
            if crypto == 'bnb':

                entry_price = bnb - (bnb * profit / 100)
                entry_price = round(entry_price,3)
                panel.profit_all = panel.profit_all + profit
                panel.save()
                b = Deal(crypto='BNB', entry_price=entry_price, sell_price=bnb, profit=profit, event='Fall',exchange=random.choice(exchange), type=deal_type)
                b.save()
            if crypto == 'xrp':

                entry_price = xrp - (xrp * profit / 100)
                entry_price = round(entry_price,3)
                panel.profit_all = panel.profit_all + profit
                panel.save()
                b = Deal(crypto='XRP', entry_price=entry_price, sell_price=xrp, profit=profit, event='Fall',exchange=random.choice(exchange), type=deal_type)
                b.save()
            if crypto == 'ada':
                entry_price = ada - (ada * profit / 100)
                entry_price = round(entry_price,3)
                panel.profit_all = panel.profit_all + profit
                panel.save()
                b = Deal(crypto='ADA', entry_price=entry_price, sell_price=ada, profit=profit, event='Fall',exchange=random.choice(exchange), type=deal_type)
                b.save()
            if crypto == 'sol':
                entry_price = sol - (sol * profit / 100)
                entry_price = round(entry_price,3)
                panel.profit_all = panel.profit_all + profit
                panel.save()
                b = Deal(crypto='SOL', entry_price=entry_price, sell_price=sol, profit=profit, event='Fall',exchange=random.choice(exchange), type=deal_type)
                b.save()
            if crypto == 'trx':
                entry_price = trx - (trx * profit / 100)
                entry_price = round(entry_price, 3)
                b = Deal(crypto='TRX', entry_price=entry_price, sell_price=trx, profit=profit, event='Fall',exchange=random.choice(exchange), type=deal_type)
                panel.profit_all = panel.profit_all + profit
                panel.save()
                b.save()
    else:
        events = ['Fall', 'Fall', 'Fall', 'Growth']
        cryptos = ['btc', 'eth', 'ltc', 'bnb', 'xrp', 'ada', 'sol', 'doge', 'shib', 'trx']
        exchange = ['Binance', 'FTX', 'Kraken', 'Kukoin', 'Gate.io','Coinbase','Bitrex','Bitmart']
        deal_type = 'Conserve'
        event = random.choice(events)
        crypto = random.choice(cryptos)
        profit = random.randrange(500, 999)
        profit = "0." + str(profit)
        profit = float(profit)
        if event == "Growth":
            if crypto == 'btc':
                entry_price = btc - (btc * profit / 100)
                entry_price = round(entry_price, 3)
                panel.profit_all = panel.profit_all + profit
                panel.save()
                b = Deal(crypto='BTC', entry_price=entry_price, sell_price=btc, profit=profit,exchange=random.choice(exchange), type=deal_type )
                b.save()
            if crypto == 'eth':
                entry_price = eth - (eth * profit / 100)
                entry_price = round(entry_price, 3)
                b = Deal(crypto='ETH', entry_price=entry_price, sell_price=eth, profit=profit,exchange=random.choice(exchange), type=deal_type)
                panel.profit_all = panel.profit_all + profit
                panel.save()
                b.save()
            if crypto == 'ltc':
                entry_price = ltc - (ltc * profit / 100)
                entry_price = round(entry_price, 3)
                b = Deal(crypto='LTC', entry_price=entry_price, sell_price=ltc, profit=profit,exchange=random.choice(exchange), type=deal_type)
                panel.profit_all = panel.profit_all + profit
                panel.save()
                b.save()
            if crypto == 'bnb':
                entry_price = bnb - (bnb * profit / 100)
                entry_price = round(entry_price, 3)
                b = Deal(crypto='BNB', entry_price=entry_price, sell_price=bnb, profit=profit,exchange=random.choice(exchange), type=deal_type)
                panel.profit_all = panel.profit_all + profit
                panel.save()
                b.save()
            if crypto == 'xrp':
                entry_price = xrp - (xrp * profit / 100)
                entry_price = round(entry_price, 3)
                b = Deal(crypto='XRP', entry_price=entry_price, sell_price=xrp, profit=profit,exchange=random.choice(exchange), type=deal_type)
                panel.profit_all = panel.profit_all + profit
                panel.save()
                b.save()
            if crypto == 'ada':
                entry_price = ada - (ada * profit / 100)
                entry_price = round(entry_price, 3)
                b = Deal(crypto='ADA', entry_price=entry_price, sell_price=ada, profit=profit,exchange=random.choice(exchange), type=deal_type)
                panel.profit_all = panel.profit_all + profit
                panel.save()
                b.save()
            if crypto == 'sol':
                entry_price = sol - (sol * profit / 100)
                entry_price = round(entry_price, 3)
                b = Deal(crypto='SOL', entry_price=entry_price, sell_price=sol, profit=profit,exchange=random.choice(exchange), type=deal_type)
                panel.profit_all = panel.profit_all + profit
                panel.save()
                b.save()
            if crypto == 'trx':
                entry_price = trx - (trx * profit / 100)
                entry_price = round(entry_price, 3)
                panel.profit_all = panel.profit_all + profit
                panel.save()
                b = Deal(crypto='TRX', entry_price=entry_price, sell_price=trx, profit=profit,exchange=random.choice(exchange), type=deal_type)
                b.save()
        else:
            profit = '-' + str(profit)
            profit = float(profit)
            if crypto == 'btc':
                entry_price = btc - (btc * profit / 100)
                entry_price = round(entry_price, 3)
                panel.profit_all = panel.profit_all + profit
                panel.save()
                b = Deal(crypto='BTC', entry_price=entry_price, sell_price=btc, profit=profit, event='Fall',exchange=random.choice(exchange), type=deal_type)
                b.save()
            if crypto == 'eth':
                entry_price = eth - (eth * profit / 100)
                entry_price = round(entry_price, 3)
                panel.profit_all = panel.profit_all + profit
                panel.save()
                b = Deal(crypto='ETH', entry_price=entry_price, sell_price=eth, profit=profit, event='Fall',exchange=random.choice(exchange), type=deal_type)
                b.save()
            if crypto == 'ltc':
                entry_price = ltc - (ltc * profit / 100)
                entry_price = round(entry_price, 3)
                panel.profit_all = panel.profit_all + profit
                panel.save()
                b = Deal(crypto='LTC', entry_price=entry_price, sell_price=ltc, profit=profit, event='Fall',exchange=random.choice(exchange), type=deal_type)
                b.save()
            if crypto == 'bnb':
                entry_price = bnb - (bnb * profit / 100)
                entry_price = round(entry_price, 3)
                panel.profit_all = panel.profit_all + profit
                panel.save()
                b = Deal(crypto='BNB', entry_price=entry_price, sell_price=bnb, profit=profit, event='Fall',exchange=random.choice(exchange), type=deal_type)
                b.save()
            if crypto == 'xrp':
                entry_price = xrp - (xrp * profit / 100)
                entry_price = round(entry_price, 3)
                panel.profit_all = panel.profit_all + profit
                panel.save()
                b = Deal(crypto='XRP', entry_price=entry_price, sell_price=xrp, profit=profit, event='Fall',exchange=random.choice(exchange), type=deal_type)
                b.save()
            if crypto == 'ada':
                entry_price = ada - (ada * profit / 100)
                entry_price = round(entry_price, 3)
                panel.profit_all = panel.profit_all + profit
                panel.save()
                b = Deal(crypto='ADA', entry_price=entry_price, sell_price=ada, profit=profit, event='Fall',exchange=random.choice(exchange), type=deal_type)
                b.save()
            if crypto == 'sol':
                entry_price = sol - (sol * profit / 100)
                entry_price = round(entry_price, 3)
                panel.profit_all = panel.profit_all + profit
                panel.save()
                b = Deal(crypto='SOL', entry_price=entry_price, sell_price=sol, profit=profit, event='Fall',exchange=random.choice(exchange), type=deal_type)
                b.save()
            if crypto == 'trx':
                entry_price = trx - (trx * profit / 100)
                entry_price = round(entry_price, 3)
                b = Deal(crypto='TRX', entry_price=entry_price, sell_price=trx, profit=profit, event='Fall',exchange=random.choice(exchange), type=deal_type)
                panel.profit_all = panel.profit_all + profit
                panel.save()
                b.save()



def risk():
    cg = CoinGeckoAPI()
    price = cg.get_price(ids=['bitcoin', 'litecoin', 'ethereum',
                              'binance-bitcoin', 'ripple', 'cardano',
                              'solana', 'tron'], vs_currencies='usd')
    btc = price.get('bitcoin').get('usd')
    eth = price.get('ethereum').get('usd')
    ltc = price.get('litecoin').get('usd')
    bnb = price.get('binance-bitcoin').get('usd')
    xrp = price.get('ripple').get('usd')
    ada = price.get('cardano').get('usd')
    sol = price.get('solana').get('usd')
    trx = price.get('tron').get('usd')
    btc = round(btc, 2)
    eth = round(eth, 2)
    ltc = round(ltc, 2)
    bnb = round(bnb, 2)
    ada = round(ada, 2)
    xrp = round(xrp, 2)
    ada = round(ada, 2)
    sol = round(sol, 2)
    trx = round(trx, 2)
    panel = AdminPanel.objects.get(pk=4)
    if panel.profit_all <= 17:
        events = ['Growth', 'Fall', 'Growth', 'Growth']
        cryptos = ['btc', 'eth', 'ltc', 'bnb', 'xrp', 'ada', 'sol', 'doge', 'shib', 'trx']
        exchange = ['Binance', 'FTX', 'Kraken', 'Kukoin', 'Gate.io','Coinbase','Bitrex','Bitmart']
        deal_type = 'Risk'
        event = random.choice(events)
        print(event)
        crypto = random.choice(cryptos)
        profit = random.randrange(100, 999)
        first_digit = random.randrange(2, 3)
        profit = str(first_digit) + '.' + str(profit)
        profit = float(profit)
        if event == "Growth":
            if crypto == 'btc':
                entry_price = btc - (btc * profit / 100)
                entry_price = round(entry_price, 3)
                panel.profit_risk = panel.profit_risk + profit
                panel.save()
                b = Deal(crypto='BTC', entry_price=entry_price, sell_price=btc, profit=profit,exchange=random.choice(exchange), type=deal_type)
                b.save()
            if crypto == 'eth':
                entry_price = eth - (eth * profit / 100)
                entry_price = round(entry_price, 3)
                b = Deal(crypto='ETH', entry_price=entry_price, sell_price=eth, profit=profit,exchange=random.choice(exchange), type=deal_type)
                panel.profit_risk = panel.profit_risk + profit
                panel.save()
                b.save()
            if crypto == 'ltc':
                entry_price = ltc - (ltc * profit / 100)
                entry_price = round(entry_price, 3)
                b = Deal(crypto='LTC', entry_price=entry_price, sell_price=ltc, profit=profit,exchange=random.choice(exchange), type=deal_type)
                panel.profit_risk = panel.profit_risk + profit
                panel.save()
                b.save()
            if crypto == 'bnb':
                entry_price = bnb - (bnb * profit / 100)
                entry_price = round(entry_price, 3)
                b = Deal(crypto='BNB', entry_price=entry_price, sell_price=bnb, profit=profit,exchange=random.choice(exchange), type=deal_type)
                panel.profit_risk = panel.profit_risk + profit
                panel.save()
                b.save()
            if crypto == 'xrp':
                entry_price = xrp - (xrp * profit / 100)
                entry_price = round(entry_price, 3)
                b = Deal(crypto='XRP', entry_price=entry_price, sell_price=xrp, profit=profit,exchange=random.choice(exchange), type=deal_type)
                panel.profit_risk = panel.profit_risk + profit
                panel.save()
                b.save()
            if crypto == 'ada':
                entry_price = ada - (ada * profit / 100)
                entry_price = round(entry_price, 3)
                b = Deal(crypto='ADA', entry_price=entry_price, sell_price=ada, profit=profit,exchange=random.choice(exchange), type=deal_type)
                panel.profit_risk = panel.profit_risk + profit
                panel.save()
                b.save()
            if crypto == 'sol':
                entry_price = sol - (sol * profit / 100)
                entry_price = round(entry_price,3)
                b = Deal(crypto='SOL', entry_price=entry_price, sell_price=sol, profit=profit,exchange=random.choice(exchange), type=deal_type)
                panel.profit_risk = panel.profit_risk + profit
                panel.save()
                b.save()

            if crypto == 'trx':
                entry_price = trx - (trx * profit / 100)
                entry_price = round(entry_price,3)
                panel.profit_risk = panel.profit_risk + profit
                panel.save()
                b = Deal(crypto='TRX', entry_price=entry_price, sell_price=trx, profit=profit,exchange=random.choice(exchange), type=deal_type)
                b.save()
        else:
            profit = "-" + str(profit)
            profit = float(profit)
            if crypto == 'btc':
                entry_price = btc - (btc * profit / 100)
                entry_price = round(entry_price,3)
                panel.profit_risk = panel.profit_risk + profit
                panel.save()
                b = Deal(crypto='BTC', entry_price=entry_price, sell_price=btc, profit=profit, event='Fall',exchange=random.choice(exchange), type=deal_type)
                b.save()
            if crypto == 'eth':
                entry_price = eth - (eth * profit / 100)
                entry_price = round(entry_price,3)
                panel.profit_risk = panel.profit_risk + profit
                panel.save()
                b = Deal(crypto='ETH', entry_price=entry_price, sell_price=eth, profit=profit,event='Fall',exchange=random.choice(exchange), type=deal_type)
                b.save()
            if crypto == 'ltc':
                entry_price = ltc - (ltc * profit / 100)
                entry_price = round(entry_price,3)
                panel.profit_risk = panel.profit_risk + profit
                panel.save()
                b = Deal(crypto='LTC', entry_price=entry_price, sell_price=ltc, profit=profit, event='Fall',exchange=random.choice(exchange), type=deal_type)
                b.save()
            if crypto == 'bnb':
                entry_price = bnb - (bnb * profit / 100)
                entry_price = round(entry_price,3)
                panel.profit_risk = panel.profit_risk + profit
                panel.save()
                b = Deal(crypto='BNB', entry_price=entry_price, sell_price=bnb, profit=profit, event='Fall',exchange=random.choice(exchange), type=deal_type)
                b.save()
            if crypto == 'xrp':
                entry_price = xrp - (xrp * profit / 100)
                entry_price = round(entry_price,3)
                panel.profit_risk = panel.profit_risk + profit
                panel.save()
                b = Deal(crypto='XRP', entry_price=entry_price, sell_price=xrp, profit=profit, event='Fall',exchange=random.choice(exchange), type=deal_type)
                b.save()
            if crypto == 'ada':
                entry_price = ada - (ada * profit / 100)
                entry_price = round(entry_price,3)
                panel.profit_risk = panel.profit_risk + profit
                panel.save()
                b = Deal(crypto='ADA', entry_price=entry_price, sell_price=ada, profit=profit, event='Fall',exchange=random.choice(exchange), type=deal_type)
                b.save()
            if crypto == 'sol':
                entry_price = sol - (sol * profit / 100)
                entry_price = round(entry_price,3)
                panel.profit_risk = panel.profit_risk + profit
                panel.save()
                b = Deal(crypto='SOL', entry_price=entry_price, sell_price=sol, profit=profit, event='Fall',exchange=random.choice(exchange), type=deal_type)
                b.save()
            if crypto == 'trx':
                entry_price = trx - (trx * profit / 100)
                entry_price = round(entry_price, 3)
                b = Deal(crypto='TRX', entry_price=entry_price, sell_price=trx, profit=profit, event='Fall',exchange=random.choice(exchange), type=deal_type)
                panel.profit_risk = panel.profit_risk + profit
                panel.save()
                b.save()
    else:
        events = ['Fall', 'Fall', 'Fall', 'Growth']
        cryptos = ['btc', 'eth', 'ltc', 'bnb', 'xrp', 'ada', 'sol', 'doge', 'shib', 'trx']
        exchange = ['Binance', 'FTX', 'Kraken', 'Kukoin', 'Gate.io','Coinbase','Bitrex','Bitmart']
        deal_type = 'Conserve'
        event = random.choice(events)
        crypto = random.choice(cryptos)
        profit = random.randrange(100, 999)
        first_digit = random.randrange(2, 3)
        profit = str(first_digit) + '.' + str(profit)
        profit = float(profit)
        if event == "Growth":
            if crypto == 'btc':
                entry_price = btc - (btc * profit / 100)
                entry_price = round(entry_price, 3)
                panel.profit_risk = panel.profit_risk + profit
                panel.save()
                b = Deal(crypto='BTC', entry_price=entry_price, sell_price=btc, profit=profit,exchange=random.choice(exchange), type=deal_type )
                b.save()
            if crypto == 'eth':
                entry_price = eth - (eth * profit / 100)
                entry_price = round(entry_price, 3)
                b = Deal(crypto='ETH', entry_price=entry_price, sell_price=eth, profit=profit,exchange=random.choice(exchange), type=deal_type)
                panel.profit_risk = panel.profit_risk + profit
                panel.save()
                b.save()
            if crypto == 'ltc':
                entry_price = ltc - (ltc * profit / 100)
                entry_price = round(entry_price, 3)
                b = Deal(crypto='LTC', entry_price=entry_price, sell_price=ltc, profit=profit,exchange=random.choice(exchange), type=deal_type)
                panel.profit_risk = panel.profit_risk + profit
                panel.save()
                b.save()
            if crypto == 'bnb':
                entry_price = bnb - (bnb * profit / 100)
                entry_price = round(entry_price, 3)
                b = Deal(crypto='BNB', entry_price=entry_price, sell_price=bnb, profit=profit,exchange=random.choice(exchange), type=deal_type)
                panel.profit_risk = panel.profit_risk + profit
                panel.save()
                b.save()
            if crypto == 'xrp':
                entry_price = xrp - (xrp * profit / 100)
                entry_price = round(entry_price, 3)
                b = Deal(crypto='XRP', entry_price=entry_price, sell_price=xrp, profit=profit,exchange=random.choice(exchange), type=deal_type)
                panel.profit_risk = panel.profit_risk + profit
                panel.save()
                b.save()
            if crypto == 'ada':
                entry_price = ada - (ada * profit / 100)
                entry_price = round(entry_price, 3)
                b = Deal(crypto='ADA', entry_price=entry_price, sell_price=ada, profit=profit,exchange=random.choice(exchange), type=deal_type)
                panel.profit_risk = panel.profit_risk + profit
                panel.save()
                b.save()
            if crypto == 'sol':
                entry_price = sol - (sol * profit / 100)
                entry_price = round(entry_price, 3)
                b = Deal(crypto='SOL', entry_price=entry_price, sell_price=sol, profit=profit,exchange=random.choice(exchange), type=deal_type)
                panel.profit_risk = panel.profit_risk + profit
                panel.save()
                b.save()
            if crypto == 'trx':
                entry_price = trx - (trx * profit / 100)
                entry_price = round(entry_price, 3)
                panel.profit_risk = panel.profit_risk + profit
                panel.save()
                b = Deal(crypto='TRX', entry_price=entry_price, sell_price=trx, profit=profit,exchange=random.choice(exchange), type=deal_type)
                b.save()
        else:
            profit = "-" + str(profit)
            profit = float(profit)
            if crypto == 'btc':
                entry_price = btc - (btc * profit / 100)
                entry_price = round(entry_price, 3)
                panel.profit_risk = panel.profit_risk + profit
                panel.save()
                b = Deal(crypto='BTC', entry_price=entry_price, sell_price=btc, profit=profit, event='Fall',exchange=random.choice(exchange), type=deal_type)
                b.save()
            if crypto == 'eth':
                entry_price = eth - (eth * profit / 100)
                entry_price = round(entry_price, 3)
                panel.profit_risk = panel.profit_risk + profit
                panel.save()
                b = Deal(crypto='ETH', entry_price=entry_price, sell_price=eth, profit=profit, event='Fall',exchange=random.choice(exchange), type=deal_type)
                b.save()
            if crypto == 'ltc':
                entry_price = ltc - (ltc * profit / 100)
                entry_price = round(entry_price, 3)
                panel.profit_risk = panel.profit_risk + profit
                panel.save()
                b = Deal(crypto='LTC', entry_price=entry_price, sell_price=ltc, profit=profit, event='Fall',exchange=random.choice(exchange), type=deal_type)
                b.save()
            if crypto == 'bnb':
                entry_price = bnb - (bnb * profit / 100)
                entry_price = round(entry_price, 3)
                panel.profit_risk = panel.profit_risk + profit
                panel.save()
                b = Deal(crypto='BNB', entry_price=entry_price, sell_price=bnb, profit=profit, event='Fall',exchange=random.choice(exchange), type=deal_type)
                b.save()
            if crypto == 'xrp':
                entry_price = xrp - (xrp * profit / 100)
                entry_price = round(entry_price, 3)
                panel.profit_risk = panel.profit_risk + profit
                panel.save()
                b = Deal(crypto='XRP', entry_price=entry_price, sell_price=xrp, profit=profit, event='Fall',exchange=random.choice(exchange), type=deal_type)
                b.save()
            if crypto == 'ada':
                entry_price = ada - (ada * profit / 100)
                entry_price = round(entry_price, 3)
                panel.profit_risk = panel.profit_risk + profit
                panel.save()
                b = Deal(crypto='ADA', entry_price=entry_price, sell_price=ada, profit=profit, event='Fall',exchange=random.choice(exchange), type=deal_type)
                b.save()
            if crypto == 'sol':
                entry_price = sol - (sol * profit / 100)
                entry_price = round(entry_price, 3)
                panel.profit_risk = panel.profit_risk + profit
                panel.save()
                b = Deal(crypto='SOL', entry_price=entry_price, sell_price=sol, profit=profit, event='Fall',exchange=random.choice(exchange), type=deal_type)
                b.save()
            if crypto == 'trx':
                entry_price = trx - (trx * profit / 100)
                entry_price = round(entry_price, 3)
                b = Deal(crypto='TRX', entry_price=entry_price, sell_price=trx, profit=profit, event='Fall',exchange=random.choice(exchange), type=deal_type)
                panel.profit_risk = panel.profit_risk + profit
                panel.save()
                b.save()


def balance():
    cg = CoinGeckoAPI()
    price = cg.get_price(ids=['bitcoin', 'litecoin', 'ethereum',
                              'binance-bitcoin', 'ripple', 'cardano',
                              'solana', 'tron'], vs_currencies='usd')
    btc = price.get('bitcoin').get('usd')
    eth = price.get('ethereum').get('usd')
    ltc = price.get('litecoin').get('usd')
    bnb = price.get('binance-bitcoin').get('usd')
    xrp = price.get('ripple').get('usd')
    ada = price.get('cardano').get('usd')
    sol = price.get('solana').get('usd')
    trx = price.get('tron').get('usd')
    btc = round(btc, 2)
    eth = round(eth, 2)
    ltc = round(ltc, 2)
    bnb = round(bnb, 2)
    ada = round(ada, 2)
    xrp = round(xrp, 2)
    ada = round(ada, 2)
    sol = round(sol, 2)
    trx = round(trx, 2)
    panel = AdminPanel.objects.get(pk=4)
    if panel.profit_all <= 17:
        events = ['Growth', 'Fall', 'Growth', 'Growth']
        cryptos = ['btc', 'eth', 'ltc', 'bnb', 'xrp', 'ada', 'sol', 'doge', 'shib', 'trx']
        exchange = ['Binance', 'FTX', 'Kraken', 'Kukoin', 'Gate.io','Coinbase','Bitrex','Bitmart']
        deal_type = 'Balance'
        event = random.choice(events)
        crypto = random.choice(cryptos)
        profit = random.randrange(100, 999)
        first_digit = random.randrange(1, 2)
        profit = str(first_digit) + '.' + str(profit)
        profit = float(profit)
        if event == "Growth":
            if crypto == 'btc':
                entry_price = btc - (btc * profit / 100)
                entry_price = round(entry_price, 3)
                panel.profit_balance = panel.profit_balance + profit
                panel.save()
                b = Deal(crypto='BTC', entry_price=entry_price, sell_price=btc, profit=profit,exchange=random.choice(exchange), type=deal_type)
                b.save()
            if crypto == 'eth':
                entry_price = eth - (eth * profit / 100)
                entry_price = round(entry_price, 3)
                b = Deal(crypto='ETH', entry_price=entry_price, sell_price=eth, profit=profit,exchange=random.choice(exchange), type=deal_type)
                panel.profit_balance = panel.profit_balance + profit
                panel.save()
                b.save()
            if crypto == 'ltc':
                entry_price = ltc - (ltc * profit / 100)
                entry_price = round(entry_price, 3)
                b = Deal(crypto='LTC', entry_price=entry_price, sell_price=ltc, profit=profit,exchange=random.choice(exchange), type=deal_type)
                panel.profit_balance = panel.profit_balance + profit
                panel.save()
                b.save()
            if crypto == 'bnb':
                entry_price = bnb - (bnb * profit / 100)
                entry_price = round(entry_price, 3)
                b = Deal(crypto='BNB', entry_price=entry_price, sell_price=bnb, profit=profit,exchange=random.choice(exchange), type=deal_type)
                panel.profit_balance = panel.profit_balance + profit
                panel.save()
                b.save()
            if crypto == 'xrp':
                entry_price = xrp - (xrp * profit / 100)
                entry_price = round(entry_price, 3)
                b = Deal(crypto='XRP', entry_price=entry_price, sell_price=xrp, profit=profit,exchange=random.choice(exchange), type=deal_type)
                panel.profit_balance = panel.profit_balance + profit
                panel.save()
                b.save()
            if crypto == 'ada':
                entry_price = ada - (ada * profit / 100)
                entry_price = round(entry_price, 3)
                b = Deal(crypto='ADA', entry_price=entry_price, sell_price=ada, profit=profit,exchange=random.choice(exchange), type=deal_type)
                panel.profit_balance = panel.profit_balance + profit
                panel.save()
                b.save()
            if crypto == 'sol':
                entry_price = sol - (sol * profit / 100)
                entry_price = round(entry_price,3)
                b = Deal(crypto='SOL', entry_price=entry_price, sell_price=sol, profit=profit,exchange=random.choice(exchange), type=deal_type)
                panel.profit_balance = panel.profit_balance + profit
                panel.save()
                b.save()

            if crypto == 'trx':
                entry_price = trx - (trx * profit / 100)
                entry_price = round(entry_price,3)
                panel.profit_balance = panel.profit_balance + profit
                panel.save()
                b = Deal(crypto='TRX', entry_price=entry_price, sell_price=trx, profit=profit,exchange=random.choice(exchange), type=deal_type)
                b.save()
        else:
            profit = "-" + str(profit)
            profit = float(profit)
            if crypto == 'btc':
                entry_price = btc - (btc * profit / 100)
                entry_price = round(entry_price,3)
                panel.profit_balance = panel.profit_balance + profit
                panel.save()
                b = Deal(crypto='BTC', entry_price=entry_price, sell_price=btc, profit=profit, event='Fall',exchange=random.choice(exchange), type=deal_type)
                b.save()
            if crypto == 'eth':
                entry_price = eth - (eth * profit / 100)
                entry_price = round(entry_price,3)
                panel.profit_balance = panel.profit_balance + profit
                panel.save()
                b = Deal(crypto='ETH', entry_price=entry_price, sell_price=eth, profit=profit,event='Fall',exchange=random.choice(exchange), type=deal_type)
                b.save()
            if crypto == 'ltc':
                entry_price = ltc - (ltc * profit / 100)
                entry_price = round(entry_price,3)
                panel.profit_balance = panel.profit_balance + profit
                panel.save()
                b = Deal(crypto='LTC', entry_price=entry_price, sell_price=ltc, profit=profit, event='Fall',exchange=random.choice(exchange), type=deal_type)
                b.save()
            if crypto == 'bnb':
                entry_price = bnb - (bnb * profit / 100)
                entry_price = round(entry_price,3)
                panel.profit_balance = panel.profit_balance + profit
                panel.save()
                b = Deal(crypto='BNB', entry_price=entry_price, sell_price=bnb, profit=profit, event='Fall',exchange=random.choice(exchange), type=deal_type)
                b.save()
            if crypto == 'xrp':
                entry_price = xrp - (xrp * profit / 100)
                entry_price = round(entry_price,3)
                panel.profit_balance = panel.profit_balance + profit
                panel.save()
                b = Deal(crypto='XRP', entry_price=entry_price, sell_price=xrp, profit=profit, event='Fall',exchange=random.choice(exchange), type=deal_type)
                b.save()
            if crypto == 'ada':
                entry_price = ada - (ada * profit / 100)
                entry_price = round(entry_price,3)
                panel.profit_balance = panel.profit_balance + profit
                panel.save()
                b = Deal(crypto='ADA', entry_price=entry_price, sell_price=ada, profit=profit, event='Fall',exchange=random.choice(exchange), type=deal_type)
                b.save()
            if crypto == 'sol':
                entry_price = sol - (sol * profit / 100)
                entry_price = round(entry_price,3)
                panel.profit_balance = panel.profit_balance + profit
                panel.save()
                b = Deal(crypto='SOL', entry_price=entry_price, sell_price=sol, profit=profit, event='Fall',exchange=random.choice(exchange), type=deal_type)
                b.save()
            if crypto == 'trx':
                entry_price = trx - (trx * profit / 100)
                entry_price = round(entry_price, 3)
                b = Deal(crypto='TRX', entry_price=entry_price, sell_price=trx, profit=profit, event='Fall',exchange=random.choice(exchange), type=deal_type)
                panel.profit_balance = panel.profit_balance + profit
                panel.save()
                b.save()
    else:
        events = ['Fall', 'Fall', 'Fall', 'Growth']
        cryptos = ['btc', 'eth', 'ltc', 'bnb', 'xrp', 'ada', 'sol', 'doge', 'shib', 'trx']
        exchange = ['Binance', 'FTX', 'Kraken', 'Kukoin', 'Gate.io','Coinbase','Bitrex','Bitmart']
        deal_type = 'Conserve'
        event = random.choice(events)
        crypto = random.choice(cryptos)
        profit = random.randrange(100, 999)
        first_digit = random.randrange(1, 2)
        profit = str(first_digit) + '.' + str(profit)
        profit = float(profit)
        if event == "Growth":
            if crypto == 'btc':
                entry_price = btc - (btc * profit / 100)
                entry_price = round(entry_price, 3)
                panel.profit_balance = panel.profit_balance + profit
                panel.save()
                b = Deal(crypto='BTC', entry_price=entry_price, sell_price=btc, profit=profit,exchange=random.choice(exchange), type=deal_type )
                b.save()
            if crypto == 'eth':
                entry_price = eth - (eth * profit / 100)
                entry_price = round(entry_price, 3)
                b = Deal(crypto='ETH', entry_price=entry_price, sell_price=eth, profit=profit,exchange=random.choice(exchange), type=deal_type)
                panel.profit_balance = panel.profit_balance + profit
                panel.save()
                b.save()
            if crypto == 'ltc':
                entry_price = ltc - (ltc * profit / 100)
                entry_price = round(entry_price, 3)
                b = Deal(crypto='LTC', entry_price=entry_price, sell_price=ltc, profit=profit,exchange=random.choice(exchange), type=deal_type)
                panel.profit_balance = panel.profit_balance + profit
                panel.save()
                b.save()
            if crypto == 'bnb':
                entry_price = bnb - (bnb * profit / 100)
                entry_price = round(entry_price, 3)
                b = Deal(crypto='BNB', entry_price=entry_price, sell_price=bnb, profit=profit,exchange=random.choice(exchange), type=deal_type)
                panel.profit_balance = panel.profit_balance + profit
                panel.save()
                b.save()
            if crypto == 'xrp':
                entry_price = xrp - (xrp * profit / 100)
                entry_price = round(entry_price, 3)
                b = Deal(crypto='XRP', entry_price=entry_price, sell_price=xrp, profit=profit,exchange=random.choice(exchange), type=deal_type)
                panel.profit_balance = panel.profit_balance + profit
                panel.save()
                b.save()
            if crypto == 'ada':
                entry_price = ada - (ada * profit / 100)
                entry_price = round(entry_price, 3)
                b = Deal(crypto='ADA', entry_price=entry_price, sell_price=ada, profit=profit,exchange=random.choice(exchange), type=deal_type)
                panel.profit_balance = panel.profit_balance + profit
                panel.save()
                b.save()
            if crypto == 'sol':
                entry_price = sol - (sol * profit / 100)
                entry_price = round(entry_price, 3)
                b = Deal(crypto='SOL', entry_price=entry_price, sell_price=sol, profit=profit,exchange=random.choice(exchange), type=deal_type)
                panel.profit_balance = panel.profit_balance + profit
                panel.save()
                b.save()
            if crypto == 'trx':
                entry_price = trx - (trx * profit / 100)
                entry_price = round(entry_price, 3)
                panel.profit_balance = panel.profit_balance + profit
                panel.save()
                b = Deal(crypto='TRX', entry_price=entry_price, sell_price=trx, profit=profit,exchange=random.choice(exchange), type=deal_type)
                b.save()
        else:
            profit = "-" + str(profit)
            profit = float(profit)
            if crypto == 'btc':
                entry_price = btc - (btc * profit / 100)
                entry_price = round(entry_price, 3)
                panel.profit_balance = panel.profit_balance + profit
                panel.save()
                b = Deal(crypto='BTC', entry_price=entry_price, sell_price=btc, profit=profit, event='Fall',exchange=random.choice(exchange), type=deal_type)
                b.save()
            if crypto == 'eth':
                entry_price = eth - (eth * profit / 100)
                entry_price = round(entry_price, 3)
                panel.profit_balance = panel.profit_balance + profit
                panel.save()
                b = Deal(crypto='ETH', entry_price=entry_price, sell_price=eth, profit=profit, event='Fall',exchange=random.choice(exchange), type=deal_type)
                b.save()
            if crypto == 'ltc':
                entry_price = ltc - (ltc * profit / 100)
                entry_price = round(entry_price, 3)
                panel.profit_balance = panel.profit_balance + profit
                panel.save()
                b = Deal(crypto='LTC', entry_price=entry_price, sell_price=ltc, profit=profit, event='Fall',exchange=random.choice(exchange), type=deal_type)
                b.save()
            if crypto == 'bnb':
                entry_price = bnb - (bnb * profit / 100)
                entry_price = round(entry_price, 3)
                panel.profit_balance = panel.profit_balance + profit
                panel.save()
                b = Deal(crypto='BNB', entry_price=entry_price, sell_price=bnb, profit=profit, event='Fall',exchange=random.choice(exchange), type=deal_type)
                b.save()
            if crypto == 'xrp':
                entry_price = xrp - (xrp * profit / 100)
                entry_price = round(entry_price, 3)
                panel.profit_balance = panel.profit_balance + profit
                panel.save()
                b = Deal(crypto='XRP', entry_price=entry_price, sell_price=xrp, profit=profit, event='Fall',exchange=random.choice(exchange), type=deal_type)
                b.save()
            if crypto == 'ada':
                entry_price = ada - (ada * profit / 100)
                entry_price = round(entry_price, 3)
                panel.profit_balance = panel.profit_balance + profit
                panel.save()
                b = Deal(crypto='ADA', entry_price=entry_price, sell_price=ada, profit=profit, event='Fall',exchange=random.choice(exchange), type=deal_type)
                b.save()
            if crypto == 'sol':
                entry_price = sol - (sol * profit / 100)
                entry_price = round(entry_price, 3)
                panel.profit_balance = panel.profit_balance + profit
                panel.save()
                b = Deal(crypto='SOL', entry_price=entry_price, sell_price=sol, profit=profit, event='Fall',exchange=random.choice(exchange), type=deal_type)
                b.save()
            if crypto == 'trx':
                entry_price = trx - (trx * profit / 100)
                entry_price = round(entry_price, 3)
                b = Deal(crypto='TRX', entry_price=entry_price, sell_price=trx, profit=profit, event='Fall',exchange=random.choice(exchange), type=deal_type)
                panel.profit_balance = panel.profit_balance + profit
                panel.save()
                b.save()


