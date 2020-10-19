#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_even_len(string: str) -> bool:
    p = 0
    for i in string:
        p = p + 1
    if (p % 2) == 0:
        return True
    else:
        return False

def remove_third_char(string: str) -> str:
    return f"{string[0:2]} {string[3:]}"


def replace_char(string: str, old_char: str, new_char: str) -> str:
    return string.replace(old_char,new_char)


def get_nb_char(string: str, char: str) -> int:
    r = 0
    for i in string:
        if i == char:
            r = r +1
        else:
            continue
    return r


def get_nb_words(sentence: str) -> int:
    r = 1
    for i in sentence:
        if i in " ":
            r = r+1
    return r


def main() -> None:
    string = "Bonjour!"
    parity = 'pair' if is_even_len(string) else 'impair'
    print(f"Le nombre de caractère dans la chaine '{string}' est {parity}")

    string = "Sam est cool!"
    print(f"On supprime le 3e caratère dans la chaine '{string}'. Résultat: {remove_third_char(string)}")

    string = "hello world!"
    print(f"On remplace le caratère w par le caractère z dans la chaine: '{string}'. Résultat: {replace_char(string, 'w', 'z')}")

    print(f"Le nombre d'occurrence de l dans hello est : {get_nb_char(string, 'l')}")
    
    string = "Baby shark doo doo doo doo doo doo"
    print(f"Le nombre de mots dans la chaine {string} est: {get_nb_words(string)}")


if __name__ == '__main__':
    main()
