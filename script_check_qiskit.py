import qiskit
print('qiskit version', qiskit.__qiskit_version__)
try:
    # from qiskit.opflow.evolutions import PauliTrotterEvolution  # Deprecated
    print('PauliTrotterEvolution import ok')
except Exception as e:
    print('PauliTrotterEvolution error', e)
try:
    from qiskit.quantum_info import PauliList
    print('PauliList import ok')
except Exception as e:
    print('PauliList error', e)
