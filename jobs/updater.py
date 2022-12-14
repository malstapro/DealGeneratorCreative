from apscheduler.schedulers.background import BackgroundScheduler
import datetime
from .jobs import conservativ, risk,balance
from deals.models import AdminPanel


def start():
    time = AdminPanel.objects.get(pk=4)
    time = time.deal
    scheduler = BackgroundScheduler()
    scheduler.add_job(conservativ, 'interval', seconds=200)
    scheduler.add_job(risk, 'interval', seconds=200)
    scheduler.add_job(balance, 'interval', seconds=200)
    scheduler.start()