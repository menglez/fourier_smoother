import matplotlib.pyplot as plt
import numpy as np

#from scipy.fft import fft
from numpy.fft import fft, ifft



def func_furier_new_series(df, col, frequency_threshold = 0.1, plot = False ):

    df = df.copy()

    # Perform Fourier transform
    # fft_values = fft(df['spread'].values )
    fft_values = fft(df[col].values )
    frequencies = np.fft.fftfreq(len(fft_values))

    # Define a frequency threshold to remove (example: remove high frequencies)
    frequency_threshold = frequency_threshold

    # Zero-out the undesired frequencies
    fft_result = fft_values
    filtered_fft_result = fft_result.copy()
    filtered_fft_result[np.abs(frequencies) > frequency_threshold] = 0

    # Apply inverse FFT
    filtered_values = np.fft.ifft(filtered_fft_result)
    df['filtered__fft'] = filtered_values.real


    if plot == True:

        # Create figure and three subplots with equal height ratios
        fig, (ax1, ax2) = plt.subplots(
            2, 1, figsize=(20, 8), sharex=True, gridspec_kw={'height_ratios': [1, 1]} )

        ax1.plot(frequencies, np.abs(fft_values), label='Frequency vs Amplitude')
        ax1.set_xlabel('Frequency')
        ax1.set_ylabel('Amplitude')
        ax1.legend(loc='upper left')
        ax1.grid(True)
        ax1.set_title('Fourier Transform')

        ax2.plot(np.abs(fft_values), label='Frequencies')
        ax2.legend(loc='upper left')
        ax2.grid(True)





    if False:
        # Plot the Fourier transform
        plt.figure(figsize=(18, 4))
        plt.plot(frequencies, np.abs(fft_values), label='Frequency vs Amplitude')
        plt.title('Fourier Transform')
        plt.xlabel('Frequency')
        plt.ylabel('Amplitude')
        plt.grid()
        plt.tight_layout()
        plt.legend()
        plt.show()


        plt.figure(figsize=(18, 4))
        plt.plot(np.abs(fft_values), label='Frequencies')
        plt.grid()
        plt.tight_layout()
        plt.legend()
        plt.show()


        plt.figure(figsize=(18, 5))
        plt.plot(df[col], label=f'{col}')
        plt.plot(df['filtered__fft'], label='filtered__fft')
        plt.grid()
        plt.tight_layout()
        plt.legend()
        plt.show()




    return df