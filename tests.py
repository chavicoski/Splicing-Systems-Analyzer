from utils import bcolors, pass_test

print(f"{bcolors.WARNING}################################\n# sh_automata (with max firms) #\n################################{bcolors.ENDC}")

print(f"{bcolors.HEADER}\n#############\n# EXAMPLE 6 #\n#############\n{bcolors.ENDC}")
I = ["aabaaaaabaaabaa"]
R = ["b"]
pass_test(1, I, R, "aabaaabaaaaabaaaaabaaabaa", expected_result=True)
pass_test(1, I, R, "aabaa", expected_result=True, verbose=0)
pass_test(1, I, R, "abaa", expected_result=False, verbose=0)
pass_test(1, I, R, "", expected_result=False, verbose=0)

print(f"{bcolors.HEADER}\n#############\n# EXAMPLE 7 #\n#############\n{bcolors.ENDC}")
I = ["abaaabaaabaa", "aabaaaaabaaaaabaaaaa"]
R = ["b"]
pass_test(1, I, R, "aabaaabaaabaaaaabaaaaa", expected_result=True)
pass_test(1, I, R, "abaaaaabaa", expected_result=True, verbose=0)
pass_test(1, I, R, "abaaabaaaabaa", expected_result=False, verbose=0)
pass_test(1, I, R, "abaaaaabaab", expected_result=False, verbose=0)

print(f"{bcolors.HEADER}\n#############\n# EXAMPLE 8 #\n#############\n{bcolors.ENDC}")
I = ["abaacaaaaaba", "abaaabaaacaaba"]
R = ["b", "c"]
pass_test(1, I, R, "abaaabaacaabaaacaaaaaba", expected_result=True)
pass_test(1, I, R, "abaacaabaaabaaaba", expected_result=True, verbose=0)
pass_test(1, I, R, "abaacaaa", expected_result=False, verbose=0)
pass_test(1, I, R, "babaaabaacaaba", expected_result=False, verbose=0)

print(f"{bcolors.HEADER}\n#############\n# EXAMPLE 9 #\n#############\n{bcolors.ENDC}")
I = ["abaaabbaabbba"]
R = ["b"]
pass_test(1, I, R, "abaaabbbbbbaabaaabbba", expected_result=True)
pass_test(1, I, R, "abbbbba", expected_result=True, verbose=0)
pass_test(1, I, R, "abbbabba", expected_result=False, verbose=0)
pass_test(1, I, R, "abaabaaaaabba", expected_result=False, verbose=0)


print(f"\n{bcolors.WARNING}###############################\n# sh_automata2 (with symbols) #\n###############################{bcolors.ENDC}")

print(f"{bcolors.HEADER}\n#############\n# EXAMPLE 6 #\n#############\n{bcolors.ENDC}")
I = ["aabaaaaabaaabaa"]
R = ["b"]
pass_test(2, I, R, "aabaaabaaaaabaaaaabaaabaa", expected_result=True)
pass_test(2, I, R, "aabaa", expected_result=True, verbose=0)
pass_test(2, I, R, "abaa", expected_result=False, verbose=0)
pass_test(2, I, R, "", expected_result=False, verbose=0)

print(f"{bcolors.HEADER}\n#############\n# EXAMPLE 7 #\n#############\n{bcolors.ENDC}")
I = ["abaaabaaabaa", "aabaaaaabaaaaabaaaaa"]
R = ["b"]
pass_test(2, I, R, "aabaaabaaabaaaaabaaaaa", expected_result=True)
pass_test(2, I, R, "abaaaaabaa", expected_result=True, verbose=0)
pass_test(2, I, R, "abaaabaaaabaa", expected_result=False, verbose=0)
pass_test(2, I, R, "abaaaaabaab", expected_result=False, verbose=0)

print(f"{bcolors.HEADER}\n#############\n# EXAMPLE 8 #\n#############\n{bcolors.ENDC}")
I = ["abaacaaaaaba", "abaaabaaacaaba"]
R = ["b", "c"]
pass_test(2, I, R, "abaaabaacaabaaacaaaaaba", expected_result=True)
pass_test(2, I, R, "abaacaabaaabaaaba", expected_result=True, verbose=0)
pass_test(2, I, R, "abaacaaa", expected_result=False, verbose=0)
pass_test(2, I, R, "babaaabaacaaba", expected_result=False, verbose=0)

print(f"{bcolors.HEADER}\n#############\n# EXAMPLE 9 #\n#############\n{bcolors.ENDC}")
I = ["abaaabbaabbba"]
R = ["b"]
pass_test(2, I, R, "abaaabbbbbbaabaaabbba", expected_result=True)
pass_test(2, I, R, "abbbbba", expected_result=True, verbose=0)
pass_test(2, I, R, "abbbabba", expected_result=False, verbose=0)
pass_test(2, I, R, "abaabaaaaabba", expected_result=False, verbose=0)
