# есть функция-процессор process, которая принимает первым аргументом функцию func
# и вторым аргументом - итерируемую последовательность seq. Затем для каждого элемента
# из последовательности применяет функцию func и возвращает список результатов. Нужно
# сделать аннотацию кода, что бы запуск mypy --strict проходил без ошибок.
from collections.abc import Callable, Sequence


def process(
    func: Callable[[int | str], int | str],
    seq: Sequence[int | str],
) -> Sequence[int | str]:
    return [func(item) for item in seq]


if __name__ == "__main__":
    for indx, (input_items, func, expected_result) in enumerate(
        (
            ((1, 2, 3, 4), lambda x: x**2, [1, 4, 9, 16]),
            (["a", "bb", "ccc"], len, [1, 2, 3]),
            (["a", "bb", "ccc"], str.upper, ["A", "BB", "CCC"]),
        ),
        start=1,
    ):
        received_result = process(func, input_items)
        print(f"кейс {indx} - результат: {received_result}")
        print(f"кейс {indx} - ожидание : {expected_result}")
        assert received_result == expected_result
