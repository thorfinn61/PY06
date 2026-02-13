from .elements import create_fire, create_water, create_air, create_earth


def healing_potion() -> str:
	return f"Healing potion brewed with {create_fire()} and {create_water()}"


def strength_potion() -> str:
	return f"Strength potion brewed with {create_earth()} and {create_fire()}"


def invisibility_potion() -> str:
	return f"Invisibility potion brewed with {create_air()} and {create_water()}"


def wisdom_potion() -> str:
	fire = create_fire()
	earth = create_earth()
	water = create_water()
	air = create_air()
	return f"Wisdom potion brewed with all elements: {fire + earth + water + air}"