# -*- coding: utf-8 -*-
import sys
import datetime
import config

sys.path.insert(1, '/apps')


def nowtime():
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day

    return now, year, month, day         


def the_countdown_till_summer():  # сколько осталось до лета
    now, year, month, day = nowtime()

    summer = datetime.datetime(year, config.beginning_summer_holidays_month, config.beginning_summer_holidays_day)
    summer_end = datetime.datetime(year, config.end_summer_holidays_month, config.end_summer_holidays_day)

    remained_summer = summer - now
    mm, ss = divmod(remained_summer.seconds, 60)
    hh, mm = divmod(mm, 60)

    days = remained_summer.days

    if int(days) <= 0:
        summer = datetime.datetime(year + 1, config.beginning_summer_holidays_month,
                                   config.beginning_summer_holidays_day)
        remained_summer = summer - now
        days = remained_summer.days

    summer_ans = ('До летних каникул осталось: {} дн. {} ч. {} мин. {} сек.⏳'.format(days, hh, mm, ss))
    
    if summer <= datetime.datetime(year, month, day) <= summer_end:
        end_summer = datetime.datetime(year, config.end_summer_holidays_month, config.end_summer_holidays_day) - now

        mm, ss = divmod(end_summer.seconds, 60)
        hh, mm = divmod(mm, 60)

        summer_ans = ('Сейчас летние каникулы☀ \n\nДо их конца осталось: \n{} дн. {} ч. {} мин. {} сек.⏳'.
                      format(end_summer.days, hh, mm, ss))

        return summer_ans
    else:
        return summer_ans


def before_the_holidays_computing():  # считаеться сколько осталось до всех каникул времени
    now, year, month, day = nowtime()

    autumn_holidays = datetime.datetime(year, config.beginning_autumn_holidays_month,
                                        config.beginning_autumn_holidays_day)

    summer_holidays = datetime.datetime(year, config.beginning_summer_holidays_month,
                                        config.beginning_summer_holidays_day)

    spring_holidays = datetime.datetime(year, config.beginning_spring_holidays_month,
                                        config.beginning_spring_holidays_day)

    winter_holidays = datetime.datetime(year, config.beginning_winter_holidays_month,
                                        config.beginning_winter_holidays_day)

    # корекктируются значения ,если год пересек значение начала каникул,то есть добавляется год
    if month > config.beginning_summer_holidays_month: 
        year = year + 1
        summer_holidays = datetime.datetime(year, config.beginning_summer_holidays_month,
                                            config.beginning_summer_holidays_day)

    if month > config.beginning_spring_holidays_month:
        year = year + 1
        spring_holidays = datetime.datetime(year, config.beginning_spring_holidays_month,
                                            config.beginning_spring_holidays_day)

    if month > config.beginning_autumn_holidays_month:
        year = year + 1
        autumn_holidays = datetime.datetime(year, config.beginning_autumn_holidays_month,
                                            config.beginning_autumn_holidays_day)

    if month > config.beginning_winter_holidays_month:
        year = year + 1
        winter_holidays = datetime.datetime(year, config.beginning_winter_holidays_month,
                                            config.beginning_winter_holidays_day)

    # считаеться сколько осталось до всех каникул времени

    remained_until_summer = summer_holidays - now
    remained_until_autumn = autumn_holidays - now
    remained_until_spring = spring_holidays - now
    remained_until_winter = winter_holidays - now

    return remained_until_summer, remained_until_autumn, remained_until_spring, remained_until_winter


def before_the_holidays_text():  # полученых значения конвертируются в текст

    remained_until_summer, remained_until_autumn, remained_until_spring, remained_until_winter \
        = before_the_holidays_computing()

    if remained_until_summer < remained_until_autumn and remained_until_summer < remained_until_spring \
            and remained_until_summer < remained_until_winter:

        mm, ss = divmod(remained_until_summer.seconds, 60)
        hh, mm = divmod(mm, 60)

        remained_until_summer_text = ('До летних каникул осталось: {} дн. {} ч. {} мин. {} сек.⏳'.
                                      format(remained_until_summer.days, hh, mm, ss))

        return remained_until_summer_text
        
    if remained_until_autumn < remained_until_summer and remained_until_autumn < remained_until_spring \
            and remained_until_autumn < remained_until_winter:

        mm, ss = divmod(remained_until_autumn.seconds, 60)
        hh, mm = divmod(mm, 60)

        remained_until_autumn_text = ('До осенних каникул осталось: {} дн. {} ч. {} мин. {} сек.⏳'.
                                      format(remained_until_autumn.days, hh, mm, ss))

        return remained_until_autumn_text

    if remained_until_spring < remained_until_autumn and remained_until_spring < remained_until_summer \
            and remained_until_spring < remained_until_winter:

        mm, ss = divmod(remained_until_spring.seconds, 60)
        hh, mm = divmod(mm, 60)

        remained_until_spring_text = ('До весенних каникул осталось: {} дн. {} ч. {} мин. {} сек.⏳'.
                                      format(remained_until_spring.days, hh, mm, ss))

        return remained_until_spring_text

    if remained_until_winter < remained_until_autumn and remained_until_winter < remained_until_spring \
            and remained_until_winter < remained_until_summer:

        mm, ss = divmod(remained_until_winter.seconds, 60)
        hh, mm = divmod(mm, 60)

        remained_until_winter_text = ('До зимних каникул осталось: {} дн. {} ч. {} мин. {} сек.⏳'.
                                      format(remained_until_winter.days, hh, mm, ss))

        return remained_until_winter_text


