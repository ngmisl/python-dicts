user = {
    "name": "dragonslayer69",
    "class": "Mage",
    "strength": "20",
    "magic": "420",
    "health": "69",
}


def main() -> None:
    check_true = user.get("class", "n/A")
    check_false = user.get("level", "n/A")
    print(f"{check_true}, {check_false}")


if __name__ == "__main__":
    main()
