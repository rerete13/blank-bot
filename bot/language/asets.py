async def languages(topic: str, lan: str, data = None) -> str:
    '''data - user full name'''
    lan_choose = {
        'first-start': {
            'all':f'''
            🇺🇸Hi {data} this a bot for monitoring your spends even in relationship/frendship partner, please choose the language 
            \n\n🇺🇦Привіт {data}, це бот для моніторингу ваших витрат, навіть якщо ви з партнером у відносинах/дружбі, будь ласка, оберіть мову
            \n\n🇷🇺Привет {data}, это бот для мониторинга ваших расходов, даже если вы с партнером в отношениях/дружбе, пожалуйста, выберите язык
            \n\n
            ''',
        },
        'start': {
            'en':'🧾Send me your spends (145.33)',
            'ua':'🧾Надішліть мені свої витрати (145.33)',
            'ru':'🧾Отправьте мне свои расходы (145.33)'
        },
        'lan-change': {
            'en':'You have choose 🇺🇸english language. \nYou allways can change it with /lan',
            'ua':'Ви вибрали 🇺🇦українську мову. \nВи завжди можете змінити її за допомогою /lan',
            'ru':'Вы выбрали 🇷🇺русский язык. \nВы всегда можете изменить его с помощью /lan'
        },
    }
    return lan_choose[topic][lan]


