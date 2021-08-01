#!/usr/bin/make

.PHONY: clean ivl vltr vsim

.DEFAULT_GOAL := ivl


clean:
	@rm -rf build/


ivl: clean
	@python run_edalize.py icarus


# verilator -f blinky_project.vc 
# %Warning-STMTDLY: ../blinky_tb.v:10: Unsupported: Ignoring delay on this delayed statement.
#   always #clk_half_period clk <= !clk;
vltr: clean
	@python run_edalize.py verilator


vsim: clean
	@export MODEL_TECH=/opt/altera/20.1/modelsim_ase/bin && \
	python run_edalize.py modelsim