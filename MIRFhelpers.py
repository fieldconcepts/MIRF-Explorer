from MIRFheaders import *
import struct

class MIRFGeneralHeader(object):
    
    def __init__(self, header=None):
        


        if header is None:
            self.create_empty_general_header()
        else:
            self.read_general_header(header)



    def create_empty_general_header(self):
        for line in GENERAL_HEADER_FORMAT:
            setattr(self, line[2], 0)

    # read in the 512 bytes long header and unpacks all values into correspding class attributes
    def read_general_header(self, header):
        cursor = 0
        
        for line in GENERAL_HEADER_FORMAT:
            length, type, name, _ = line
            
            if type == 'float32':
                rawbytes = header[cursor : cursor + length]
                [value]= struct.unpack('f', rawbytes)
                setattr(self, line[2], value)

            elif type == 'int32':
                rawbytes = header[cursor : cursor + length]
                value = int.from_bytes(rawbytes, byteorder='little', signed=True) 
                setattr(self, line[2], value)
            
            elif type == 'unicode':
                rawbytes = header[cursor : cursor + length]
                value = rawbytes.decode("utf-8") 
                setattr(self, line[2], value)

            cursor += length


class MIRFTraceHeader(object):
    
    def __init__(self, header=None):
        
        if header is None:
            self.create_empty_trace_header()
        else:
            self.read_trace_header(header)
        
        self.create_raw_data_attribute()
  
    
    # add all the field from TRACE HEADER FORMAT and create new attribute for the class setting values to zero
    def create_empty_trace_header(self):
        for line in TRACE_HEADER_FORMAT:
            setattr(self, line[2], 0)
    
    
    # read in the 64 bytes long header and unpacks all values into correspding class attributes
    def read_trace_header(self, header):
        cursor = 0
        
        for line in TRACE_HEADER_FORMAT:
            length, type, name, _ = line
            
            if type == 'float32':
                rawbytes = header[cursor : cursor + length]
                [value]= struct.unpack('f', rawbytes)
                setattr(self, line[2], value)

            elif type == 'int32':
                rawbytes = header[cursor : cursor + length]
                value = int.from_bytes(rawbytes, byteorder='little', signed=True) 
                setattr(self, line[2], value)
            
            elif type == 'unicode':
                rawbytes = header[cursor : cursor + length]
                value = rawbytes.decode("utf-8") 
                setattr(self, line[2], value)
            
            cursor += length

    # add a raw data attribute if one does not already exist
    def create_raw_data_attribute(self):
        value = []
        setattr(self, 'Raw_data', value)


def MIRFheader(file):

    #open file and make general header object
    with open(file, 'rb') as fd:
        
        #move cursor to byte 0
        fd.seek(0)
        
        #grab first 512bytes from file. Create Header object and get number of channels 
        general_header_block = fd.read(512)
        headerObject = MIRFGeneralHeader(general_header_block)
        return headerObject

def getTraceHeaderObjects(file, num_of_channels):
    #open file and make list trace header objects
    with open(file, 'rb') as fd:
        
        #move cursor to byte 512
        fd.seek(512)
        
        #empty array to hold all the trace
        trace_headers_list = []
        
        #loop through all channels defined by the generel header block
        for i in range (num_of_channels):
            
            #each trace header is only 64 byte
            trace_header_block = fd.read(64)
            
            #create trace header objects
            traceObject = MIRFTraceHeader(trace_header_block)
            
            #check is the channels that are unused - if NS =0 then chanel is unused.
            if traceObject.NS != 0:
                
                #only add the trace object to the array is NS !=0
                trace_headers_list.append(traceObject)
        
        return trace_headers_list
        
        # number of actual real data channels
        
def getRawData(file, traceObjectList, num_of_channels, number_of_data_channels):
    #open file and add raw data to the trace objects
    with open(file, 'rb') as fd:
        
        #create the main trace list that will include header and data info
        MIRFdata = []
        
        #caluclate beginning of first data trace
        first_byte_of_surface_channels = 512 + (64 * num_of_channels)
        
        #move cursor to byte 512 + 64 * defined channels
        fd.seek(first_byte_of_surface_channels)
        
        for j in range(number_of_data_channels):

            channel = traceObjectList[j]
        
            #Check format code of trace and decode bytes accordingly. 5 = 24bit decode
            if channel.Format_code == 5:

                #empty array to store raw data
                temp_raw_data = []
                
                for i in range(channel.NS):
                    threebytes = fd.read(3)
                    value = int.from_bytes(threebytes, byteorder='big', signed=True)
                    
                    #adjust values to take into acount scaling factor and dc offset
                    value = value * channel.SF
                    value = value - channel.DC
                    value = value * channel.SSF

                    
                    #append adjsuted value to temp array
                    temp_raw_data.append(value)
                
                #update the Raw_data attribute in the trace class
                channel.Raw_data = temp_raw_data

                MIRFdata.append(channel)
            
            #Check format code of trace and decode bytes accordingly. 16bits (2 bytes per sample). Fourteen most sig bit hold twos compliment mantissa a
            # Two least significant bits hold exponent.
            
            elif channel.Format_code == 2:

                #empty array to store raw data
                temp_raw_data = []
                
                for i in range(channel.NS):
                    twobytes = fd.read(2)
                
                    #pull in a signed littel endian integer, this will be used for the bit shift operation
                    IFP_signed_integer = int.from_bytes(twobytes, byteorder='little', signed=True) 

                    #pull in unsigned little endian integer, this will be used grabbing the exponents in twos complements format
                    IFP_unsigned_integer = int.from_bytes(twobytes, byteorder='little', signed=False)
                    
                    #get the binary representation of the IFP unsigned short.
                    binstring = "{0:b}".format(IFP_unsigned_integer)

                    #split binary string into exponet and get last 2 bits for the exponents decode.
                    exponent = binstring[-2:]

                    #divide matissa by 4 (or bit shift twice to right) to take up space of exponets
                    mantissa = float(IFP_signed_integer >> 2 )

                    #get the gain code and correspding mulitplaction factor from expoennts.
                    gain_code = int(exponent,2)

                    xGain = 1
                    if gain_code == 0:
                        xGain = 1
                    elif gain_code == 1:
                        xGain = 4
                    elif gain_code == 2:
                        xGain = 16
                    elif gain_code == 3:
                        xGain = 64
                    
                    value = mantissa * channel.SF   #mulitply by scaling factorn 
                    value = value / xGain           #divide by gain facto
                    value = value - channel.DC      #Subtract dc offset

                    #append adjsuted value to temp array
                    temp_raw_data.append(value)
                
                #update the Raw_data attribute in the trace class
                channel.Raw_data = temp_raw_data
                
                MIRFdata.append(channel)

        return MIRFdata

def MIRFdata(file):

    #open file and create header object
    headerObject = MIRFheader(file)

    #get number of channels from header object
    num_of_channels = headerObject.Channels_defined

    #create list of trace header obejcts
    traceObjectList = getTraceHeaderObjects(file,num_of_channels)

    #get number of real channels exlcuding empty channels
    number_of_data_channels = len(traceObjectList)

    #create list of trace headers with data
    MIRFdata = getRawData(file, traceObjectList, num_of_channels, number_of_data_channels)

    return MIRFdata

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

def owner_translate(value):
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


