
import random

from voter_model import voter_model

import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def voter_basic_test(dut):
    """Test for 1 1 0 """

    A = 1
    B = 1
    C = 0

    dut.a_in.value = A
    dut.b_in.value = B
    dut.c_in.value = C

    await Timer(2, units="ns")

    assert dut.X.value == tmr_model(
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
