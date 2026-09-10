"""
Класс трассы для гонок на драконах
"""

class Track:
    def __init__(self, name: str, length: int, difficulty: str = "medium"):
        self.name = name
        self.length = length          # Длина трассы в метрах
        self.difficulty = difficulty  # easy / medium / hard

        # Модификаторы сложности
        self.difficulty_modifiers = {
            "easy": 1.0,
            "medium": 1.2,
            "hard": 1.5
        }

    def get_difficulty_multiplier(self) -> float:
        return self.difficulty_modifiers.get(self.difficulty, 1.0)

    def __str__(self):
        return f"🏁 Трасса: {self.name} | Длина: {self.length}м | Сложность: {self.difficulty}"
