class Destination:
    def __init__(self, name, budget, visa_required):
        self.name = name
        self.budget = budget
        self.visa_required = visa_required

class TravelRecommendation:
    def __init__(self):
        self.knowledge_base = {
            "budget": None,
            "visa_required": None,
            "destination": None
        }
        self.destinations = [
            Destination(name="Thailand", budget=1000, visa_required=False),
            Destination(name="Japan", budget=2000, visa_required=True),
            Destination(name="France", budget=3000, visa_required=False)
        ]

    def get_user_input(self):
        budget = int(input("Enter your budget (in USD): "))
        visa_required = input("Do you require a visa to your destination (yes/no): ")
        self.knowledge_base["budget"] = budget
        self.knowledge_base["visa_required"] = visa_required

    def infer_destination(self):
        for destination in self.destinations:
            if destination.budget <= self.knowledge_base["budget"] and destination.visa_required == (self.knowledge_base["visa_required"].lower() == "yes"):
                self.knowledge_base["destination"] = destination.name
                break

    def display_recommendation(self):
        if self.knowledge_base["destination"]:
            print(f"Based on your budget and visa requirements, we recommend {self.knowledge_base['destination']}.")
        else:
            print("Sorry, we could not find a suitable destination for you based on your input.")

if __name__ == "__main__":
    recommendation = TravelRecommendation()
    recommendation.get_user_input()
    recommendation.infer_destination()
    recommendation.display_recommendation()
