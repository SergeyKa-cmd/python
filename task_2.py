# -*- coding: utf-8 -*-
import re

glasn = r"[уеёыаоэяиью]"
B_glasn = r"[УЕЁЫAОЭЯИЮ]"
soglasn = r"[йцкнгшщзхъфвпрлджчсмтбъ]"
B_soglasn = r"[ЙЦКНГШЩЗХФВПРЛДЖЧСМТБ]"

def razbor_strok(glas, soglas, bglas, bsoglas):
    stroki = int(input("Введите кол-во строк: "))
    for q in range(stroki):
        count_glas, count_soglas = 0, 0
        stroka = input("Введите строку: ")
        print(stroka)
        for i in range(len(stroka)):
            if re.search(glas, stroka[i]):
                count_glas += 1
            elif re.search(soglas, stroka[i]):
                count_soglas += 1
            elif re.search(bsoglas, stroka[i]):
                count_soglas += 1
            elif re.search(bglas, stroka[i]):
                count_glas += 1    
            else:
                continue
        print("Гласных: ", count_glas)
        print("Согласных: ", count_soglas)
razbor_strok(glasn, soglasn, B_glasn, B_soglasn)        