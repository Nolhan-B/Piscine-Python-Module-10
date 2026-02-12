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


# def enchantment_factory(enchantment_type: str) -> callable:

# def memory_vault() -> dict[str, callable]:

def main() -> None:
	print("\nTesting mage counter...")
	call = mage_counter()
	print(f" Call 1: {call()}")
	print(f" Call 2: {call()}")
	print(f" Call 3: {call()}")

	print("\nTesting enchantment factory...")


	# print("\nTesting spell accumulator...")
	# power = 10
	# print(f"Initial power : {power}")
	# acc = spell_accumulator(power)
	# print(f"Power is now : {acc(15)}")
	# print(f"Power is now : {acc(3)}")


if __name__ == "__main__":
	main()