from itertools import permutations
import processor

class PAYLOAD():

    def amplifiers (self, code, inp_range_start, inp_range_end, amp_input = 0):
        amp_inputs = permutations(range(inp_range_start,inp_range_end+1))
        thruster_out_max = 0
        for combos in amp_inputs:
            for phase in combos:
                amp_out, loop_amps = processor.processor(phase, amp_input, code)
                amp_input = amp_out
            if amp_out > thruster_out_max:
                thruster_out_max = amp_out
                combo_out = combos



        return thruster_out_max, combo_out