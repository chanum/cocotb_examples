# cocotb_examples (Cocotb + Icarus Verilog/GHDL +  GTKWave)

## Setup 

Cocotb [Installation Guide](https://docs.cocotb.org/en/stable/install.html)

> sudo apt-get install make gcc g++ python3 python3-dev python3-pip
> pip install cocotb

Compilador & simulador verilog: Icarus Verilog

> sudo apt install iverilog

Compilador & simulador VHDL: GHDL

> sudo apt install ghdl

Simulators Cocotb [notes](https://docs.cocotb.org/en/stable/simulator_support.html)

Waveform viewer: gtkwave
> sudo apt install gtkwave

## Run Test

> cd cocotb_examples/adder/tests

> make

Change the RTL source language and compiler in Makefile:

VERILOG
- TOPLEVEL_LANG: verilog 
-  SIM : icarus  

VHDL
-  TOPLEVEL_LANG: vhdl
- SIM : ghdl




