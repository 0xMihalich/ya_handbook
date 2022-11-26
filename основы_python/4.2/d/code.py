def month(num, lang="ru"):
    return {1: {"ru": "Январь", "en": "January"}, 2: {"ru": "Февраль", "en": "February"},
            3: {"ru": "Март", "en": "March"}, 4: {"ru": "Апрель", "en": "April"},
            5: {"ru": "Май", "en": "May"}, 6: {"ru": "Июнь", "en": "June"},
            7: {"ru": "Июль", "en": "July"}, 8: {"ru": "Август", "en": "August"},
            9: {"ru": "Сентябрь", "en": "September"}, 10: {"ru": "Октябрь", "en": "October"},
            11: {"ru": "Ноябрь", "en": "November"}, 12: {"ru": "Декабрь", "en": "December"}}[num][lang]
