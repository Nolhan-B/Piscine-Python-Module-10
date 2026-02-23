def mage_counter() -> callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> callable:
    power = initial_power

    def accumulate(moreover_power: int) -> int:
        nonlocal power
        power += moreover_power
        return power
    return accumulate


def enchantment_factory(enchantment_type: str) -> callable:
    return lambda item: f"{enchantment_type} {item}"


def memory_vault() -> dict[str, callable]:
    vault = {}

    def store(key, value) -> None:
        vault[key] = value

    def recall(key) -> str:
        if vault[key]:
            return vault[key]
        return "Memory not found"
    return {
        'store': store,
        'recall': recall
    }


def main() -> None:
    print("\nTesting mage counter...")
    call = mage_counter()
    print(f" Call 1: {call()}")
    print(f" Call 2: {call()}")
    print(f" Call 3: {call()}")

    print("\nTesting enchantment factory...")
    ench_flame = enchantment_factory("Flaming")
    ench_frozen = enchantment_factory("Frozen")

    print(ench_flame("sword"))
    print(ench_frozen("Shield"))

    # print("\nTesting spell accumulator...")
    # power = 10
    # print(f"Initial power : {power}")
    # acc = spell_accumulator(power)
    # print(f"Power is now : {acc(15)}")
    # print(f"Power is now : {acc(3)}")

    # print("Testing memory vault...")
    # mem = memory_vault()
    # mem["store"]("bagpack", "sword")
    # print(mem["recall"]("bagpack"))


if __name__ == "__main__":
    main()
