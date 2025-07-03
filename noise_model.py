from qiskit_aer import noise
from qiskit_aer.noise import (NoiseModel, ReadoutError, depolarizing_error, thermal_relaxation_error)


# IBM torino. The dataset is saved in a folder named data_ibm_torino.
T1 = [171.967863, 152.728335141796, 13.2054432977472, 266.581226157921, 61.8336922854567, 124.955878334868, 214.843271318771, 76.6650530665129]
T2 = [155.433384330652, 138.442507232412, 15.4473758905583, 245.072617607131, 107.762500111648, 63.2275748975155, 225.226564994028, 59.3047500067739]
P01 = [0.0052, 0.009, 0.0208, 0.008, 0.0144, 0.0162, 0.0166, 0.0222, 0, 0, 0, 0, 0, 0, 0, 0]
P10 = [0.0038, 0.0052, 0.0038, 0.0184, 0.0056, 0.0056, 0.01, 0.0176, 0, 0, 0, 0, 0, 0, 0, 0]
gateErrors = [['rx', 0.000354, 0.0003695, 0.0010775, 0.000282, 0.000763, 0.00031, 0.0001195, 0.000202],
              ['i', 0.00035428, 0.0003695, 0.0010775, 0.0002823, 0.00076, 0.000315756, 0.0001195, 0.000202],
              ['sx', 0.00035428, 0.0003695, 0.0010775, 0.00028, 0.000763, 0.00031, 0.0001195, 0.000202],
              ['cx', 0.00503669, 0.003105, 0.0018, 0.002674, 0.00298, 0.002700386, 0.003066, 0.0026788],
              ['cz', 0.00503669, 0.003105, 0.0018, 0.002674, 0.00298, 0.002700386, 0.003066, 0.0026788],
              ['rz', 0, 0, 0, 0, 0, 0, 0, 0]]

'''
# IBM Perth. The dataset is saved in a folder named data_ibm_perth.
T1 = [197.79, 158.07, 278.36, 223.29, 109.91, 236.63, 193.96]
T2 = [97.02, 48.06, 83.1, 211, 126.96, 188.44, 291.83]
P01 = [0.31, 0.222, 0.282, 0.18, 0.23, 0.264, 0.072]
P10 = [0.226, 0.236, 0.23, 0.13, 0.164, 0.208, 0.054]
gateErrors = [['rz', 0.0001836, 0.0003291, 0.0002153, 0.0002381, 0.0003141, 0.0002563, 0.0003357],
              ['x', 0.0001836, 0.0003291, 0.0002153, 0.0002381, 0.0003141, 0.0002563, 0.0003357],
              ['sx', 0.0001836, 0.0003291, 0.0002153, 0.0002381, 0.0003141, 0.0002563, 0.0003357],
              ['cx', 0.0735, 0.0769667, 0.0694, 0.0835, 0.01169, 0.098133, 0.0984]]
'''

