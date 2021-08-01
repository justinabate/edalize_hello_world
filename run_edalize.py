from edalize import *
import os
from argparse import ArgumentParser


cli = ArgumentParser()
cli.add_argument("tool", type=str) # icarus, modelsim, verilator
args = cli.parse_args()


work_root = 'build'

files = [
  {'name' : os.path.relpath('blinky.v', work_root), 'file_type' : 'verilogSource'},
  {'name' : os.path.relpath('blinky_tb.v', work_root), 'file_type' : 'verilogSource'},
  {'name' : os.path.relpath('vlog_tb_utils.v', work_root), 'file_type' : 'verilogSource'}
]

parameters = {'clk_freq_hz' : {'datatype' : 'int', 'default' : 1000, 'paramtype' : 'vlogparam'},
              'vcd' : {'datatype' : 'bool', 'paramtype' : 'plusarg'}}

# EDA Metadata - https://edalize.readthedocs.io/en/latest/edam/api.html
edam = {
  'files'        : files,
  'name'         : 'blinky_project',
  'parameters'   : parameters,
  'toplevel'     : 'blinky_tb'
}

tool = args.tool

backend = get_edatool(tool)(edam=edam, work_root=work_root)

os.makedirs(work_root)
backend.configure()

backend.build()

args = {'vcd' : True}
backend.run(args)