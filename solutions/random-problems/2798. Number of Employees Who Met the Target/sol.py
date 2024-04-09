def numberOfEmployeesWhoMetTarget(self, hours: list[int], target: int) -> int:
    number_of_employees_met_target = 0
    for hour in hours:
        if hour >= target:
            number_of_employees_met_target += 1
    
    return number_of_employees_met_target