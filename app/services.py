programs = {
    "Fat Loss": {"factor": 22},
    "Muscle Gain": {"factor": 35},
    "Beginner": {"factor": 26}
}


def calculate_calories(weight, program):
    if program not in programs:
        return None
    return int(weight * programs[program]["factor"])


def get_programs():
    return list(programs.keys())