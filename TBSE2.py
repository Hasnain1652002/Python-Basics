class Destination:
    def __init__(self, name, budget, visa_required):
        self.name = name
        self.budget = budget
        self.visa_required = visa_required


class TravelRecommendation:
    def __init__(self):
        self.destinations = [
            Destination(name="Saudi Arabia", budget=500000, visa_required=False),
            Destination(name="Iraq", budget=200000, visa_required=True),
            Destination(name="Egypt", budget=300000, visa_required=False)
        ]

    def get_user_input(self):
        self.knowledge_base = {
            "budget": int(input("Enter your budget: ")),
            "visa_required": input("Do you require a visa to your destination (yes/no): ").lower() == "yes",
            "transportation": input("Do you prefer to travel by plane or train ? "),
            "accommodation": input("Do you prefer to stay in a hotel, hostel, or Airbnb? ")
        }

    def infer_destination(self):
        possible_destinations = [destination for destination in self.destinations
         if destination.budget <= self.knowledge_base["budget"] and
            destination.visa_required == self.knowledge_base["visa_required"]]
        if possible_destinations:
            # Choose the destination with the lowest budget
            self.knowledge_base["destination"] = min(possible_destinations, key=lambda destination: destination.budget).name

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
