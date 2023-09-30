class MadCalculator:
    """Производит арифметические действия разной степени безумности."""

    def sum_string(self, first_num, second_num):
        """Складывает аргументы, как строки и возвращает число,
        сформрованное из них. Если один из аргументов меньше нуля,
        эмоционально отказывается работать.
        """
        if first_num < 0 or second_num < 0:
            raise ValueError('Я отказываюсь работать!')
        return int(str(first_num) + (str(second_num)))

    def sum_args(self, *args):
        """Возвращает сумму принятых аргументов."""
        return sum(i for i in args)
