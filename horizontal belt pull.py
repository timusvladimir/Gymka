import matplotlib.pyplot as plt

class WorkoutPlan:
    def __init__(self):
        self.schedule = [
            {"week": 1, "day": "Пн", "exercise": "Горизонтальная тяга к поясу", "weight": 5, "reps": 10, "sets": 6},
            {"week": 1, "day": "Чт", "exercise": "Горизонтальная тяга к поясу", "weight": 5, "reps": 10, "sets": 6},
            {"week": 2, "day": "Пн", "exercise": "Горизонтальная тяга к поясу", "weight": 10, "reps": 10, "sets": 6},
            {"week": 2, "day": "Чт", "exercise": "Горизонтальная тяга к поясу", "weight": 10, "reps": 10, "sets": 6},
            {"week": 3, "day": "Пн", "exercise": "Горизонтальная тяга к поясу", "weight": 15, "reps": 8, "sets": 6},
            {"week": 3, "day": "Чт", "exercise": "Горизонтальная тяга к поясу", "weight": 15, "reps": 8, "sets": 6},
            {"week": 4, "day": "Пн", "exercise": "Горизонтальная тяга к поясу", "weight": 20, "reps": 6, "sets": 6},
            {"week": 4, "day": "Чт", "exercise": "Горизонтальная тяга к поясу", "weight": 20, "reps": 6, "sets": 6},
        ]

    def display_plan(self):
        print("План реабилитации спины на месяц:")
        for entry in self.schedule:
            print(f"Неделя {entry['week']}, День {entry['day']}: {entry['exercise']} - "
                  f"Вес: {entry['weight']} кг, Повторения: {entry['reps']}, Подходы: {entry['sets']}")

    def plot_progress(self):
        weeks = [entry['week'] for entry in self.schedule]
        weights = [entry['weight'] for entry in self.schedule]

        plt.figure(figsize=(10,5))
        plt.plot(weeks, weights, marker='o')
        plt.title('Прогресс в весе для горизонтальной тяги к поясу')
        plt.xlabel('Неделя')
        plt.ylabel('Вес (кг)')
        plt.xticks(weeks)
        plt.grid(True)
        plt.show()

if __name__ == "__main__":
    workout_plan = WorkoutPlan()
    workout_plan.display_plan()
    workout_plan.plot_progress()
