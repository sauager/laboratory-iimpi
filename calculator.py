# calculator.py
class Calculator:
    def add(self, a: float, b: float) -> float:
        """Возвращает сумму двух чисел."""
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """Возвращает разность двух чисел (a - b)."""
        # БАГ ДЛЯ СТУДЕНТОВ: Неверный порядок вычитания
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """Возвращает произведение двух чисел."""
        # БАГ ДЛЯ СТУДЕНТОВ: Захардкоженный результат
        return a * b

    def divide(self, a: float, b: float) -> float:
        """Возвращает частное от деления a на b. 
        При делении на ноль должен выбрасывать ValueError.
        """
        # БАГ ДЛЯ СТУДЕНТОВ: Вместо исключения возвращает 0
        if b == 0:
            raise ValueError
        return a / b
