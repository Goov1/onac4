# made by Goov.
# ver 1.0 RELEASE.
import random
import time
import sys

ldoor = "open"
rdoor = "open"
vendoor = "open"

def acat_attack(ldoor, rdoor):
    if rdoor == "open":
        print("+ На вас напали с правой стороны. Вы проиграли +")
        sys.exit()
    if rdoor == "close":
        print("+ На вас напали с правой стороны. Вы защитились. Все двери открылись. +")
def bcat_attack(ldoor, rdoor):
    if ldoor == "open":
        print("+ На вас напали с левой стороны. Вы проиграли +")
    elif ldoor == "close":
        print("+ На вас напали с левой стороны. Вы защитились. Все двери открылись. +")
def ccat_attack(ldoor, rdoor, vendoor):
    if vendoor == "open":
        print("+ На вас напали с вентиляции. Вы проиграли +")
    elif vendoor == "close":
        print("+ На вас напали с вентиляции. Вы защитились. Все двери открылись. +")
def dcat_attack(ldoor, rdoor):
    print("* Скример последнего кота *")
    time.sleep(5)
    print("+ Вы прошли onac 4! Если вы проходили предыдущие части, тогда вы прошли весь onac! +")
    print("+ Мне уже скучно это писать. Субтитров не будет, всё зделал Goov;) +")
    sys.exit()
print("-----ONAC 4-----")
print("-----START (s)-----")
print("-----HELP (h)-----")
a = input("~1: ")
if a == "s":
    print("* Несколько мяу одновременно *")
    b = int(input("~1: "))
    if b == 1:
        ldoor = "open"
        print("+ Левая дверь открылась. +")
    elif b == 2:
        rdoor = "open"
        print("+ Правая дверь открылась. +")
    elif b == 3:
        vendoor = "open"
        print("+ Вентиляция открылась. +")
    elif b == 4:
        ldoor = "close"
        print("+ Левая дверь закрылась. +")
    elif b == 5:
        rdoor = "close"
        print("+ Правая дверь закрылась. +")
    elif b == 6:
        vendoor = "close"
        print("+ Вентиляция закрылась. +")
    acat_attack(ldoor, rdoor)
    ldoor = "open"
    rdoor = "open"
    print("Слишком быстро...")
    b = int(input("~1: "))
    if b == 1:
        ldoor = "open"
        print("+ Левая дверь открылась. +")
    elif b == 2:
        rdoor = "open"
        print("+ Правая дверь открылась. +")
    elif b == 3:
        vendoor = "open"
        print("+ Вентиляция открылась. +")
    elif b == 4:
        ldoor = "close"
        print("+ Левая дверь закрылась. +")
    elif b == 5:
        rdoor = "close"
        print("+ Правая дверь закрылась. +")
    elif b == 6:
        vendoor = "close"
        print("+ Вентиляция закрылась. +")
    bcat_attack(ldoor, rdoor)
    ldoor = "open"
    rdoor = "open"
    print("Я не успеваю...")
    b = int(input("~1: "))
    if b == 1:
        ldoor = "open"
        print("+ Левая дверь открылась. +")
    elif b == 2:
        rdoor = "open"
        print("+ Правая дверь открылась. +")
    elif b == 3:
        vendoor = "open"
        print("+ Вентиляция открылась. +")
    elif b == 4:
        ldoor = "close"
        print("+ Левая дверь закрылась. +")
    elif b == 5:
        rdoor = "close"
        print("+ Правая дверь закрылась. +")
    elif b == 6:
        vendoor = "close"
        print("+ Вентиляция закрылась. +")
    ccat_attack(ldoor, rdoor, vendoor)
    ldoor = "open"
    rdoor = "open"
    print("Мяяяууу!")
    b = int(input("~1: "))
    if b == 1:
        ldoor = "open"
        print("+ Левая дверь открылась. +")
    elif b == 2:
        rdoor = "open"
        print("+ Правая дверь открылась. +")
    elif b == 3:
        vendoor = "open"
        print("+ Вентиляция открылась. +")
    elif b == 4:
        ldoor = "close"
        print("+ Левая дверь закрылась. +")
    elif b == 5:
        rdoor = "close"
        print("+ Правая дверь закрылась. +")
    elif b == 6:
        vendoor = "close"
        print("+ Вентиляция закрылась. +")
    dcat_attack(ldoor, rdoor)

elif a == "h":
    print("-----КОМАНДЫ-----")
    print("1-открыть левую дверь.")
    print("2-открыть правую дверь.")
    print("3-открыть вентиляцию.")
    print("4-закрыть левую дверь.")
    print("5-закрыть правую дверь.")
    print("6-закрыть вентиляцию")
    print("Перезапустите игру.")