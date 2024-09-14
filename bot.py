import discord
from discord.ext import commands
import datetime
import random

# Настройки для бота
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Мы вошли как {bot.user}')

# Команды
@bot.command(help="Приветствие от бота.")
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command(help="Повторить 'he' указанное количество раз (по умолчанию 5).")
async def heh(ctx, count_heh: int = 5):
    await ctx.send("he" * count_heh)

@bot.command(help="Показать текущее время и дату.")
async def time(ctx):
    now = datetime.datetime.now()
    await ctx.send(f"Текущая дата и время: {now.strftime('%Y-%m-%d %H:%M:%S')}")

@bot.command(help="Сгенерировать случайное число в заданном диапазоне.")
async def random_number(ctx, lower: int, upper: int):
    random_number = random.randint(lower, upper)
    await ctx.send(f"Случайное число от {lower} до {upper}: {random_number}")

@bot.command(help="Информация о сервере.")
async def serverinfo(ctx):
    guild = ctx.guild
    await ctx.send(f"Название сервера: {guild.name}\nКоличество участников: {guild.member_count}")

@bot.command(help="Получить случайную шутку.")
async def joke(ctx):
    jokes = [
        "Почему программисты не любят природу? Потому что в ней слишком много ошибок.",
        "Как программист меняет лампочку? Он не меняет, это аппаратная проблема.",
        "Почему у программистов нет друзей? Потому что они всегда работают с кодом."
    ]
    await ctx.send(random.choice(jokes))

@bot.command(help="Получить случайный факт.")
async def fact(ctx):
    facts = [
        "Медузы не имеют мозга.",
        "Слон – единственное животное, которое не может прыгать.",
        "Существуют более 2000 видов комаров."
    ]
    await ctx.send(random.choice(facts))

@bot.command(help="Бросить кости с указанным количеством сторон.")
async def roll(ctx, sides: int):
    roll_result = random.randint(1, sides)
    await ctx.send(f"Вы бросили кости и получили: {roll_result}")

@bot.command(help="Подбросить монету.")
async def flip(ctx):
    result = random.choice(["Орёл", "Решка"])
    await ctx.send(f"Монета упала на: {result}")

@bot.command(help="Сделать выбор между вариантами.")
async def choose(ctx, *choices):
    if len(choices) > 1:
        choice = random.choice(choices)
        await ctx.send(f"Я выбираю: {choice}")
    else:
        await ctx.send("Укажите как минимум два варианта для выбора.")

@bot.command(help="Получить случайную цитату.")
async def quote(ctx):
    quotes = [
        "Будь собой; все остальные уже заняты. - Оскар Уайльд",
        "Программирование - это искусство, а не наука. - Кен Томпсон",
        "Самая большая ошибка, которую вы можете сделать, это бояться сделать ошибку. - Эллен ДеДженерес"
    ]
    await ctx.send(random.choice(quotes))

@bot.command(help="Информация о пользователе.")
async def userinfo(ctx, user: discord.User = None):
    user = user or ctx.author
    await ctx.send(f"Пользователь: {user.name}\nID: {user.id}\nСоздан: {user.created_at.strftime('%Y-%m-%d %H:%M:%S')}")

@bot.command(help="Получить аватар пользователя.")
async def avatar(ctx, user: discord.User = None):
    user = user or ctx.author
    await ctx.send(user.avatar.url)

@bot.command(help="Проверить задержку бота.")
async def ping(ctx):
    await ctx.send(f"Пинг: {round(bot.latency * 1000)}ms")

@bot.command(help="Выполнить математическое выражение.")
async def math(ctx, expression: str):
    try:
        result = eval(expression)
        await ctx.send(f"Результат: {result}")
    except Exception as e:
        await ctx.send("Ошибка в выражении.")

@bot.command(help="Игра в Камень, Ножницы, Бумага.")
async def rps(ctx, user_choice: str):
    user_choice = user_choice.lower()
    bot_choice = random.choice(['камень', 'ножницы', 'бумага'])
    if user_choice == bot_choice:
        await ctx.send(f"Ничья! Я выбрал {bot_choice}.")
    elif (user_choice == 'камень' and bot_choice == 'ножницы') or \
         (user_choice == 'ножницы' and bot_choice == 'бумага') or \
         (user_choice == 'бумага' and bot_choice == 'камень'):
        await ctx.send(f"Вы выиграли! Я выбрал {bot_choice}.")
    else:
        await ctx.send(f"Вы проиграли! Я выбрал {bot_choice}.")

@bot.command(help="Повторить указанный текст.")
async def repeat(ctx, *, text: str):
    await ctx.send(text)

@bot.command(help="Получить вдохновляющую цитату.")
async def inspire(ctx):
    inspirations = [
        "Действуйте так, как будто то, что вы делаете, имеет значение. Это имеет значение.",
        "Секрет успеха в том, чтобы начать.",
        "Не бойтесь делать ошибки — бойтесь не учиться на них."
    ]
    await ctx.send(random.choice(inspirations))

