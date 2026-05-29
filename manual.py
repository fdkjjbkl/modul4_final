import json

def create_manual_json():
    guide_data = {
        "title": "Таинственный контракт",
        "version": "1.0",
        "game": {
            "description": "Ролевая игра с боями и выбором пути",
            "combat_rules": {
                "attack": "Наносит 15-25 урона",
                "defense": "Снижает урон на 5-15",
                "evasion": "60% шанс уклониться от атаки"
            },
            "tips": [
                "Используйте защиту при низком здоровье",
                "После каждого боя есть место для восстановления"
            ]
        },
        "how_to_play": "В бою выбирайте действие (1-3). Побеждайте врагов, чтобы пройти дальше."
    }
    with open("manual.json", "w", encoding="utf-8") as file:
        json.dump(guide_data, file, ensure_ascii=False, indent=4)
create_manual_json()