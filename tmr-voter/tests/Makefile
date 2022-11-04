# TOPLEVEL_LANG: verilog 
# SIM : icarus  

TOPLEVEL_LANG ?= verilog

PWD=$(shell pwd)

export PYTHONPATH := $(PWD)/../model:$(PYTHONPATH)

SIM ?= icarus
VERILOG_SOURCES = $(PWD)/../hdl/voter_2_of_3.v

TOPLEVEL := voter_2_of_3
MODULE   := test_voter

include $(shell cocotb-config --makefiles)/Makefile.sim
