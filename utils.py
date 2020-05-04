def get_max_firm_subwords(I, R):
    '''Returns a list of strings
    
    Given a list of words and a list of splicing rules finds the
    maximal firm subwords and returns them in a list.
    Params:
        I -> List with the words to extract the maximal firm subwords
        R -> list of rules with the symbols where we make the splicing
    '''
    max_firms = set()
    for word in I:
        firm = ""
        for symbol in word:
            if symbol not in R:
                firm += symbol
            else:
                max_firms.add(firm)
                firm = ""

        if firm != "":
            max_firms.add(firm)
            firm = ""

    return list(max_firms)


if __name__ == "__main__":
    print("FUNCTIONS TESTS:")

    print("\nget_max_firm_subwords():")
    I = ["abaacaaaaaba", "abaaabaaacaaba"]
    R = ["b", "c"]
    print(f"\tinputs: I={I}, R={R}")
    print(f"\toutput: {get_max_firm_subwords(I, R)}")
