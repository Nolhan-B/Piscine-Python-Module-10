def spell_combiner(spell1: callable, spell2: callable) -> callable:
    return lambda t: (spell1(t), spell2(t))


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    return lambda power: base_spell(power) * multiplier


def conditional_caster(condition: callable, spell: callable) -> callable:
    return lambda t: spell(t) if condition(t) else "Spell fizzled"


def spell_sequence(spells: list[callable]) -> callable:
    return lambda t: [spell(t) for spell in spells]


if __name__ == "__main__":
    def fireball(target):
        return f"Fireball hits {target}"

    def heals(target):
        return f"Heals {target}"

    def damage_spell(power):
        return power

    print("\nTesting spell combiner...")
    combined = spell_combiner(fireball, heals)
    result = combined("Dragon")
    print(f"Combined spell result: {result[0]}, {result[1]}")

    print("\nTesting power amplifier...")
    mega_spell = power_amplifier(damage_spell, 3)
    original = damage_spell(10)
    amplified = mega_spell(10)
    print(f"Original: {original}, Amplified: {amplified}")
    # print("\nTesting conditional caster...")
    # def has_mana(target):
    #     return len(target) > 3

    # conditional_fire = conditional_caster(has_mana, fireball)
    # print(conditional_fire("Dragon"))
    # print(conditional_fire("Bat"))

    # print("\nTesting spell sequence...")
    # def lightning(target):
    #     return f"Lightning strikes {target}"

    # combo = spell_sequence([fireball, heal, lightning])
    # results = combo("Boss")
    # for result in results:
    #     print(result)
