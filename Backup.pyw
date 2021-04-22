import os
import time

time.sleep(10)
try:
    os.remove('tele_bot.pyw')
    os.rename('last.pyw', 'tele_bot.pyw')
    os.startfile('tele_bot.pyw')
except Exception as e:
    with open('backup_error.txt', 'a') as f:
        f.write(str(e))
