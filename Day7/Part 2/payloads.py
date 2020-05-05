from itertools import permutations
import processer

class PAYLOAD():

    def amplifiers (self, code, amp_input = 0, loop_amps = True):
        amp_inputs = permutations(range(5,10))
        thruster_out_max = 0
        for combos in amp_inputs:
            for phase in combos:
                while loop_amps:
                    amp_out, loop_amps = processer.processor(phase, amp_input, code)
                    amp_input = amp_out



        return thruster_out_max, combo_out