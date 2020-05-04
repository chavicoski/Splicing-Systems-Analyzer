from sh_automata import SH_automata

print("\n#############\n# EXAMPLE 6 #\n#############\n")
I = ["aabaaaaabaaabaa"]
R = ["b"]
word = "aabaaabaaaaabaaaaabaaabaa"
automata = SH_automata(I, R)
print(f"I = {I}")
print(f"R = {R}")
print("Automata:")
print(automata)
print(f"\"{word}\" check: {automata.check_word(word, verbose=0)}")

print("\n#############\n# EXAMPLE 7 #\n#############\n")
I = ["abaaabaaabaa", "aabaaaaabaaaaabaaaaa"]
R = ["b"]
word = "aabaaabaaabaaaaabaaaaa"
automata = SH_automata(I, R)
print(f"I = {I}")
print(f"R = {R}")
print("Automata:")
print(automata)
print(f"\"{word}\" check: {automata.check_word(word, verbose=0)}")

print("\n#############\n# EXAMPLE 8 #\n#############\n")
I = ["abaacaaaaaba", "abaaabaaacaaba"]
R = ["b", "c"]
word = "abaaabaacaabaaacaaaaaba"
automata = SH_automata(I, R)
print(f"I = {I}")
print(f"R = {R}")
print("Automata:")
print(automata)
print(f"\"{word}\" check: {automata.check_word(word, verbose=0)}")

print("\n#############\n# EXAMPLE 9 #\n#############\n")
I = ["abaaabbaabbba"]
R = ["b"]
word = "abaaabbbbbbaabaaabbba"
automata = SH_automata(I, R)
print(f"I = {I}")
print(f"R = {R}")
print("Automata:")
print(automata)
print(f"\"{word}\" check: {automata.check_word(word, verbose=0)}")
