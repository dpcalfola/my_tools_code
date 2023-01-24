"""
This program is to calculate total power consumption
of my family's hobby devices
which are doubtfully high power consumption.

Because I don't understand why my electricity bill is so high.
"""

"""----- class part -----"""


class Device:

    def __init__(self, name, power, cnt, use_time_a_day):
        """
        :param name: 기기 이름
        :param power: 전력량(w)
        :param cnt: 갯수(개)
        :param use_time_a_day: 하루 사용 시간(h)
        """

        self.name: str = name
        self.power: float = power
        self.cnt: int = cnt
        self.use_time_a_day: int = use_time_a_day


class Electrics(Device):

    def __init__(self, name, power, cnt, use_time_a_day):
        super().__init__(name, power, cnt, use_time_a_day)

    # calculate daily power (unit: kWh)
    @property
    def daily_power(self) -> float:
        return self.power * self.cnt * self.use_time_a_day / 1000

    # Calculate total power (unit: KWh)
    def total_power(self, time_case: str) -> float:
        if time_case == 'a_day':
            return self.daily_power
        elif time_case == 'a_month':
            return self.daily_power * 30
        elif time_case == 'a_year':
            return self.daily_power * 365
        else:
            raise ValueError('time_case should be a_day, a_month, a_year')


"""----- data part -----"""
# data: list = [name, power, cnt, use_time_a_day]
data_lamp_1 = ['PLED', 20, 4, 12]
data_lamp_2 = ['Philips', 16, 4, 12]
data_lamp_3 = ['FarmTec', 12, 1, 12]
data_lamp_4 = ['LED_BAR', 7.2, 10, 12]
data_nas = ['Synology', 25, 1, 24]

# data_list
data_list: list = [data_lamp_1, data_lamp_2, data_lamp_3, data_lamp_4, data_nas]

"""----- main part -----"""
if __name__ == '__main__':
    # Make a list of devices objects from data_list
    devices: list[Electrics] = [Electrics(*data) for data in data_list]

    # Calculate total power (unit: kWh)
    total_power_a_day: float = 0
    total_power_a_month: float = 0
    total_power_a_year: float = 0

    for device in devices:
        total_power_a_day += device.total_power('a_day')
        total_power_a_month += device.total_power('a_month')
        total_power_a_year += device.total_power('a_year')

    print(f'Total power a day: {total_power_a_day:.3f} kWh')
    print(f'Total power a month: {total_power_a_month:.3f} kWh')
    print(f'Total power a year: {total_power_a_year:.3f} kWh')
