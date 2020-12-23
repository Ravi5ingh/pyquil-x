import pyquil as py
import pyquil.api as ap
import pyquil.gates as ga

# program = py.Program(ga.Z(0), ga.CNOT(0, 1))
#
# with ap.local_forest_runtime():
#     qvm = py.get_qc('9q-square-qvm')
#     results = qvm.run_and_measure(program, trials=10)

p = py.Program(ga.H(0), ga.CNOT(0, 1))

qc = py.get_qc('9q-square-qvm')
result = qc.run_and_measure(p, trials=10)
print(result[0])
print(result[1])