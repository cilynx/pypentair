class Program():

    MODE = [0x03, 0x85]
    RPM = [0x03, 0x8D]
    SCHEDULE_START = [0x03, 0x95]
    SCHEDULE_END = [0x03, 0x9D]
    EGG_TIMER = [0x03, 0xA5]

    MANUAL_MODE = 0
    EGG_TIMER_MODE = 1
    SCHEDULE_MODE = 2
    DISABLED = 3

    def __init__(self, pump, id):
        self.pump = pump
        self.id = id

    def my(self, address):
        return [address[0], address[1] + self.id - 1]

    @property
    def rpm(self):
        return self.pump.get(self.my(Program.RPM))

    @rpm.setter
    def rpm(self, rpm):
        return self.pump.set(self.my(Program.RPM), rpm)

    @property
    def mode(self):
        return self.pump.get(self.my(Program.MODE))

    @mode.setter
    def mode(self, mode):
        self.pump.set(self.my(Program.MODE), mode)

    @property
    def egg_timer(self):
        minutes = self.pump.get(self.my(Program.EGG_TIMER))
        return [int(minutes/60), minutes % 60]

    @egg_timer.setter
    def egg_timer(self, duration):
        minutes = 60 * duration[0] + duration[1]
        self.pump.set(self.my(Program.EGG_TIMER), minutes)

    @property
    def schedule_start(self):
        minutes = self.pump.get(self.my(Program.SCHEDULE_START))
        return [int(minutes/60), minutes % 60]

    @schedule_start.setter
    def schedule_start(self, time):
        minutes = 60 * time[0] + time[1]
        self.pump.set(self.my(Program.SCHEDULE_START), minutes)

    @property
    def schedule_end(self):
        minutes = self.pump.get(self.my(Program.SCHEDULE_END))
        return [int(minutes/60), minutes % 60]

    @schedule_end.setter
    def schedule_end(self, time):
        minutes = 60 * time[0] + time[1]
        self.pump.set(self.my(Program.SCHEDULE_END), minutes)
