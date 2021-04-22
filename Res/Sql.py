import sqlite3

conn = sqlite3.connect("Res/logs.db")  # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()

# Создание таблицы
cursor.execute("""CREATE TABLE Action (Action text, message text, 'data time' text)""")
