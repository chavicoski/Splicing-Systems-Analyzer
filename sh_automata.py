from utils import get_max_firm_subwords


class SH_automata:
    '''
    This implementation of this SH-automata follows this internal structure:
    For I=["abaacaaaaaba", "abaaabaaacaaba"] and R=["b", "c"]

    states = {"s_0", "s_b", "s_c", "s_f"}
    transitions = {  
        "s_0": {"a": ["s_b"]},
        "s_b": {"aaa": ["s_b", "s_c"], "aa": ["s_c"], "a": ["s_f"]},
        "s_c": {"aa": ["s_b"], "aaaaa": ["s_b"]},
        "s_f": {}
    }
    initial_state = "s_0"
    final_state = "s_f"

    This is the representation of the example 8 of the paper 
    "Recognition of Simple Splicing Systems using SH-Automaton".
    '''
    def __init__(self, I, R):
        self.I = I
        self.R = R
        self.states = R
        
        # Build the automata from the splicing system
        max_firms = get_max_firm_subwords(I, R)

        #### GET TRANSITIONS

        self.transitions = transitions
        self.initial_state = initial_state
        self.final_state = final_state

    def add_state(self, state_name):
        ''' 
        Adds and empty state to the automata
        Params:
            state_name -> string with the name of the new state
        '''
        if state_name not in self.states:
            self.states.add(state_name)
            self.transitions[state_name] = dict()
        else:
            print(f"The state {state_name} allready exists")

    def add_transition(self, src, dst, word):
        '''
        Adds a new transition to the automata
        Params:
            src -> name string of the source state of the transition
            dst -> name string of the destination state of the transition
            word -> word string that makes the transition from state 'src'
        '''
        if src in self.states:
            if dst in self.states:
                self.transitions[src][word].append(dst)
            else:
                print(f"The destination state {dst} of the transition doesn't exist")
        else:
            print(f"The source state {src} of the transition doesn't exist")

    def check_word(self, word):
        '''Return a boolean
        Checks if the given word belongs to the language of the SH-automata
        Params:
            word -> word string to check with the automata
        '''
        max_firms = get_max_firm_subwords([word], self.R)
        states_stack = [(self.initial_state, 0)]
        while True:
            try:
                current_state, firm_idx = states_stack.pop()
                if current_state == self.final_state:
                    return True
                next_states = self.transitions[current_state].get(max_firms[firm_idx], [])  # It can have multiple states
                if len(next_state) > 0:
                    for state in next_states:
                        states_stack.append((state, firm_idx+1))
            except:
                break  # We have emptied the stack

        return False
