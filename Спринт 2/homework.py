from dataclasses import dataclass
from typing import List, Dict, Type


@dataclass
class InfoMessage:
    """Информационное сообщение о тренировке."""
    training_type: int
    duration: float
    distance: float
    speed: float
    calories: float

    def get_message(self) -> str:
        return (
            f'Тип тренировки: {self.training_type}; '
            f'Длительность: {self.duration:3.3f} ч.; '
            f'Дистанция: {self.distance:3.3f} км; '
            f'Ср. скорость: {self.speed:3.3f} км/ч; '
            f'Потрачено ккал: {self.calories:3.3f}.'
        )


class Training:
    """Базовый класс тренировки."""

    LEN_STEP: float = 0.65
    M_IN_KM: float = 1000
    MIN: float = 60

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action: int = action
        self.duration_km: float = duration
        self.weight_kg: float = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        # action * LEN_STEP / M_IN_KM
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        # преодоленная_дистанция_за_тренировку / время_тренировки
        return self.get_distance() / self.duration_km

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        raise NotImplementedError

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке"""
        return InfoMessage(type(self).__name__,
                           self.duration_km,
                           self.get_distance(),
                           self.get_mean_speed(),
                           self.get_spent_calories()
                           )


class Running(Training):
    """Тренировка: бег."""

    CALORIES_RUN_1: int = 18
    CALORIES_RUN_2: int = 20

    def get_spent_calories(self) -> float:
        # (18 * средняя_скорость - 20) * вес_спортсмена
        # / M_IN_KM * время_тренировки_в_минутах
        return ((self.CALORIES_RUN_1 * self.get_mean_speed()
                - self.CALORIES_RUN_2)
                * self.weight_kg / self.M_IN_KM * self.duration_km * self.MIN)


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""

    CALORIES_WALK_1: float = 0.035
    CALORIES_WALK_2: float = 0.029

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float
                 ) -> None:
        super().__init__(action, duration, weight)
        self.height_m: float = height

    def get_spent_calories(self) -> float:
        # (0.035 * вес + (средняя_скорость**2 // рост) * 0.029 * вес)
        # * время_тренировки_в_минутах
        return ((self.CALORIES_WALK_1 * self.weight_kg
                + (self.get_mean_speed() ** 2 // self.height_m)
                * self.CALORIES_WALK_2 * self.weight_kg)
                * (self.duration_km * self.MIN))


class Swimming(Training):
    """Тренировка: плавание."""

    LEN_STEP: float = 1.38
    CALORIES_SWIM_1: float = 1.1
    CALORIES_SWIM_2: int = 2

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: float,
                 count_pool: float
                 ) -> None:
        super().__init__(action, duration, weight)
        self.length_pool: float = length_pool
        self.count_pool: float = count_pool

    def get_mean_speed(self) -> float:
        # длина_бассейна * count_pool / M_IN_KM / время_тренировки
        return (self.length_pool * self.count_pool
                / self.M_IN_KM / self.duration_km)

    def get_spent_calories(self) -> float:
        # (средняя_скорость + 1.1) * 2 * вес
        return ((self.get_mean_speed() + self.CALORIES_SWIM_1)
                * self.CALORIES_SWIM_2 * self.weight_kg)


def read_package(workout_type: str, data: List[int]) -> Training:
    """Прочитать данные полученные от датчиков."""
    training_type: Dict[str, Type[Training]] = {
        'SWM': Swimming,
        'RUN': Running,
        'WLK': SportsWalking
    }
    if workout_type not in training_type:
        raise ValueError(
                        f'Нет такой тренировки {workout_type}.'
                        f'Ожидалось {data.keys()}'
        )
    return training_type[workout_type](*data)


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    print(info.get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
