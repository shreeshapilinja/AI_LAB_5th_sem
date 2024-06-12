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
 
 
 Backward chaining is a method of reasoning used in artificial intelligence and logic programming. It is a form of goal-driven reasoning, in which the system starts with a goal and works backward to determine what actions need to be taken to achieve the goal.

In this code example, the system starts with the goal of reaching the state ["dirty", "smelly"], and works backward by applying the rules in reverse order until the goal is reached. The rules specify the conditions that need to be satisfied in order to reach the goal. For example, the first rule specifies that if the current state is "clean" and "smelly", then the state is "fresh". The second rule specifies that if the current state is "dirty", then the state is "clean".

The system initializes the current state to the initial state of "fresh" and then iteratively applies the rules until the goal is reached. It checks if the goal is already present in the current state at each iteration, and if it is, it breaks out of the loop. If the goal is not present in the current state, it applies the rules in reverse order to determine the new current state. Once the goal is reached, the system prints the final state.
"""