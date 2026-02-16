from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul


def spell_reducer(spells: list[int], operation: str) -> int:
    operations = {
        'add': add,
        'multiply': mul,
        'max': max,
        'min': min
    }
    return reduce(operations[operation], spells)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    return {
        'fire_enchant': partial(base_enchantment, power=50, element='fire'),
        'ice_enchant': partial(base_enchantment, power=50, element='ice'),
        'lightning_enchant': partial(base_enchantment, power=50, element='lightning')
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> callable:
    @singledispatch
    def cast_spell(spell):
        return f"Unknown spell type: {type(spell).__name__}"

    @cast_spell.register(int)
    def _(spell):
        return f"Damage spell: {spell} damage"

    @cast_spell.register(str)
    def _(spell):
        return f"Enchantment: {spell}"

    @cast_spell.register(list)
    def _(spell):
        return f"Multi-cast: {len(spell)} spells"

    return cast_spell


def main() -> None:
    print("Testing spell reducer...")
    spells = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer([10, 20, 30, 40], 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")

    print("\nTesting memoized fibonacci...")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")


if __name__ == "__main__":
    main()