from utils import bcolors, pass_test

print(f"{bcolors.HEADER}\n#############\n# EXAMPLE 6 #\n#############\n{bcolors.ENDC}")
I = ["aabaaaaabaaabaa"]
R = ["b"]
pass_test(I, R, "aabaaabaaaaabaaaaabaaabaa", expected_result=True)
pass_test(I, R, "aabaa", expected_result=True, verbose=0)
pass_test(I, R, "abaa", expected_result=False, verbose=0)
pass_test(I, R, "", expected_result=False, verbose=0)

print(f"{bcolors.HEADER}\n#############\n# EXAMPLE 7 #\n#############\n{bcolors.ENDC}")
I = ["abaaabaaabaa", "aabaaaaabaaaaabaaaaa"]
R = ["b"]
pass_test(I, R, "aabaaabaaabaaaaabaaaaa", expected_result=True)
pass_test(I, R, "abaaaaabaa", expected_result=True, verbose=0)
pass_test(I, R, "abaaabaaaabaa", expected_result=False, verbose=0)
pass_test(I, R, "abaaaaabaab", expected_result=False, verbose=0)

print(f"{bcolors.HEADER}\n#############\n# EXAMPLE 8 #\n#############\n{bcolors.ENDC}")
I = ["abaacaaaaaba", "abaaabaaacaaba"]
R = ["b", "c"]
pass_test(I, R, "abaaabaacaabaaacaaaaaba", expected_result=True)
pass_test(I, R, "abaacaabaaabaaaba", expected_result=True, verbose=0)
pass_test(I, R, "abaacaaa", expected_result=False, verbose=0)
pass_test(I, R, "babaaabaacaaba", expected_result=False, verbose=0)

print(f"{bcolors.HEADER}\n#############\n# EXAMPLE 9 #\n#############\n{bcolors.ENDC}")
I = ["abaaabbaabbba"]
R = ["b"]
pass_test(I, R, "abaaabbbbbbaabaaabbba", expected_result=True)
pass_test(I, R, "abbbbba", expected_result=True, verbose=0)
pass_test(I, R, "abbbabba", expected_result=False, verbose=0)
pass_test(I, R, "abaabaaaaabba", expected_result=False, verbose=0)
