"""
Логика проведения гонки
"""

import time
from typing import List
from dragon import Dragon
from track import Track


class Race:
    def __init__(self, track: Track, dragons: List[Dragon]):
        self.track = track
        self.dragons = dragons
        self.finished = False
        self.winner = None

    def start(self):
        print(f"\n🔥 Гонка начинается на трассе: {self.track.name}!")
        print(f"Участники: {[d.name for d in self.dragons]}\n")

        while not self.finished:
            for dragon in self.dragons:
                # Простая симуляция движения
                move = dragon.accelerate()
                print(f"{dragon.name} продвинулся на {move:.1f}м. Позиция: {dragon.position:.1f}м")

                if dragon.position >= self.track.length:
                    self.finished = True
                    self.winner = dragon
                    break

            time.sleep(0.5)  # Небольшая пауза для наглядности

        print(f"\n🏆 Победитель: {self.winner.name}!")
        print("Гонка завершена!")
