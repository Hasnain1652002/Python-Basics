class Destination:
    def __init__(self, name, budget, visa_required):
        self.name = name
        self.budget = budget
        self.visa_required = visa_required


class TravelRecommendation:
    def __init__(self):
        self.destinations = [
            Destination(name="Saudi Arabia", budget=500000, visa_required=True),
            Destination(name="Iraq", budget=200000, visa_required=True),
            Destination(name="France", budget=100000, visa_required=True),
            Destination(name="Thailand", budget=150000, visa_required=True),
            Destination(name="Japan", budget=100000, visa_required=True),
            Destination(name="Sawat", budget=40000, visa_required=False),
            Destination(name="Quetta", budget=20000, visa_required=False),
            Destination(name="Kashmir", budget=50000, visa_required=False)
        ]

    def get_user_input(self):
        self.knowledge_base = {
            "budget": int(input("Enter your budget (in PKR): ")),
            "visa_required": input("Do you require a visa to your destination (yes/no): ").lower() == "yes",
            "transportation": input("Do you prefer to travel by plane, train, bus, or taxi? "),
            "accommodation": input("Do you prefer to stay in a hotel, hostel, or Airbnb? ")
        }

    def infer_destination(self):
        possible_destinations = [destination for destination in self.destinations
        if destination.budget <= self.knowledge_base["budget"] and
            destination.visa_required == self.knowledge_base["visa_required"]]
        if possible_destinations:
            if len(possible_destinations) == 1:
                self.knowledge_base["destination"] = possible_destinations[0].name
            else:
                print("Multiple destinations are available within your budget:")
                for i, dest in enumerate(possible_destinations):
                    print(f"{i+1}. {dest.name}")
                choice = int(input("Please choose a destination (1, 2, 3, etc.): "))
                self.knowledge_base["destination"] = possible_destinations[choice-1].name

    def display_recommendation(self):
        if self.knowledge_base.get("destination"):
            print(f"Based on your budget and visa requirements, we recommend {self.knowledge_base['destination']}.")
            print(f"For transportation, we recommend using {self.knowledge_base['transportation']} and for accommodation, we recommend staying in a {self.knowledge_base['accommodation']}.")
        else:
            print("Sorry, we could not find a suitable destination for you based on your budget.")

    def run(self):
        self.get_user_input()
        self.infer_destination()
        self.display_recommendation()


if __name__ == "__main__":
    recommendation = TravelRecommendation()
    recommendation.run()