'''
# IBM Lagos. The dataset is saved in a folder named data_ibm_lagos.
T1 = [96, 131.71, 174.23, 139.45, 113.32, 131.19, 93.17]
T2 = [40.53, 75.18, 160.96, 84.68, 29.5, 64.52, 81.31]
P01 = [0.018, 0.0192, 0.0094, 0.0166, 0.021, 0.0148, 0.013]
P10 = [0.0092, 0.0178, 0.0074, 0.0144, 0.0198, 0.019, 0.0152]
gateErrors = [['rz', 1.813e-4, 1.439e-4, 2.279e-4, 1.988e-4, 2.090e-4, 1.975e-4, 1.845e-4],
              ['x', 1.813e-4, 1.439e-4, 2.279e-4, 1.988e-4, 2.090e-4, 1.975e-4, 1.845e-4],
              ['sx', 1.813e-4, 1.439e-4, 2.279e-4, 1.988e-4, 2.090e-4, 1.975e-4, 1.845e-4],
              ['cx', 0.006553, 0.00769667, 0.00685, 0.006505, 0.00723, 0.0068467, 0.00588]]
'''
'''
# IBM Nairobi. The dataset is saved in a folder named data_ibm_nairobi.
T1 = [104.92, 141.98, 57.67, 145.77, 99.1, 126.61, 148.77]
T2 = [26.07, 97.62, 69.22, 59.13, 61.06, 16.25, 105.21]
P01 = [0.0318, 0.072, 0.0406, 0.0366, 0.0326, 0.0432, 0.041]
P10 = [0.011, 0.0198, 0.0116, 0.0096, 0.0098, 0.0204, 0.0142]
gateErrors = [['rz', 2.782e-4, 5.325e-4, 0.00365, 3.363e-4, 2.725e-4, 2.855e-4, 2.028e-4],
              ['x', 2.782e-4, 5.325e-4, 0.00365, 3.363e-4, 2.725e-4, 2.855e-4, 2.028e-4],
              ['sx', 2.782e-4, 5.325e-4, 0.00365, 3.363e-4, 2.725e-4, 2.855e-4, 2.028e-4],
              ['cx', 0.01034, 0.01765, 0.03446, 0.01259, 0.00954, 0.0111767, 0.00696]]
'''
'''
# IBM Jakarta. The dataset is saved in a folder named data_ibm_jakarta.
T1 = [145.55, 143.21, 110.89, 78.53, 145.55, 128.7, 139.55]
T2 = [47.91, 28.18, 22.67, 36.52, 47.91, 65.54, 21.58]
P01 = [0.0282, 0.0396, 0.0252, 0.0254, 0.0282, 0.0646, 0.04]
P10 = [0.007, 0.0096, 0.0082, 0.0112, 0.007, 0.048, 0.0244]
gateErrors = [['rz', 3.194e-4, 2.136e-4, 2.076e-4, 2.149e-4, 3.194e-4, 2.627e-4, 2.507e-4],
              ['x', 3.194e-4, 2.136e-4, 2.076e-4, 2.149e-4, 3.194e-4, 2.627e-4, 2.507e-4],
              ['sx', 3.194e-4, 2.136e-4, 2.076e-4, 2.149e-4, 3.194e-4, 2.627e-4, 2.507e-4],
              ['cx', 0.00806, 0.00872, 0.00914, 0.007755, 0.00806, 0.00616, 0.00577]]
'''
# Generate a noise model including the quantum gates [‘rz’, ‘rx’, ‘i’, ‘cz’].
def creat_noise_model(number_of_qubits):

    # Add errors to noise model
    noise_model = noise.NoiseModel()
    for i in range(number_of_qubits):
        noise_model.add_quantum_error(depolarizing_error(gateErrors[0][i + 1], 1), ['rz', 'rx', 'i'], [i])
        for k in range(number_of_qubits):
            noise_model.add_quantum_error(depolarizing_error((gateErrors[3][i + 1] + gateErrors[3][k + 1]) / 2, 2),
                                          ['cz'], [i, k])

    # Add T1 and T2 relaxation times
    # Instruction times (in nanoseconds)
    time_reset = 1000  # 1 microsecond
    time_measure = 1000  # 1 microsecond
    time_rz = 100  # virtual gate
    time_x = 100  # virtual gate
    time_sx = 100  # (single X90 pulse)
    time_i = 100  # (two X90 pulses)
    time_cx = 300

    # QuantumError objects
    errors_reset = [thermal_relaxation_error(t1 * 1000, t2 * 1000, time_reset)
                    for t1, t2 in zip(T1, T2)]
    errors_measure = [thermal_relaxation_error(t1 * 1000, t2 * 1000, time_measure)
                      for t1, t2 in zip(T1, T2)]
    errors_rz = [thermal_relaxation_error(t1 * 1000, t2 * 1000, time_rz)
                 for t1, t2 in zip(T1, T2)]
    errors_x = [thermal_relaxation_error(t1 * 1000, t2 * 1000, time_x)
                 for t1, t2 in zip(T1, T2)]
    errors_sx = [thermal_relaxation_error(t1 * 1000, t2 * 1000, time_sx)
                for t1, t2 in zip(T1, T2)]
    errors_i = [thermal_relaxation_error(t1 * 1000, t2 * 1000, time_i)
                 for t1, t2 in zip(T1, T2)]
    errors_cx = [[thermal_relaxation_error(t1a * 1000, t2a * 1000, time_cx).expand(
        thermal_relaxation_error(t1b * 1000, t2b * 1000, time_cx))
        for t1a, t2a in zip(T1, T2)]
        for t1b, t2b in zip(T1, T2)]

    # Add errors to noise model
    for j in range(number_of_qubits):
        noise_model.add_quantum_error(errors_reset[j], "reset", [j])
        noise_model.add_quantum_error(errors_measure[j], "measure", [j])
        noise_model.add_quantum_error(errors_rz[j], "rz", [j])
        noise_model.add_quantum_error(errors_x[j], "rx", [j])
        noise_model.add_quantum_error(errors_sx[j], "ry", [j])
        noise_model.add_quantum_error(errors_i[j], "i", [j])
        for k in range(number_of_qubits):
            noise_model.add_quantum_error(errors_cx[j][k], "cz", [j, k])

    # Add readout errors
    # Measurement miss-assignement probabilities
    for i in range(number_of_qubits):
        noise_model.add_readout_error(ReadoutError([[1 - P10[i], P10[i]], [P01[i], 1 - P01[i]]]), [i])

    print(noise_model)
    return noise_model

def creat_depolarizing_noise_model(number_of_qubits):
    # Create a depolarizing noise model
    p = 0.1  # Probability of depolarizing noise
    noise_model = NoiseModel()

    error = depolarizing_error(p, 1)
    noise_model.add_all_qubit_quantum_error(error, ['i', 'rx', 'ry', 'rz'])

    # Add depolarizing noise to the CZ gate
    noise_model.add_all_qubit_quantum_error(depolarizing_error(p, 2), ['cz'])

    return noise_model