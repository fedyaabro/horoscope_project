import random


times = ["утром", "днём", "вечером", "ночью", "после обеда", "перед сном"]
advices = ["ожидайте", "предостерегайтесь", "будьте открыты для"]
promises = ["гостей из забытого прошлого", "встреч со старыми знакомыми", "неожиданного праздника", "приятных перемен"]

i = 0
generated_prophecies = []
while i < 5:
    j = 0
    middle_list =[]
    while j < 3: # генерим список из 3 предсказания
        t_inx = random.choice(times)
        a_inx = random.choice(advices)
        p_inx = random.choice(promises)
        full_phrase = t_inx.title() + ' ' + a_inx + ' ' + p_inx + '.'
        # print(full_phrase) - check
        j += 1
        middle_list.append(full_phrase)
    i += 1
    generated_prophecies.append(middle_list)

# print(middle_list) - check
print(generated_prophecies)