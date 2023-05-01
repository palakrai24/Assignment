class GraduationCeremony:

    def __init__(self,no_of_days):
        self.no_of_days = no_of_days

    def generate_binary_attendance(self):
        for i in range(2 ** self.no_of_days):
            attendance = (bin(i).replace("0b", "")).rjust(self.no_of_days, '0')
            yield attendance

    def probability_of_attendance(self):
        valid_attendance = 0
        last_day_miss = 0
        for attendance in self.generate_binary_attendance():
            # absent for 4 consecutive day
            if '0000' not in attendance:
                valid_attendance += 1
                # last day missed the ceremony
                if attendance[-1] == '0':
                    last_day_miss += 1
        return valid_attendance,last_day_miss

n = 5
obj = GraduationCeremony(n)
total_grad_missed,total_grad_attend = obj.probability_of_attendance()
print(f'for {n} days : {total_grad_missed}/{total_grad_attend}')

n = 10
obj = GraduationCeremony(n)
total_grad_missed,total_grad_attend = obj.probability_of_attendance()
print(f'for {n} days : {total_grad_missed}/{total_grad_attend}')
