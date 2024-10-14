Modern CPUs are very complex, and as a result, can't be designed by placing logic gates by hand. Thus, there have been several hardware description languages (HDLs) created to describe and build these circuits:
- Verilog (1984, Standardised as IEEE1364)
- VHDL (1980s, Standardised as IEEE1076-2019)
- System Verilog (2002, Standardised as IEEE1800-2005)
We will focus on System Verilog, and its use within AMD's *Vivado* FPGA simulation software.
### FPGAs
It is incredibly difficult and costly to build semiconductor dies and can often take years to begin production. Thus, there are types of dies, such that their function is not specialised, and can be reshaped, often on the fly with custom logic. Though there are several different types, the one most commonly used nowadays is the *Field Programmable Gate Array*. These are made of blocks of logic gates which can be turned on and off programmatically. It is important to note that this is a volatile form of memory.
### Defining Modules
```verilog
module full_adder (
	input logic a, b, c,
	output logic o1, o2
);
logic i, j, k, l

xor g0 (i, a, b); 
xor g1 (sum, i, carryIn); 
and g2 (j, a, b);
and g3 (k, a, carryIn); 
and g4 (l, b, carryIn); 
or g5 (carryOut, j, k, l); 
endmodule;
```
The above code defines a module in System Verilog. 
> [!Note] Naming Modules
> Note that that the filename and name of the module should be the same to prevent *Vivado* from throwing a fit.

The first statement, `module(...);` defines the inputs, outputs and name of a module. On the first line, should always be `input logic`, followed by each of the inputs. The next line should always contain `output logic`, followed by each of the outputs.
In the above code, the `logic` statement defines any intermediary points in the circuit diagram.
Below, each logic gate is defined, with its type, name, output and input. Using the first gate as an example:
- `xor` $\rightarrow$ gate type
- `g0` $\rightarrow$ gate name
- `i` $\rightarrow$ gate output node
- `a`, `b` $\rightarrow$ gate input nodes
The output node of a gate is always the first argument.
To finish a module definition, the `endmodule` statement is used.
