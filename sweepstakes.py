import streamlit as st
import random

# List of Euro 2024 teams
teams = [
    "Germany", "Scotland", "Hungary", "Switzerland", 
    "Spain", "Croatia", "Italy", "Albania", 
    "England", "Slovenia", "Denmark", "Serbia",
    "Netherlands", "France", "Poland", "Austria",
    "Ukraine", "Slovakia",  "Belgium", "Romania",
    "Portugal", "Czech Republic", "Georiga", "Turkiye"
]

def assign_teams(names, seed):
    random.seed(seed)
    random.shuffle(teams)
    
    assignments = {name: [] for name in names}
    
    team_index = 0
    name_index = 0
    while len(teams) - team_index > 3:
        assignments[names[name_index]].append(teams[team_index])
        team_index += 1
        name_index = (name_index + 1) % len(names)
    
    remaining_teams = teams[team_index:]
    return assignments, remaining_teams

# Streamlit UI
st.title("Euro 2024 Team Assignment")

# User input for names
names_input = st.text_area("Enter the names of the people (one per line):")
names = names_input.split("\n")
names = [name.strip() for name in names if name.strip()]

# User input for random seed
seed = st.number_input("Enter a random seed:", value=42)

if st.button("Assign Teams"):
    if names:
        assignments, remaining_teams = assign_teams(names, seed)
        st.write("Team assignments:")
        for name, assigned_teams in assignments.items():
            st.write(f"{name}: {', '.join(assigned_teams)}")
        st.write("Remaining teams:")
        st.write(", ".join(remaining_teams))
    else:
        st.write("Please enter at least one name.")
