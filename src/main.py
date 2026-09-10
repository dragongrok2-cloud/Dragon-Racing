"""
Dragon Racing - Main entry point
Гонки на драконах
"""

from dragon import Dragon
from track import Track
from race import Race


def main():
    print("🐉 Добро пожаловать в Dragon Racing!")
    print("Подготовка к гонке...")

    # Создаём драконов-участников
    player_dragon = Dragon(name="Пламенный", speed=85, maneuverability=90, stamina=80)
    rival_dragon = Dragon(name="Грозовой", speed=88, maneuverability=75, stamina=85)

    # Создаём трассу
    track = Track(name="Небесный Пик", length=5000, difficulty="hard")

    # Запускаем гонку
    race = Race(track=track, dragons=[player_dragon, rival_dragon])
    race.start()


if __name__ == "__main__":
    main()
