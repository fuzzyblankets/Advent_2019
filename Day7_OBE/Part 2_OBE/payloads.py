from itertools import permutations
import processor

class AMPS():
    def __init__(self, start, end, loopback_mode):
        self.start= int(start)
        self.end = int(end)
        self.loopback_mode = loopback_mode

    def output (self, code, inp_range_start, inp_range_end, loopback_mode=False):
        amp_inputs = permutations(range(inp_range_start,inp_range_end+1))
        thruster_out_max = 0
        for combos in amp_inputs:
            amp_input = 0
            for phase in combos:
                amp_out = processor.processor(code, amp_input, phase)
                amp_input = amp_out
            while loopback_mode:
                amp_out_loop = processor.processor(code, amp_input, phase)
                if amp_out_loop is None:
                    break
                amp_input = amp_out_loop
                amp_out = amp_out_loop
            if amp_out > thruster_out_max:
                thruster_out_max = amp_out
                combo_out = combos

        return thruster_out_max, combo_out

    def loopback (self, code, amp_input):
        return processor.processor(phase, amp_input, code)
