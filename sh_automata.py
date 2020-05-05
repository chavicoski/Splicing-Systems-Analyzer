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
    def __init__(self, I, R, initial_state="s_0", final_state="s_f"):
        '''
        Constructor of the automata. It takes an syplicing system as input and
        creates the automata tha accepts the language of the splicing system.
        Params:
            I -> list with the initial words of the system
            R -> list with the words where the splicing is aplied 
            initial_state -> name for the initial state
            final_state -> name for the final state
        '''
        # Store the splicing system definition
        self.I = I
        self.R = R

        # Create the states
        self.initial_state = initial_state
        self.final_state = final_state
        self.states = set()
        for state in [initial_state, final_state] + list(map(lambda x: f"s_{x}", R)):
            self.add_state(state)

        # Create transitions from the splicing system
        self.build_transitions()


    def build_transitions(self):
        '''
        Build the transitions of the automata from the initial words and rules of the
        splicing system given as reference in the constructor
        '''
        self.transitions = {state: dict() for state in self.states}
        for word in self.I:
            current_state = self.initial_state 
            firm = ""
            for symbol in word:
                if symbol not in self.R:
                    firm += symbol
                else:
                    next_state = f"s_{symbol}"
                    self.add_transition(current_state, next_state, firm)
                    current_state = next_state
                    firm = ""

            # Handle the last firm of the word
            if firm != "":
                self.add_transition(current_state, self.final_state, firm)


    def add_state(self, state_name):
        ''' 
        Adds and empty state to the automata
        Params:
            state_name -> string with the name of the new state
        '''
        if state_name not in self.states:
            self.states.add(state_name)
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
                self.transitions[src][word] = list(set(self.transitions[src].get(word, []) + [dst]))
            else:
                print(f"The destination state {dst} of the transition doesn't exist")
        else:
            print(f"The source state {src} of the transition doesn't exist")


    def __repr__(self):
        '''
        Function that returns the string representation of the automata
        '''
        res = ""
        res += f"states: {self.states}\n"
        res += f"initial state: {self.initial_state}\n"
        res += f"final state: {self.final_state}\n"
        res += "transitions: {\n"
        for state, transitions in self.transitions.items():
            res += f"\t{state}: {transitions}\n"
        res += "\t}\n"
        return res


    def get_max_firm_subwords(self, I, R):
        '''Returns a list of strings
        Given a list of words and a list of splicing rules finds the
        maximal firm subwords and returns them in a list.
        Params:
            I -> List with the words to extract the maximal firm subwords
            R -> list of rules with the symbols where we make the splicing
        '''
        max_firms = []
        for word in I:
            firm = ""
            for symbol in word:
                if symbol not in R:
                    firm += symbol
                else:
                    max_firms.append(firm)
                    firm = ""

            max_firms.append(firm)

        return max_firms


    def check_word(self, word, verbose=0):
        '''Return a boolean
        Checks if the given word belongs to the language of the SH-automata
        Params:
            word -> word string to check with the automata
        '''
        max_firms = self.get_max_firm_subwords([word], self.R)
        if verbose: print(f"{word} max firms: {max_firms}")
        states_stack = [(self.initial_state, 0)]
        while True:
            try:
                if verbose: print(f"states stack: {states_stack}")
                current_state, firm_idx = states_stack.pop()
                if current_state == self.final_state and firm_idx == len(max_firms):
                    return True
                elif firm_idx == len(max_firms):
                    continue
                else:
                    next_states = self.transitions[current_state].get(max_firms[firm_idx], [])  # It can have multiple states
                    if verbose: print(f"From state {current_state} to states {next_states} with \"{max_firms[firm_idx]}\"")
                    if len(next_states) > 0 and firm_idx < len(max_firms):
                        for state in next_states:
                            states_stack.append((state, firm_idx+1))
            except Exception as e:
                print(e)
                break  # We have emptied the stack

        return False
