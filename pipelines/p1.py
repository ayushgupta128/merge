Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Schedule = Schedule, SensorSchedule = SensorSchedule):
    p1__FindDuplicates_1 = Task(
        task_id = "p1__FindDuplicates_1", 
        component = "Model", 
        modelName = "p1__FindDuplicates_1"
    )
    p1__FuzzyMatch_0 = Task(task_id = "p1__FuzzyMatch_0", component = "Model", modelName = "p1__FuzzyMatch_0")
