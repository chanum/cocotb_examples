
import random

from voter_model import voter_model

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, Timer, ClockCycles

@cocotb.test()
async def voter_basic_test(dut):
    dut._log.info("start")
    A = 1
    B = 1
    C = 0

    clock = Clock(dut.clock, 10, units="ns")
    cocotb.fork(clock.start())
    
    dut._log.info("reset")
    dut.reset_in.value = 1
    await ClockCycles(dut.clock, 10)
    dut.reset_in.value = 0

    dut.a_in.value = A
    dut.b_in.value = B
    dut.c_in.value = C

    await Timer(100, units="ns")

    assert dut.v_out.value == voter_model(
        A, B, C
    ), f"Voter result is incorrect: {dut.v_out.value} != 1"


# @cocotb.test()
# async def tmr_randomised_test(dut):
#     """Test for adding 2 random numbers multiple times"""

#     for i in range(10):

#         A = random.randint(0, 15)
#         B = random.randint(0, 15)

#         dut.A.value = A
#         dut.B.value = B

#         await Timer(2, units="ns")

#         assert dut.X.value == tmr_model(
#             A, B
#         ), "Randomised test failed with: {A} + {B} = {X}".format(
#             A=dut.A.value, B=dut.B.value, X=dut.X.value
#         )
