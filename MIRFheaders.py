GENERAL_HEADER_FORMAT = [
    # [length, type, name, mandatory]
    [4, 'int32', 'MIRF_version', True],
    [4, 'int32', 'File_type', True],
    [4, 'int32', 'Format_code', True],
    [4, 'int32', 'Correaltion_flag', True],
    [4, 'int32', 'Controller_Type', True],
    [4, 'int32', 'Tool_system', True],
    [4, 'int32', 'Channels_defined', True],
    [4, 'int32', 'Test_mode', True],
    [4, 'int32', 'Dataset_id', True],
    [4, 'int32', 'Year', True],
    [4, 'int32', 'Month', True],
    [4, 'int32', 'Day', True],
    [4, 'int32', 'Hour', True],
    [4, 'int32', 'Minute', True],
    [4, 'int32', 'Second', True],
    [4, 'int32', 'Timezone_bias_seconds', True],
    [4, 'int32', 'Source_id', True],
    [4, 'int32', 'Number_of_receivers', True],
    [4, 'int32', 'Receiver_number', True],
    [4, 'int32', 'Number_in_stack', True],
    [4, 'int32', 'Measurement_units', True],
    [4, 'int32', 'Receiver_polarity', True],
    [4, 'int32', 'Source_reference_channel', True],
    [4, 'int32', 'reserved', True],
    [4, 'int32', 'Record_number', True],
    [4, 'int32', 'Stack_number', True],
    [4, 'int32', 'Fix_number', True],
    [4, 'int32', 'Tool_MD', True],
    [4, 'int32', 'SIus', True],
    [4, 'int32', 'Line_number', True],
    [4, 'int32', 'Gun_pressure', True],
    [4, 'int32', 'Software_version_x100', True],
    [4, 'int32', 'SCX', True],
    [4, 'int32', 'SCY', True],
    [4, 'int32', 'TCX', True],
    [4, 'int32', 'TCY', True],
    [4, 'int32', 'WRE_(aka WREF)', True],
    [4, 'int32', 'SRE_(aka SREF)', True],
    [4, 'int32', 'SD', True],
    [4, 'int32', 'S2M', True],
    [4, 'int32', 'Source_elevation_error', True],
    [4, 'int32', 'External_reference_delay_us', True],
    [4, 'int32', 'Supplied_Ts_us', True],
    [4, 'int32', 'TB_advance_us', True],
    [4, 'int32', 'Tool_skew_us', True],
    [4, 'int32', 'Raw_SCX_x10', True],
    [4, 'int32', 'Raw_SCY_x10', True],
    [4, 'int32', 'Controller_second', True],
    [4, 'int32', 'Microsecond', True],
    [4, 'int32', 'Timestamp_mode', True],
    [4, 'int32', 'SDE', True],
    [4, 'int32', 'Error_control', True],
    [4, 'int32', 'Microseismic_mode', True],
    [4, 'int32', 'Overlap_samples', True],
    [108, 'unicode', 'GPRMC_data', True],
    [188, 'int32', 'Reserved', True]]

TRACE_HEADER_FORMAT = [
    # [length, type, name, mandatory]
    [4, 'int32', 'Legacy_owner', True],
    [4, 'int32', 'Descriptor', True],
    [4, 'int32', 'Format_code', True],
    [4, 'int32', 'NS', True],
    [4, 'int32', 'Pointer_us', True],
    [4, 'int32', 'Owner', True],
    [4, 'int32', 'RCX', True],
    [4, 'int32', 'RCY', True],
    [4, 'int32', 'TVD', True],
    [4, 'int32', 'MDO', True],
    [4, 'float32', 'HSI', True],
    [4, 'int32', 'reserved', True],
    [4, 'float32', 'SSF', True],
    [4, 'float32', 'DC', True],
    [4, 'float32', 'SF', True],
    [4, 'float32', 'Max_magnitude', True]]


def owner_translate(value):
    value_translated = ""
    
    if value == 0:
        value_translated = ""
    elif value == -1:
        value_translated = "AUX"
    elif value == -2:
        value_translated = "REF"
    else: 
        value_translated = "GEO {}".format(value)
    
    
    return value_translated

def description_translate(value):
    value_translated = ""
    
    if value == 0:
        value_translated = ""
    elif value == 1:
        value_translated = "VZ"
    elif value == 2:
        value_translated = "HX"
    elif value == 3:
        value_translated = "HY"
    elif value == 4:
        value_translated = "DH"
    elif value == 5:
        value_translated = "HYDRO"
    elif value == 6:
        value_translated = "PILOT"
    elif value == 7:
        value_translated = "TB"
    elif value == 8:
        value_translated = "GF"
    elif value == 9:
        value_translated = "RM"
    elif value == 10:
        value_translated = "BP"
    elif value == 11:
        value_translated = "PPS"
    elif value == 12:
        value_translated = "VSIM"
    elif value == 13:
        value_translated = "RSIM"
    elif value == 14:
        value_translated = "NGEO"
    elif value == 15:
        value_translated = "FGEO"
    
    return value_translated