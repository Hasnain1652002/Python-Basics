# Name: YOUR NAME
# Student Number: 23XXXXXX

class Leaderboard:
    """A leaderboard of speedrunning record times."""

    def __init__(self, runs=[]):
        """Initialize the leaderboard and manually insert runs in  order."""
        self.runs = []
        
        for run in runs:
            time = run[0]
            name = run[1]
            self.insert_correct_order(time, name)

    def get_runs(self):
        """Returns the current leaderboard."""
        result = []
        
        for run in self.runs:
            result.append(run)

        return result

    def submit_run(self, time, name):
        """Adds a new run to the leaderboard while maintainingY order."""
        self.insert_correct_order(time, name)

    def get_rank_time(self, rank):
        """Get the time required to achieve at least a given rank."""
        if rank < 1 or rank > len(self.runs):
            return None
        
        return self.runs[rank - 1][0]

    def get_possible_rank(self, time):
        """Determine what rank the run would be if submitted."""
        rank = 1
        index = 0
        
        while index < len(self.runs):
            if self.runs[index][0] < time:
                rank += 1
            index += 1

        return rank

    def count_time(self, time):
        """Count the number of runs with the given time."""
        count = 0
        index = 0

        while index < len(self.runs):
            if self.runs[index][0] == time:
                count += 1
            index += 1

        return count

    def insert_correct_order(self, time, name):
        """Manually insert (time, name) into the leaderboard while maintaining order."""
        if len(self.runs) == 0:
            self.runs.append((time, name))
            return

        index = len(self.runs) - 1
        
        while index >= 0:
            t, n = self.runs[index]

            if time > t:
                break

            if time == t and name > n:
                break

            index -= 1

        self.runs.insert(index + 1, (time, name))
