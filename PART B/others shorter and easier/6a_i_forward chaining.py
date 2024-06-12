# define the set of known facts
facts = {
    "John is a student": True,
    "Mary is a student": True,
    "Students go to school": False
}

# define the set of rules
rules = [
    {
        "premises": ["John is a student", "Mary is a student"],
        "conclusion": "Students go to school"
    }
]

# function to apply the rules and update the set of known facts
def apply_rules(facts, rules):
    for rule in rules:
        all_premises_true = True
        for premise in rule["premises"]:
            if not facts[premise]:
                all_premises_true = False
                break
        if all_premises_true:
            facts[rule["conclusion"]] = True

# apply the rules until no more conclusions can be derived
while True:
    num_conclusions_before = sum(facts.values())
    apply_rules(facts, rules)
    num_conclusions_after = sum(facts.values())
    if num_conclusions_before == num_conclusions_after:
        break

# print the final set of known facts
print(facts)
