import os
import time

time.sleep(10)
try:
    if os.path.exists('last.pyw'):
        os.remove('last.pyw')
    os.rename('tele_bot.pyw', 'last.pyw')
    os.rename('update.pyw', 'tele_bot.pyw')
    os.startfile('tele_bot.pyw')
except Exception as e:
    with open('update_error.txt', 'a') as f:
        f.write(str(e))
