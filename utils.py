from sh_automata import SH_automata

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


def pass_test(I, R, word, expected_result, verbose=0):
    '''Returns a boolean with the result of the test
    Given an splicing system (I, R) and a word. It checks if the
    word belongs to the language of the splicing systems and checks
    if it gets the 'expected_result'.
    Params:
        I -> list with the initial words of the splicing system
        R -> list with the rules of the system
        word -> string to check with the splicing system
        expected_result -> boolean, if the word really belongs or not the
                           language of the splicing system
        verbose -> to set verbosity for the automata check process
    '''
    automata = SH_automata(I, R)
    check_res = automata.check_word(word, verbose=verbose)
    print(f"{bcolors.BOLD}Splicing system:{bcolors.ENDC} I = {I}, R = {R}\n")
    print(f"{bcolors.BOLD}Automata:{bcolors.ENDC}\n{automata}")
    print(f"\"{word}\" check: {bcolors.OKGREEN + 'OK' if check_res == expected_result else bcolors.FAIL + 'FAIL'}{bcolors.ENDC}")
