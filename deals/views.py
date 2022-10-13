import datetime

from django.shortcuts import render
from pycoingecko import CoinGeckoAPI

import random

from deals.models import Deal, AdminPanel


def index(request):
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
    deals = Deal.objects.order_by('-date')
    xrp = round(xrp, 2)
    ada = round(ada, 2)
    trx = round(trx, 2)
    now = datetime.datetime.now()
    context = {
        'now': now,
        'deals': deals,
        'btc': btc,
        'eth': eth,
        'xrp': xrp,
        'ada': ada,
        'sol': sol,
        'trx': trx,
        'ltc': ltc,
        'bnb': bnb,
    }
    return render(request, 'dealer.html', context)