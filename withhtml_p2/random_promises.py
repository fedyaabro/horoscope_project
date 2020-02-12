import random
from pprint import pprint

times = ["утром", "днём", "вечером", "ночью", "после обеда", "перед сном"]
advices = ["ожидайте", "предостерегайтесь", "будьте открыты для"]
promises = ["гостей из забытого прошлого", "встреч со старыми знакомыми", "неожиданного праздника", "приятных перемен"]


def gen_prophecies(num_sent=5,num_promises=3):
    generated_prophecies = []
    for i in range(num_sent):
        for j in range(num_promises):  # генерим список из 3 предсказания
            t_inx = random.choice(times)
            a_inx = random.choice(advices)
            p_inx = random.choice(promises)
            full_phrases = f"{t_inx.title()} {a_inx} {p_inx}."
            # print(full_phrases)
            generated_prophecies.append(full_phrases)
    return generated_prophecies


