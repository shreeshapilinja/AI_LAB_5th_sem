# Define the initial state
initial_state = ["fresh"]

# Define the rules
rules = [
    {"if": ["clean", "smelly"], "then": ["fresh"]},
    {"if": ["dirty"], "then": ["clean"]},
]

# Define the goal
goal = ["dirty", "smelly"]

# Initialize the current state
current_state = initial_state

# Apply the rules until the goal is reached
while not all(x in current_state for x in goal):
    # Check if the goal is already present in the current state
    if all(x in current_state for x in goal):
        break
    # Otherwise, apply the rules in reverse order
    for rule in reversed(rules):
        if all(x in current_state for x in rule["then"]):
            current_state += rule["if"]

# Print the final state
print("The final state is:", current_state)

"""
In this example, the initial state is defined as ["fresh"], the goal is defined as ["dirty", "smelly"], 
and the rules are defined as a list of if-then statements. The code initializes the current state as the 
initial state and enters a loop that applies the rules in reverse order until the goal is reached or it becomes 
clear that the goal cannot be reached. In each iteration of the loop, the code checks each rule in reverse order
 to see if the actions specified in the "then" clause are present in the current state. If they are, the code 
 updates the current state by adding the conditions specified in the "if" clause to the current state. This process 
 of applying the rules in reverse order to deduce new facts is called backward chaining because it involves moving 
 backward through the rules, starting with the desired conclusion and working towards the known facts.
"""