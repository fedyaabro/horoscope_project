import random
from pprint import pprint

times = ["утром", "днём", "вечером", "ночью", "после обеда", "перед сном"]
advices = ["ожидайте", "предостерегайтесь", "будьте открыты для"]
promises = ["гостей из забытого прошлого", "встреч со старыми знакомыми", "неожиданного праздника", "приятных перемен"]


def gen_prophecies(num_sent=5,num_promises=3):
    i = 0
    generated_prophecies = []
    while i < num_sent:
        j = 0
        middle_list = []
        while j < 3:  # генерим список из 3 предсказания
            t_inx = random.choice(times)
            a_inx = random.choice(advices)
            p_inx = random.choice(promises)
            full_phrases = t_inx.title() + ' ' + a_inx + ' ' + p_inx + '.'
            # print(full_phrases)
            j += 1
            generated_prophecies.append(full_phrases)
        i += 1
    return generated_prophecies
    # print(middle_list) - check
