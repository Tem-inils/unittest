import sqlite3

connection = sqlite3.connect('database.db')

sql = connection.cursor()

sql.execute('CREATE TABLE IF NOT EXISTS user (id INTEGER, name TEXT, number TEXT, balance INTEGER);')



def deposit(id, amount):
    db = sqlite3.connect('database.db')
    sql = db.cursor()
    sql.execute('UPDATE user SET balance = balance + ? WHERE id = ?;', (amount, id))
    db.commit()
    db.close()
    print("Баланс успешно пополнен.")


def withdraw(id, amount):
    db = sqlite3.connect('database.db')
    sql = db.cursor()
    sql.execute('UPDATE user SET balance = balance - ? WHERE id = ?;', (amount, id))
    db.commit()
    db.close()
    print("Средства успешно сняты с баланса.")

def check_balance(id):
    db = sqlite3.connect('database.db')
    sql = db.cursor()
    sql.execute('SELECT balance FROM user WHERE id=?;', (id,))
    result = sql.fetchone()
    db.close()
    if result:
        print(f"Баланс: {result[0]}")
    else:
        print("Пользователь с указанным ID не найден.")

def calculate_interest(id, months):
    db = sqlite3.connect('database.db')
    sql = db.cursor()
    sql.execute('SELECT balance FROM user WHERE id=?;', (id,))
    result = sql.fetchone()
    db.close()
    if result and result[0] is not None:
        balance = result[0]
        interest_rate = 0.05  # Процентная ставка (5%)
        interest = balance * interest_rate * (months / 12)
        print(f"Прогнозируемый вклад через {months} месяцев: {balance + interest}")
    else:
        print("Пользователь с указанным ID не найден или баланс отсутствует.")


while True:
    print("\nМеню:")
    print("1. Пополнить баланс")
    print("2. Снять средства с баланса")
    print("3. Проверить баланс")
    print("4. Рассчитать вклад")
    print("5. Выход")

    choice = input("Выберите действие (1/2/3/4/5): ")


    if choice == '1':
        user_id = int(input("Введите ID пользователя: "))
        amount = float(input("Введите сумму для пополнения: "))
        deposit(user_id, amount)
    elif choice == '2':
        user_id = int(input("Введите ID пользователя: "))
        amount = float(input("Введите сумму для снятия: "))
        withdraw(user_id, amount)
    elif choice == '3':
        user_id = int(input("Введите ID пользователя: "))
        check_balance(user_id)
    elif choice == '4':
        user_id = int(input("Введите ID пользователя: "))
        months = int(input("Введите количество месяцев: "))
        calculate_interest(user_id, months)
    elif choice == '5':
        break
    else:
        print("Неверный выбор. Попробуйте ещё раз.")