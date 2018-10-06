from rdoclient_py3 import RandomOrgClient


class Workout:
    name_pad = 0
    link_pad = 0

    def __init__(self, name: str, link: str, hardness: int):
        self.name = name
        self.link = link
        self.hardness = hardness
        if Workout.name_pad < len(name) + 1:
            Workout.name_pad = len(name) + 1
        if Workout.link_pad < len(link) + 1:
            Workout.link_pad = len(link) + 1

    def __str__(self):
        return self.name.ljust(Workout.name_pad) + ' ' + self.link.ljust(Workout.link_pad) + ' ' + str(self.hardness)


def generate_set_of_workouts(sets: int, rand: RandomOrgClient):
    workouts = [
        Workout('3-Minute Intensive Workout', 'https://www.youtube.com/watch?v=3GZ7n0Kr9uo', 0),
        Workout('3-Minute No Gym Fat Burning', 'https://www.youtube.com/watch?v=XZQy3kqlbnM', 0),
        Workout('3-Minute Fat Burning Progression', 'https://www.youtube.com/watch?v=lyxCEbNAVpQ', 0),
        Workout('2018 Fat Burning Full Body Workout', 'https://www.youtube.com/watch?v=0Rv_blEHkBc', 0),
        Workout('No Gym Intensive Fat Burning Workout', 'https://www.youtube.com/watch?v=OihBUKIFrss', 0),
        Workout('Basic High Intensity Home Workout', 'https://www.youtube.com/watch?v=34Sw3ktC7mo', 0),
        Workout('Full Body Workout', 'https://www.youtube.com/watch?v=j57HMjVM7Is', 0),
        Workout('6 Extreme Exercises', 'https://www.youtube.com/watch?v=-FPAXEOxqVo', 0),
        Workout('9 Minutes Fat Burning: Round 1/3', 'https://www.youtube.com/watch?v=YUEs8yQ-MBs', 0),
        Workout('9 Minutes Fat Burning: Round 2/3', 'https://www.youtube.com/watch?v=YUEs8yQ-MBs&t=191', 0),
        Workout('9 Minutes Fat Burning: Round 3/3', 'https://www.youtube.com/watch?v=YUEs8yQ-MBs&t=375', 0),
        Workout('10 Minute Intensive Fat Burning: Round 1/3', 'https://www.youtube.com/watch?v=GDe_MwdCTI0', 0),
        Workout('10 Minute Intensive Fat Burning: Round 2/3', 'https://www.youtube.com/watch?v=GDe_MwdCTI0&t=160', 0),
        Workout('10 Minute Intensive Fat Burning: Round 3/3', 'https://www.youtube.com/watch?v=GDe_MwdCTI0&t=362', 0),
    ]

    no_of_workouts = len(workouts) - 1
    workout_ids = rand.generate_integers(n=sets, min=0, max=no_of_workouts, replacement=False)
    chosen_workouts = [workouts[x] for x in workout_ids]

    return chosen_workouts


def main():
    rand = RandomOrgClient(open('api.key').readline())
    print(str(rand.get_requests_left()) + ' requests from random.org are left available today.')

    sets = int(input('How many sets? '))
    workouts = generate_set_of_workouts(sets, rand)

    for workout in workouts:
        print(workout)


if __name__ == "__main__":
    main()
