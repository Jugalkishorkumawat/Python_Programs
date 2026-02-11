def game_over(reason):
    print("\n💀 GAME OVER 💀")
    print(reason)
    print("The shadows close in...")
    exit()


def ending(title, description):
    print(f"\n👑 {title} 👑")
    print(description)
    print("\nThe world will never know the truth.")
    exit()


def choose_companion():
    print("\nShadow Garden stands behind you.")
    print("Choose who leads this operation:\n")
    print("1. Alpha – Grand Strategy")
    print("2. Beta – Knowledge & Records")
    print("3. Gamma – Economy & Influence")
    print("4. Delta – Violence & Fear")
    print("5. Epsilon – Illusion & Deception")
    print("6. Zeta – Assassination & Faith")
    print("7. Eta – Science & Madness")

    return input("\nChoose (1-7): ")


def alpha_story():
    print("\nAlpha lays out a world map filled with red marks.")
    print("Each mark is a cult-controlled noble house.")

    choice = input(
        "\nDo you:\n"
        "1. Collapse the cult slowly through politics\n"
        "2. Or stage a single massive shadow war\n"
        "Choose (1/2): "
    )

    if choice == "1":
        print("\nYears pass. Kingdoms fall without battles.")
        print("No one ever realizes Shadow Garden caused it.")
        ending(
            "Architect of the World",
            "You shaped history silently. Kings unknowingly obeyed your design."
        )
    elif choice == "2":
        print("\nThe night sky burns with magic.")
        print("Legends are born from fear.")
        ending(
            "Shadow Emperor",
            "Your name becomes a forbidden myth whispered in terror."
        )
    else:
        game_over("A wrong command ruins the plan.")


def beta_story():
    print("\nBeta uncovers ancient texts older than kingdoms.")
    print("They speak of repeating cycles and false heroes.")

    choice = input(
        "\nDo you:\n"
        "1. Rewrite history using false records\n"
        "2. Preserve the truth for yourself alone\n"
        "Choose (1/2): "
    )

    if choice == "1":
        print("\nFuture generations learn lies you designed.")
        ending(
            "Author of Reality",
            "History itself becomes your greatest weapon."
        )
    elif choice == "2":
        print("\nYou carry unbearable knowledge alone.")
        ending(
            "Bearer of Truth",
            "Only you understand the world’s true nature."
        )
    else:
        game_over("The records burn accidentally.")


def gamma_story():
    print("\nGamma shows you economic charts.")
    print("Entire wars are funded by the cult.")

    choice = input(
        "\nDo you:\n"
        "1. Replace cult money with Shadow Garden currency\n"
        "2. Crash the global economy to reset power\n"
        "Choose (1/2): "
    )

    if choice == "1":
        print("\nKingdoms unknowingly become dependent on you.")
        ending(
            "Invisible Ruler",
            "Money bends the world more effectively than swords."
        )
    elif choice == "2":
        print("\nChaos erupts. Only Shadow Garden survives.")
        ending(
            "Lord of Ruin",
            "From collapse, you rise uncontested."
        )
    else:
        game_over("Markets spiral out of control.")


def delta_story():
    print("\nDelta grins. She only understands enemies.")
    print("A cult fortress stands before you.")

    choice = input(
        "\nDo you:\n"
        "1. Release Delta completely\n"
        "2. Restrict her and fight tactically\n"
        "Choose (1/2): "
    )

    if choice == "1":
        print("\nThe fortress is erased.")
        ending(
            "Beast of the Night",
            "Fear becomes your signature across the continent."
        )
    elif choice == "2":
        print("\nVictory is clean but unnoticed.")
        ending(
            "Silent Hunter",
            "The cult dies without legends."
        )
    else:
        game_over("Delta loses patience.")


def epsilon_story():
    print("\nEpsilon crafts illusions so real they deceive reality.")

    choice = input(
        "\nDo you:\n"
        "1. Create a false Shadow to mislead enemies\n"
        "2. Let the world imagine your power instead\n"
        "Choose (1/2): "
    )

    if choice == "1":
        print("\nEnemies hunt a shadow that doesn't exist.")
        ending(
            "Master of Deception",
            "Your lies protect the truth."
        )
    elif choice == "2":
        print("\nRumors grow stronger than facts.")
        ending(
            "Myth Made Flesh",
            "You exist only in fear and speculation."
        )
    else:
        game_over("The illusion collapses.")


def zeta_story():
    print("\nZeta kneels.")
    print("She believes Shadow is a god.")

    choice = input(
        "\nDo you:\n"
        "1. Encourage her faith\n"
        "2. Suppress it to keep control\n"
        "Choose (1/2): "
    )

    if choice == "1":
        print("\nA cult devoted to you forms.")
        ending(
            "Shadow Deity",
            "Belief becomes your sharpest blade."
        )
    elif choice == "2":
        print("\nZeta remains loyal but distant.")
        ending(
            "Absolute Controller",
            "Emotion is removed from loyalty."
        )
    else:
        game_over("Zeta acts independently.")


def eta_story():
    print("\nEta presents forbidden technology.")
    print("It can surpass magic itself.")

    choice = input(
        "\nDo you:\n"
        "1. Merge science with magic\n"
        "2. Seal the research forever\n"
        "Choose (1/2): "
    )

    if choice == "1":
        print("\nA new era begins.")
        ending(
            "Transcendent Existence",
            "You step beyond human limitations."
        )
    elif choice == "2":
        print("\nSome power is too dangerous.")
        ending(
            "Guardian of Balance",
            "You protect the world from itself."
        )
    else:
        game_over("The experiment explodes.")


def main():
    name = input("Enter your name: ")
    print(f"\n{name}, you walk the path of shadows.")
    print("You are weak by design. Invisible by choice.")

    observe = input(
        "\nDo you:\n"
        "1. Act as a background character\n"
        "2. Seek power openly\n"
        "Choose (1/2): "
    )

    if observe == "2":
        game_over("The world crushes those who stand in the light.")

    companion = choose_companion()

    if companion == "1":
        alpha_story()
    elif companion == "2":
        beta_story()
    elif companion == "3":
        gamma_story()
    elif companion == "4":
        delta_story()
    elif companion == "5":
        epsilon_story()
    elif companion == "6":
        zeta_story()
    elif companion == "7":
        eta_story()
    else:
        game_over("Indecision leads to death.")


main()
