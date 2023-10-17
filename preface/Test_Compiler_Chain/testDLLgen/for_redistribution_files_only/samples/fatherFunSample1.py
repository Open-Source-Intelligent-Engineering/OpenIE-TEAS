#!/usr/bin/env python
"""
Sample script that uses the testFun module created using
MATLAB Compiler SDK.

Refer to the MATLAB Compiler SDK documentation for more information.
"""

import testFun
# Import the matlab module only after you have imported
# MATLAB Compiler SDK generated Python modules.
import matlab

my_testFun = testFun.initialize()

inputIn = matlab.double([4.0], size=(1, 1))
resultOut = my_testFun.fatherFun(inputIn)
print(resultOut, sep='\n')

my_testFun.terminate()