def identification_holidays():  # проверка сейчас ли каникулы
    now, year, month, day = nowtime()
    remained_until_holidays = before_the_holidays_text()

    if datetime.datetime(year, config.beginning_summer_holidays_month, config.beginning_summer_holidays_day) \
            <= datetime.datetime(year, month, day)\
            <= datetime.datetime(year, config.end_summer_holidays_month, config.end_summer_holidays_day):

        holidays = "summer"
        end_holidays_text = until_the_end_o_the_holidays(holidays)
        return end_holidays_text
                
    elif datetime.datetime(year, config.beginning_winter_holidays_month, config.beginning_winter_holidays_day) \
            <= datetime.datetime(year, month, day)\
            <= datetime.datetime(year, config.end_winter_holidays_month, config.end_winter_holidays_day):

        holidays = "winter"
        end_holidays_text = until_the_end_o_the_holidays(holidays)
        return end_holidays_text
           
    elif datetime.datetime(year, config.beginning_spring_holidays_month, config.beginning_spring_holidays_day) \
            <= datetime.datetime(year, month, day)\
            <= datetime.datetime(year, config.end_spring_holidays_month, config.end_spring_holidays_day):

        holidays = "spring"
        end_holidays_text = until_the_end_o_the_holidays(holidays)
        return end_holidays_text
    
    elif datetime.datetime(year, config.beginning_autumn_holidays_month, config.beginning_autumn_holidays_day) \
            <= datetime.datetime(year, month, day) \
            <= datetime.datetime(year, config.end_autumn_holidays_month, config.end_autumn_holidays_day):

        holidays = "autumn"
        end_holidays_text = until_the_end_o_the_holidays(holidays)
        return end_holidays_text
    else:
        return remained_until_holidays
    

def until_the_end_o_the_holidays(holidays):  # сколько осталось до конца каникул
    now, year, month, day = nowtime()

    if holidays == "summer":
        end_summer = datetime.datetime(year, config.end_summer_holidays_month, config.end_summer_holidays_day) - now

        mm, ss = divmod(end_summer.seconds, 60)
        hh, mm = divmod(mm, 60)

        end_holidays_text = ('Сейчас летние каникулы☀ \n\nДо их конца осталось: \n{} дн. {} ч. {} мин. {} сек.⏳'.
                             format(end_summer.days, hh, mm, ss))

        return end_holidays_text
    
    elif holidays == "spring":
        end_spring = datetime.datetime(year,config.end_spring_holidays_month,config.end_spring_holidays_day) - now

        mm, ss = divmod(end_spring.seconds, 60)
        hh, mm = divmod(mm, 60)

        end_holidays_text = ('Сейчас весенние каникулы🍃 \n\nДо их конца осталось:\n{} дн. {} ч. {} мин. {} сек.⏳'.
                             format(end_spring.days, hh, mm, ss))

        return end_holidays_text

    elif holidays == "autumn":
        end_autumn = datetime.datetime(year,config.end_autumn_holidays_month, config.end_autumn_holidays_day) - now

        mm, ss = divmod(end_autumn.seconds, 60)
        hh, mm = divmod(mm, 60)

        end_holidays_text = ('Сейчас осение каникулы🍂 \n\nДо их конца осталось:\n{} дн. {} ч. {} мин. {} сек.⏳'.
                             format(end_autumn.days, hh, mm, ss))
        return end_holidays_text

    elif holidays == "winter":
        end_winter = datetime.datetime(year, config.end_winter_holidays_month,config.end_winter_holidays_day) - now

        mm, ss = divmod(end_winter.seconds, 60)
        hh, mm = divmod(mm, 60)

        end_holidays_text = ('Сейчас зимние каникулы❄ \n\nДо их конца осталось:\n{} дн. {} ч. {} мин. {} сек.⏳'.
                             format(end_winter.days, hh, mm, ss))

        return end_holidays_text
