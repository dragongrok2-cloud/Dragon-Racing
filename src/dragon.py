"""
Класс дракона для гонок
"""

class Dragon:
    def __init__(self, name: str, speed: int, maneuverability: int, stamina: int):
        self.name = name
        self.speed = speed                  # Максимальная скорость
        self.maneuverability = maneuverability  # Манёвренность
        self.stamina = stamina              # Выносливость
        self.current_stamina = stamina
        self.position = 0.0

    def accelerate(self):
        """Ускорение дракона"""
        if self.current_stamina > 0:
            boost = self.speed * 0.1
            self.position += boost
            self.current_stamina -= 5
            return boost
        return 0

    def use_boost(self):
        """Использование ускорения"""
        if self.current_stamina >= 20:
            self.current_stamina -= 20
            return self.speed * 1.5
        return 0

    def rest(self):
        """Восстановление выносливости"""
        self.current_stamina = min(self.stamina, self.current_stamina + 10)

    def __str__(self):
        return f"🐉 {self.name} | Скорость: {self.speed} | Манёвренность: {self.maneuverability} | Выносливость: {self.current_stamina}/{self.stamina}"
