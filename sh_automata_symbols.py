class SH_automata_symbols:
    '''
    This implementation of this SH-automata follows this internal structure:
    For I=["abaacaaaaaba", "abaaabaaacaaba"] and R=["b", "c"]

    states = {'s_b', 's_caaaaa', 's_0', 's_c', 's_ca', 's_ba', 's_baa', 's_caaaa', 's_caa', 's_baaa', 's_caaa', 's_0a'}
    initial state = s_0
    final state = {'s_ba'}
    transitions = {
	s_0: {'a': ['s_0a']}
	s_0a: {'b': ['s_b']}
	s_b: {'a': ['s_ba']}
	s_ba: {'a': ['s_baa']}
	s_baa: {'c': ['s_c'], 'a': ['s_baaa']}
	s_baaa: {'b': ['s_b'], 'c': ['s_c']}
	s_c: {'a': ['s_ca']}
	s_ca: {'a': ['s_caa']}
	s_caa: {'a': ['s_caaa'], 'b': ['s_b']}
	s_caaa: {'a': ['s_caaaa']}
	s_caaaa: {'a': ['s_caaaaa']}
	s_caaaaa: {'b': ['s_b']}
    }

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
        self.final_states = set()
        self.states = {self.initial_state}

        # Create transitions from the splicing system
        self.build_transitions_and_states()


    def build_transitions_and_states(self):
        '''
        Build the transitions and the states of the automata from the initial words 
        and rules of the splicing system given as reference in the constructor
        '''
        self.transitions = {state: dict() for state in self.states}
        for word in self.I:
            current_state = self.initial_state 
            for symbol in word:
                if symbol not in self.R:
                    next_state = current_state + symbol
                    self.add_state(next_state, verbose=0)
                else:
                    next_state = f"s_{symbol}"
                    self.add_state(next_state, verbose=0)

                self.add_transition(current_state, next_state, symbol)
                current_state = next_state

            # Handle the last symbol of the word
            self.final_states.add(next_state)

    def add_state(self, state_name, verbose=1):
        ''' 
        Adds and empty state to the automata
        Params:
            state_name -> string with the name of the new state
        '''
        if state_name not in self.states:
            self.states.add(state_name)
            self.transitions[state_name] = dict()
        elif verbose:
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
        res += f"final state: {self.final_states}\n"
        res += "transitions: {\n"
        for state, transitions in sorted(self.transitions.items(), key=lambda x: x[0]):
            res += f"\t{state}: {transitions}\n"
        res += "\t}\n"
        return res


    def check_word(self, word, verbose=0):
        '''Return a boolean
        Checks if the given word belongs to the language of the SH-automata
        Params:
            word -> word string to check with the automata
        '''
        # Stack for being able to explore all the possibilities in DFS
        states_stack = [(self.initial_state, 0)]
        while True:
            try:
                if verbose: print(f"states stack: {states_stack}")
                # Get current state of the automata and next symbol 
                current_state, symbol_idx = states_stack.pop()
                # If the current state is the final and we processed all the symbols
                if current_state in self.final_states and symbol_idx == len(word): 
                    return True
                # If the current state is not final and there are no more symbols left
                elif symbol_idx == len(word):
                    continue
                else:
                    # Get list of possible next states
                    next_states = self.transitions[current_state].get(word[symbol_idx], [])
                    if verbose: print(f"From state {current_state} to states {next_states} with \"{word[symbol_idx]}\"")
                    if len(next_states) > 0:
                        # Store in the stack the states to explore with the corresponding symbol index
                        for state in next_states:
                            states_stack.append((state, symbol_idx+1))
            except:
                break  # We have emptied the stack

        return False
