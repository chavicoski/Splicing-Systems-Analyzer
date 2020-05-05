from utils import bcolors, pass_test

print(f"{bcolors.HEADER}\n#############\n# EXAMPLE 6 #\n#############\n{bcolors.ENDC}")
I = ["aabaaaaabaaabaa"]
R = ["b"]
word = "aabaaabaaaaabaaaaabaaabaa"
pass_test(I, R, word, expected_result=True, verbose=0)

print(f"{bcolors.HEADER}\n#############\n# EXAMPLE 7 #\n#############\n{bcolors.ENDC}")
I = ["abaaabaaabaa", "aabaaaaabaaaaabaaaaa"]
R = ["b"]
word = "aabaaabaaabaaaaabaaaaa"
pass_test(I, R, word, expected_result=True, verbose=0)

print(f"{bcolors.HEADER}\n#############\n# EXAMPLE 8 #\n#############\n{bcolors.ENDC}")
I = ["abaacaaaaaba", "abaaabaaacaaba"]
R = ["b", "c"]
word = "abaaabaacaabaaacaaaaaba"
pass_test(I, R, word, expected_result=True, verbose=0)

print(f"{bcolors.HEADER}\n#############\n# EXAMPLE 9 #\n#############\n{bcolors.ENDC}")
I = ["abaaabbaabbba"]
R = ["b"]
word = "abaaabbbbbbaabaaabbba"
pass_test(I, R, word, expected_result=True, verbose=0)
