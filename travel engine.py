
# Define the knowledge base and rules
knowledge_base = {
    "budget": None,
    "travel_dates": None,
    "visa_required": None,
    "destination": None
}

rules = {
    "destination": {
        "Thailand": {
            "budget": lambda budget: budget >= 1000,
            "travel_dates": lambda travel_dates: "January" in travel_dates or "February" in travel_dates,
            "visa_required": lambda visa_required: not visa_required
        },
        "Japan": {
            "budget": lambda budget: budget >= 2000,
            "travel_dates": lambda travel_dates: "April" in travel_dates or "November" in travel_dates,
            "visa_required": lambda visa_required: visa_required == "yes"
        },
        "France": {
            "budget": lambda budget: budget >= 3000,
            "travel_dates": lambda travel_dates: "June" in travel_dates or "September" in travel_dates,
            "visa_required": lambda visa_required: visa_required == "no"
        }
    }
}

# Get user input
budget = int(input("Enter your budget (in USD): "))
travel_dates = input("Enter your preferred travel dates (comma-separated): ").split(",")
visa_required = input("Do you require a visa to your destination (yes/no): ")

# Update the knowledge base with user input
knowledge_base["budget"] = budget
knowledge_base["travel_dates"] = travel_dates
knowledge_base["visa_required"] = visa_required

# Apply rules to the knowledge base to infer the recommended destination
for destination, criteria in rules["destination"].items():
    if criteria["budget"](budget) and criteria["travel_dates"](travel_dates) and criteria["visa_required"](visa_required):
        knowledge_base["destination"] = destination
        break

# Display the recommended destination
if knowledge_base["destination"]:
    print(f"Based on your budget, travel dates, and visa requirements, we recommend {knowledge_base['destination']}.")
else:
    print("Sorry, we could not find a suitable destination for you based on your input.")


