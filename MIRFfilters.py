from scipy.signal import iirfilter
from scipy.signal import sosfilt
from scipy.signal import zpk2sos

def bandpass(data, freq_min, freq_max, sample_frequency, corners=4):
    """
    Zero-Phase Butterworth-Bandpass Filter.

    Filter data from ``freqmin`` to ``freqmax`` using ``corners``
    corners.
    The filter uses :func:`scipy.signal.iirfilter` (for design)
    and :func:`scipy.signal.sosfilt` (for applying the filter).

    :type data: numpy.ndarray
    :param data: Data to filter.
    :param freqmin: Pass band low corner frequency.
    :param freqmax: Pass band high corner frequency.
    :param df: Sampling rate in Hz.
    :param corners: Filter corners / order.
    :return: Filtered data.
    """
    nyquist = 0.5 * sample_frequency
    low = freq_min / nyquist
    high = freq_max / nyquist
    
    zeroes, poles, gain = iirfilter(corners, [low, high], btype='band', ftype='butter', output='zpk')
    sos = zpk2sos(zeroes, poles, gain)
    
    firstpass = sosfilt(sos, data)
    return sosfilt(sos, firstpass[::-1])[::-1]
    