class SH_automata:
    '''
    This implementation of an SH-automata follows this internal structure:

    states = {"s_0", "s_b", "s_c", "s_f"}
    transitions = {  
        "s_0": {"s_b": ["a"]},
        "s_b": {"s_b": ["aaa"], "s_c": ["aa", "aaa"], "s_f": ["a"]},
        "s_c": {"s_b": ["aa", "aaaaa"]},
        "s_f": {}
    }
    initial_state = "s_0"
    final_state = "s_f"

    This is the representation of the example 8 of the paper 
    "Recognition of Simple Splicing Systems using SH-Automaton".
    '''
    def __init__(self, states={"s_0", "s_f"}, transitions=dict(), initial_state="s_0", final_state="s_f"):
        self.states = states
        self.transitions = transitions
        self.initial_state = initial_state
        self.final_state = final_state
