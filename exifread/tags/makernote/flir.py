#Based on the work of Phil Harvey
#http://www.sno.phy.queensu.ca/~phil/exiftool/TagNames/FLIR.html
#Information extracted from the maker notes of JPEG images from thermal imaging cameras by FLIR Systems Inc.
#Tag ID
TAGS = {
0x0001: ('ImageTemperatureMax',),
0x0002: ('ImageTemperatureMin',),
0x0003: ('Emissivity',),
0x0004: ('UnknownTemperature',),
0x0005: ('CameraTemperatureRangeMax?',),
0x0006: ('CameraTemperatureRangeMin?',)
}

#Information extracted from FLIR FFF images and the FLIR APP1 segment of JPEG images.
#Tag ID    Tag Name       Values 
#'_header' FFFHeader ---> FLIR Header Tags
FFF_TAGS = {
    0x0001: ('RawData',),
    0x0005: ('GainDeadData',),
    0x0006: ('CoarseData',),
    0x000E: ('EmbeddedImage',),
    0x0020: ('CameraInfo',),
    0x0021: ('MeasurementInfo',),
    0x0022: ('PaletteInfo',),
    0x0023: ('TextInfo',),
    0x0024: ('EmbeddedAudioFile',),
    0x0028: ('PaintData',),
    0x002A: ('PiP',),
    0x002B: ('GPSInfo',),
    0x002C: ('MeterLink',),
    0x002E: ('ParameterInfo',)
}

#Index2
RAWDATA = {
    1: ('RawThermalImageWidth',),
    2: ('RawThermalImageHeight',),
    16: ('RawThermalImageType',)
#16.1 	RawThermalImage
}

#Index2
GAINDEADDATA = {
    1: ('GainDeadMapImageWidth',),
    2: ('GainDeadMapImageHeight',),
    16: ('GainDeadMapImageType',)
#16.1 	GainDeadMapImage 	N
}

#Index2
COARSEDATA = {
    1: ('CoarseMapImageWidth',),
    2: ('CoarseMapImageHeight',),
    16: ('CoarseMapImageType')
#16.1 	CoarseMapImage 	N
}

EMBEDDEDIMAGE 