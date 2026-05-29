import random
import json

def load_manual(): #загрузка json
    with open("manual.json", "r", encoding="utf-8") as f:
        return json.load(f)

class Player:
    def __init__(self):
        self.max_health = 100 #макс хп
        self.health = 100 #текущее хп
        self.has_stone = False
#получение урона
    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
#хил
    def heal(self, amount):
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health
#Шкала здоровья
    def show_health(self):
        health_bar = "[" + "█" * (self.health // 5) + " " * ((self.max_health - self.health) // 5) + "]"
        return f"Здоровье: {health_bar} {self.health}/{self.max_health}"

#характеристики врагов
class Enemy:
    def __init__(self, name, health, damage):
        self.name = name #ник врага
        self.health = health #его хп
        self.damage = damage #урон
#жив ли
    def is_alive(self):
        return self.health > 0

#бой
def combat(player, enemy):
    print(f"\nБой!")
    print(f"Здоровье врага: {enemy.health}")
#проверка на живность
    while enemy.is_alive() and player.health > 0:
        print(f"\n{player.show_health()}")
        print("Выберите действие:")
        print("1 - Атака")
        print("2 - Защита")
        print("3 - Уклонение")

        try:
            action = int(input("Ваш выбор (1-3): "))
        except ValueError:
            print("Введите число от 1 до 3!")
            continue

        # урон игрока и врага
        player_damage = 0
        enemy_damage = enemy.damage

        if action == 1:  # Атака
            player_damage = random.randint(15, 25)
            print(f"Вы атакуете и наносите {player_damage} урона!")
        elif action == 2:  # Защита
            enemy_damage = max(0, enemy_damage - random.randint(5, 15))
            print("Вы защищаетесь от урона!")
        elif action == 3:  # Уклонение
            if random.random() < 0.6:  # 60% шанс уклониться.
                enemy_damage = 0
                print("Вы уклонились от атаки!")
            else:
                print("Уклонение не удалось!")
        else:
            print("Неверный выбор!")
            continue

        # Атака по врагу
        if player_damage > 0:
            enemy.health -= player_damage
            if enemy.health <= 0:
                enemy.health = 0
                print(f"Вы победили {enemy.name}!")
                return True

        # Атака врага
        if enemy.is_alive() and enemy_damage > 0:
            player.take_damage(enemy_damage)
            print(f"{enemy.name} атакует и наносит {enemy_damage} урона!")

            if player.health <= 0:
                print("Вы погибли..")
                input("\nНажмите Enter, чтобы выйти...")
                return False

    return player.health > 0

#хилка
def checkpoint_heal(player, location_name):
    print(f"\n{location_name}")
    print("Вы нашли безопасное место и можете восстановить силы!")
    old_health = player.health
    player.heal(50)
    print(f"Здоровье восстановлено: {old_health} => {player.health}")
    input("Нажмите Enter чтобы продолжить..")


def introduction():
    print("=" * 21)
    print("ТАИНСТВЕННЫЙ КОНТРАКТ")
    print("=" * 21)
    print("\nВы, закалённый в боях искатель приключений, уже видите дверь")
    print("в знаменитый трактир «МЕДЯЯЯЯЯТИНА», где на доске") #название от даши
    print("объявлений вас ждёт новая работа - охота на гоблинов.")
    print("\nНо ваш путь преградила худая, тенеподобная фигура в плаще..")

    print("\n— Прошу прощения, - голос незнакомца тихий, но твёрдый.")
    print("— Мне сказали, что вы ищете.. прибыльные контракты.")
    print("Охота на гоблинов оплачивается серебром.")
    print("То, что предлагаю я, принесёт вам славу.")
    print("\nОн протягивает чёрный камень с мерцающими рунами.")

    while True:
        print("\n1 - Взять камень и согласиться")
        print("2 - Отказаться и пойти в трактир")

        try:
            choice = int(input("Ваш выбор: "))
            if choice == 1:
                print("\n- Мудрое решение, - кивает незнакомец. - Следуйте за камнем..")
                return True
            elif choice == 2:
                print("\n- Как знаете, - пожимает плечами незнакомец. Удачи с гоблинами.")
                print("\nИгра окончена. Вы провели остаток дней, охотясь на гоблинов.")
                input("\nНажмите Enter, чтобы выйти...")
                return False
            else:
                print("Выберите 1 или 2!")
        except ValueError:
            print("Введите число!")


def final_confrontation(player):
    print("\n" + "=" * 12)
    print("СЕРДЦЕ ТЕНИ")
    print("=" * 12)

    print("\nВы достигаете сердца подземелья - зала, где на пьедестале")
    print("покоится древний артефакт, испускающий зловещее свечение.")
    print("Это «Сердце Тени» - источник тёмной магии.")

    print("\nИз теней появляется знакомый силуэт..")
    print("Незнакомец снимает капюшон, открывая лицо, усеянное")
    print("древними морщинами и холодными глазами.")

    print("\n- Благодарю тебя, ключ. Ты отпер дверь, которую я,")
    print("будучи связан клятвой, не мог отпереть сам.")
    print("\nОказывается, он - бессмертный лич, создавший этот артефакт!")

    while True:
        print("\nЧто вы сделаете с сердцем Тени?")
        print("1 - Уничтожить артефакт")
        print("2 - Оставить артефакт и принять проклятие")

        try:
            choice = int(input("Ваш выбор (1-2): "))
            if choice == 1:
                print("\nВы вкладываете всю силу в удар по артефакту!")
                print("Ослепительная вспышка.. грохот.. тишина..")
                print("Вы уничтожаете источник зла и жертвуете собой")
                print("Мир спасён, но о вашем подвиге никто не узнает..")
                return "heroic"
            elif choice == 2:
                print("\nПроклятие вступает в силу. Выход исчезает.")
                print("Вы понимаете, что теперь вы - новый бессмертный Страж.")
                print("Вы обречены вечно защищать источник зла..")
                print("В ожидании следующего «ключа»..")
                return "cursed"
            else:
                print("Выберите 1 или 2!")
        except ValueError:
            print("Введите число!")


def main():
    guide = load_manual()
    print(guide['title'])
    print(guide['game']['description'])
    input()

    player = Player()
    # Введение отказ от камня
    if not introduction():
        return

    player.has_stone = True
    print("\nКамень в вашей руке начинает светиться и указывает путь..")
    print("Вы спускаетесь в древнее подземелье.")
    input("\nНажмите Enter чтобы продолжить..")

    # бой 1
    print("\n" + "=" * 35)
    print("УРОВЕНЬ 1: ЗАБЫТЫЕ КАТАКОМБЫ")
    print("=" * 35)

    print("\nВы входите в сырые катакомбы. В воздухе пахнет плесенью и пылью.")
    print("Из темноты на вас нападает Теневой страж!")

    if not combat(player, Enemy("Теневой страж", 60, 10)):
        return

    # хилка 1
    checkpoint_heal(player, "ДРЕВНИЙ РОДНИК")

    # бой 2
    print("\n" + "=" * 30)
    print("УРОВЕНЬ 2: ЗАЛ РУН")
    print("=" * 30)

    print("\nВы попадаете в огромный зал, стены которого покрыты светящимися рунами.")
    print("Призрачный рыцарь выходит из стены!")

    if not combat(player, Enemy("Призрачный рыцарь", 80, 15)):
        return

    # хилка 2
    checkpoint_heal(player, "СВЯТИЛИЩЕ ДРЕВНИХ")

    # бой 3
    print("\n" + "=" * 35)
    print("УРОВЕНЬ 3: ЧЕРТОГИ ТЕНЕЙ")
    print("=" * 35)

    print("\nТемнота сгущается. Воздух становится тяжёлым от магии.")
    print("Хранитель Бездны, огромное существо из тьмы, преграждает путь!")

    if not combat(player, Enemy("Хранитель Бездны", 90, 15)):
        return

    # Финал
    ending = final_confrontation(player)

    # Эпилог
    print("\n" + "=" * 9)
    print("ЭПИЛОГ")
    print("=" * 9)

    if ending == "heroic":
        print("\nПроходят годы.. В другом трактире другой молодой")
        print("искатель приключений собирается на охоту на гоблинов.")
        print("К нему подходит худая фигура в плаще и протягивает")
        print("чёрный рунический камень..")
    else:
        print("\nВремя теряет смысл. Вы стоите на страже в вечной тьме,")
        print("слушая шепот Сердца Тени. Иногда вам кажется, что")
        print("где-то наверху снова звенят мечи и кто-то идёт")
        print("по вашему старому пути..")

    print("\nИгра завершена. Спасибо за прохождение!")
    input("\nНажмите Enter, чтобы выйти...")


if __name__ == "__main__":
    main()