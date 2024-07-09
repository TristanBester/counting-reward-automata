from cra.agents.reward_machine.machine import RewardMachine


class RegularRewardMachine(RewardMachine):
    def __init__(self):
        self.U = [0, 1, 2]
        self.F = [3]
        self.u_0 = 0

        self.delta_u = {
            (("A",), 0): 1,
            (("B",), 0): 3,
            (("C",), 0): 3,
            ((), 0): 0,
            (("A",), 1): 3,
            (("B",), 1): 2,
            (("C",), 1): 3,
            ((), 1): 1,
            (("A",), 2): 3,
            (("B",), 2): 3,
            (("C",), 2): 3,
            ((), 2): 2,
        }
        self.delta_r = {
            (("A",), 0): 0,
            (("B",), 0): 0,
            (("C",), 0): 0,
            ((), 0): 0,
            (("A",), 1): 0,
            (("B",), 1): 0,
            (("C",), 1): 0,
            ((), 1): 0,
            (("A",), 2): 0,
            (("B",), 2): 0,
            (("C",), 2): 1,
            ((), 2): 0,
        }