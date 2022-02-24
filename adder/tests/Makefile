# TOPLEVEL_LANG: vhdl - verilog 
# SIM : ghdl - icarus  

TOPLEVEL_LANG ?= vhdl

PWD=$(shell pwd)

export PYTHONPATH := $(PWD)/../model:$(PYTHONPATH)

ifeq ($(TOPLEVEL_LANG),verilog)
    SIM ?= icarus
    VERILOG_SOURCES = $(PWD)/../hdl/adder.sv
else ifeq ($(TOPLEVEL_LANG),vhdl)
    SIM ?= ghdl
    SIM_ARGS+=--vcd=dump.vcd
    VHDL_SOURCES = $(PWD)/../hdl/adder.vhdl
else
    $(error "A valid value (verilog or vhdl) was not provided for TOPLEVEL_LANG=$(TOPLEVEL_LANG)")
endif

TOPLEVEL := adder
MODULE   := test_adder

include $(shell cocotb-config --makefiles)/Makefile.sim
