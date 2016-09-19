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

#Index2 = multiplier for calculating a byte offset is 2
RAWDATA = {
    1: ('RawThermalImageWidth',),
    2: ('RawThermalImageHeight',),
    16: ('RawThermalImageType',)
#16.1 RawThermalImage
}

#Index2 = multiplier for calculating a byte offset is 2
GAINDEADDATA = {
    1: ('GainDeadMapImageWidth',),
    2: ('GainDeadMapImageHeight',),
    16: ('GainDeadMapImageType',)
#16.1 GainDeadMapImage
}

#Information found in FFF-format .CRS correction image files.
#Index2 = multiplier for calculating a byte offset is 2
COARSEDATA = {
    1: ('CoarseMapImageWidth',),
    2: ('CoarseMapImageHeight',),
    16: ('CoarseMapImageType')
#16.1 CoarseMapImage
}

#Index2 = multiplier for calculating a byte offset is 2
EMBEDDEDIMAGE = {
    1: ('EmbeddedImageWidth',),
    2: ('EmbeddedImageHeight',),
    16: ('EmbeddedImageType',)
#16.1 EmbeddedImage
}

#FLIR camera information. The Planck tags are variables used in the temperature calculation
#Index1 = multiplier for calculating a byte offset is 1
CAMERAINFO = {
    32: ('Emissivity',),
    36: ('ObjectDistance',),
    40: ('ReflectedApparentTemperature',),
    44: ('AtmosphericTemperature',),
    48: ('IRWindowTemperature',),
    52: ('IRWindowTransmission',),
    60: ('RelativeHumidity',),
    88: ('PlanckR1',),
    92: ('PlanckB',),
    96: ('PlanckF',),
    112: ('AtmosphericTransAlpha1',),
    116: ('AtmosphericTransAlpha2',),
    120: ('AtmosphericTransBeta1',),
    124: ('AtmosphericTransBeta2',),
    128: ('AtmosphericTransX',),
    144: ('CameraTemperatureRangeMax',),
    148: ('CameraTemperatureRangeMin',),
    152: ('UnknownTemperature1?',),
    156: ('UnknownTemperature2?',),
    160: ('UnknownTemperature3?',),
    164: ('UnknownTemperature4?',),
    168: ('UnknownTemperature5?',),
    172: ('UnknownTemperature6?',),
    212: ('CameraModel',),
    244: ('CameraPartNumber',),
    260: ('CameraSerialNumber',),
    276: ('CameraSoftware',),
    368: ('LensModel',),
    400: ('LensPartNumber',),
    416: ('LensSerialNumber',),
    436: ('FieldOfView',),
    492: ('FilterModel',),
    508: ('FilterPartNumber',),
    540: ('FilterSerialNumber',),
    776: ('PlanckO',),
    780: ('PlanckR2',),
    824: ('RawValueMedian',),
    828: ('RawValueRange',),
    900: ('DateTimeOriginal',),
    912: ('FocusStepCount',),
    1116: ('FocusDistance')
}

#Index1 = multiplier for calculating a byte offset is 1
PALETTEINFO = {
    0: ('PaletteColors',),
    6: ('AboveColor',),
    9: ('BelowColor',),
    12: ('OverflowColor',),
    15: ('UnderflowColor',),
    18: ('Isotherm1Color',),
    21: ('Isotherm2Color',),
    26: ('PaletteMethod',),
    27: ('PaletteStretch',),
    48: ('PaletteFileName',),
    80: ('PaletteName',),
    112: ('Palette',)
}

#Index1 = multiplier for calculating a byte offset is 1
GPSInfo = {
    88: ('GPSMapDatum',)
}

#FLIR Picture in Picture tags.
#Index2 = multiplier for calculating a byte offset is 2
PIP = {
    0: ('Real2IR',),
    2: ('OffsetX',),
    3: ('OffsetY',),
    4: ('PiPX1',),
    5: ('PiPX2',),
    6: ('PiPY1',),
    7: ('PiPY2',)
}
