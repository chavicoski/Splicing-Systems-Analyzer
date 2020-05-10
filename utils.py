from sh_automata_firms import SH_automata_firms
from sh_automata_symbols import SH_automata_symbols

class bcolors:
    '''
    For using colors in terminal output
    '''
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def pass_test(automata, I, R, word, expected_result, verbose=1):
    '''Returns a boolean with the result of the test
    Given an splicing system (I, R) and a word. It checks if the
    word belongs to the language of the splicing systems and checks
    if it gets the 'expected_result'.
    Params:
        automata -> Selects the implementation of the automata. 1:max firms - 2:symbols
        I -> list with the initial words of the splicing system
        R -> list with the rules of the system
        word -> string to check with the splicing system
        expected_result -> boolean, if the word really belongs or not the
                           language of the splicing system
        verbose -> 0: Only shows result
                   1: shows result + splicing + automata
                   2: shows result + splicing + automata + automata trace
    '''
    if automata == 1:
        automata = SH_automata_firms(I, R)
    elif automata == 2:
        automata = SH_automata_symbols(I, R)
    else:
        print(f"The automata {automata} is not valid")
        return 
    if verbose > 0:
        print(f"{bcolors.BOLD}Splicing system:{bcolors.ENDC} I = {I}, R = {R}\n")
        print(f"{bcolors.BOLD}Automata:{bcolors.ENDC}\n{automata}")
    check_res = automata.check_word(word, verbose=max(0, verbose-1))
    if expected_result:
        print(f"\"{word}\" belongs: {bcolors.OKGREEN + 'OK' if check_res == expected_result else bcolors.FAIL + 'FAIL'}{bcolors.ENDC}")
    else:
        print(f"\"{word}\" don't belongs: {bcolors.OKGREEN + 'OK' if check_res == expected_result else bcolors.FAIL + 'FAIL'}{bcolors.ENDC}")
