import json

# Define global dictionaries and lists
all_items = []
all_skills = []
all_spells = []

# Initial Buffs and Debuffs
BUFFS = ["Might", "Agility", "Haste", "Regen", "Brilliance", "Invisibility", "Flying"]
DEBUFFS = ["Slow", "Confusion", "Paralysis", "Poison", "Petrification", "Fear", "Rot", "Drain", "Silence", "Mark"]

# Function to dynamically manage Buffs and Debuffs
def manage_effects(effect_type):
    effects = BUFFS if effect_type == "buff" else DEBUFFS
    while True:
        print(f"\nCurrent {effect_type.title()}s: {', '.join(effects)}")
        print("1. Add new effect")
        print("2. Remove an effect")
        print("3. Back to main menu")
        choice = input("Choose an option: ")
        
        if choice == "1":
            new_effect = input(f"Enter new {effect_type}: ")
            if new_effect not in effects:
                effects.append(new_effect)
                print(f"{effect_type.title()} '{new_effect}' added successfully!")
            else:
                print(f"{effect_type.title()} '{new_effect}' already exists.")
        elif choice == "2":
            effect_to_remove = input(f"Enter {effect_type} to remove: ")
            if effect_to_remove in effects:
                effects.remove(effect_to_remove)
                print(f"{effect_type.title()} '{effect_to_remove}' removed successfully!")
            else:
                print(f"{effect_type.title()} '{effect_to_remove}' not found.")
        elif choice == "3":
            break
        else:
            print("Invalid choice, please try again.")

# Function to create an item
def create_item():
    item = {}
    print("\n=== Create New Item ===")
    item["name"] = input("Enter item name: ")
    item["type"] = input("Enter item type (e.g., Weapon, Armor, Potion): ")
    item["rarity"] = input("Enter item rarity (e.g., Common, Rare, Legend): ")
    item["stats"] = {}

    # Input main stats
    print("Enter main stats and their bonuses (leave blank if none):")
    for stat in ["Strength", "Dexterity", "Intelligence", "Wisdom", "Constitution", "Willpower", "Luck"]:
        value = input(f"  {stat} bonus: ")
        if value:
            item["stats"][stat] = int(value)
    
    # Derived stats
    item["derived_stats"] = {}
    print("Enter derived stats (leave blank if none):")
    for derived_stat in ["HP", "MP", "AC", "EV", "MR", "Speed", "Crit"]:
        value = input(f"  {derived_stat} bonus: ")
        if value:
            item["derived_stats"][derived_stat] = float(value)
    
    # Input buffs
    item["buffs"] = []
    print(f"Available Buffs: {', '.join(BUFFS)}")
    while True:
        buff = input("Add a buff (leave blank to finish): ")
        if buff in BUFFS:
            item["buffs"].append(buff)
        elif buff == "":
            break
        else:
            print("Invalid buff name. You can add it through the manage effects menu.")

    # Input debuffs
    item["debuffs"] = []
    print(f"Available Debuffs: {', '.join(DEBUFFS)}")
    while True:
        debuff = input("Add a debuff (leave blank to finish): ")
        if debuff in DEBUFFS:
            item["debuffs"].append(debuff)
        elif debuff == "":
            break
        else:
            print("Invalid debuff name. You can add it through the manage effects menu.")
    
    # Add to global list
    all_items.append(item)
    print(f"Item '{item['name']}' created successfully!")
    return item

# Main Menu
def main_menu():
    while True:
        print("\n=== Game System Menu ===")
        print("1. Create Item")
        print("2. Manage Buffs")
        print("3. Manage Debuffs")
        print("4. View All Items")
        print("5. Export to JSON")
        print("6. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            create_item()
        elif choice == "2":
            manage_effects("buff")
        elif choice == "3":
            manage_effects("debuff")
        elif choice == "4":
            print("\n=== All Items ===")
            for item in all_items:
                print(json.dumps(item, indent=2))
        elif choice == "5":
            with open("game_data.json", "w") as f:
                json.dump({"items": all_items, "buffs": BUFFS, "debuffs": DEBUFFS}, f, indent=2)
            print("Data exported to game_data.json.")
        elif choice == "6":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

# Run the main menu
if __name__ == "__main__":
    main_menu()