@bot.command(help="Выбрать случайный цвет.")
async def choosecolor(ctx):
    colors = ["Красный", "Зеленый", "Синий", "Желтый", "Фиолетовый", "Оранжевый"]
    await ctx.send(f"Случайный цвет: {random.choice(colors)}")

@bot.command(help="Получить цитату дня.")
async def quoteofday(ctx):
    quotes_of_day = [
        "Каждый день — это новая возможность.",
        "Не позволяйте вчерашнему дню занимать слишком много места в сегодняшнем.",
        "Сложности — это то, что делает жизнь интересной."
    ]
    await ctx.send(random.choice(quotes_of_day))

@bot.command(help="Выполнить арифметические операции.")
async def calc(ctx, num1: float, operation: str, num2: float):
    if operation == '+':
        await ctx.send(f"Результат: {num1 + num2}")
    elif operation == '-':
        await ctx.send(f"Результат: {num1 - num2}")
    elif operation == '*':
        await ctx.send(f"Результат: {num1 * num2}")
    elif operation == '/':
        if num2 != 0:
            await ctx.send(f"Результат: {num1 / num2}")
        else:
            await ctx.send("Ошибка: Деление на ноль.")
    else:
        await ctx.send("Неизвестная операция.")

@bot.command(help="Получить случайный мем.")
async def meme(ctx):
    memes = [
        "https://i.imgflip.com/1bij.jpg",
        "https://i.imgflip.com/1ihzfe.jpg",
        "https://i.imgflip.com/4t0m5.jpg"
    ]
    await ctx.send(random.choice(memes))

@bot.command(help="Получить факт дня.")
async def factofday(ctx):
    facts_of_day = [
        "Человеческий мозг состоит на 75% из воды.",
        "Кошки могут прыгать до шести раз длины своего тела.",
        "Слон — единственное животное, которое не может прыгать."
    ]
    await ctx.send(random.choice(facts_of_day))

@bot.command(help="Получить совет.")
async def advice(ctx):
    advices = [
        "Не бойтесь пробовать новое.",
        "Слушайте свое сердце.",
        "Не откладывайте на завтра то, что можете сделать сегодня."
    ]
    await ctx.send(random.choice(advices))

@bot.command(help="Получить случайный вопрос для викторины.")
async def trivia(ctx):
    trivia_questions = [
        "Какой самый большой океан на Земле? (Ответ: Тихий)",
        "Сколько планет в Солнечной системе? (Ответ: 8)",
        "Кто написал 'Гарри Поттера'? (Ответ: Дж.К. Роулинг)"
    ]
    await ctx.send(random.choice(trivia_questions))

@bot.command(name='commands', help="Показать список доступных команд.")
async def commands_list(ctx):
    help_text = (
        "**Информация**:\n"
        "$hello - Приветствие от бота.\n"
        "$time - Показать текущее время и дату.\n"
        "$serverinfo - Информация о сервере.\n"
        "$userinfo - Информация о пользователе.\n"
        "$avatar - Получить аватар пользователя.\n"
        "$joined - Узнать, когда участник присоединился к серверу.\n\n"

        "**Игры**:\n"
        "$rps <камень|ножницы|бумага> - Игра в Камень, Ножницы, Бумага.\n"
        "$roll <число> - Бросить кости с указанным количеством сторон.\n"
        "$flip - Подбросить монету.\n"
        "$choose <вариант1> <вариант2> ... - Сделать выбор между вариантами.\n"
        "$poll <вопрос> <вариант1> <вариант2> ... - Создать опрос.\n\n"

        "**Развлечения**:\n"
        "$joke - Получить случайную шутку.\n"
        "$fact - Получить случайный факт.\n"
        "$quote - Получить случайную цитату.\n"
        "$inspire - Получить вдохновляющую цитату.\n"
        "$meme - Получить случайный мем.\n"
        "$factofday - Получить факт дня.\n"
        "$advice - Получить совет.\n"
        "$trivia - Получить случайный вопрос для викторины.\n\n"

        "**Математика**:\n"
        "$math <выражение> - Выполнить математическое выражение.\n"
        "$calc <число1> <операция> <число2> - Выполнить арифметические операции.\n"
        "$random_number <min> <max> - Генерация случайного числа в заданном диапазоне.\n\n"

        "**Общие команды**:\n"
        "$heh [количество] - Повторить 'he' указанное количество раз (по умолчанию 5).\n"
        "$ping - Проверить задержку бота.\n"
        "$choosecolor - Выбрать случайный цвет.\n"
        "$quoteofday - Получить цитату дня.\n"
        "$repeat <текст> - Повторить указанный текст."
    )
    await ctx.send(help_text)

