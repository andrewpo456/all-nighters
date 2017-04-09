from enum import Enum


class Sensors():
    """A grouping of similar sensor units."""

    def __init__(self, family, units):
        """Constructor."""
        self.family = family
        self.units = units


class LabUnit(Enum):
    """Available PCLab Login Unit Identifiers."""

    E1_04201 = 'E1-04201'
    E1_05204 = 'E1-05204'
    E1_05300 = 'E1-05300'
    E1_053L0 = 'E1-053L0'
    E1_053V0 = 'E1-053V0'
    E1_05402 = 'E1-05402'
    E1_06101 = 'E1-06101'
    E1_06102 = 'E1-06102'
    E1_06103 = 'E1-06103'
    E1_061V2 = 'E1-061V2'
    E1_07403 = 'E1-07403'
    E1_07404 = 'E1-07404'
    E1_07405 = 'E1-07405'
    E1_07406 = 'E1-07406'
    E1_08409 = 'E1-08409'
    E1_09405 = 'E1-09405'
    E1_10104 = 'E1-10104'
    E1_11300 = 'E1-11300'
    E1_11302 = 'E1-11302'
    E1_11403 = 'E1-11403'
    E1_B1100 = 'E1-B1100'
    E1_B1102 = 'E1-B1102'
    E1_B1103 = 'E1-B1103'
    E1_B11V2 = 'E1-B11V2'
    E1_B11V3 = 'E1-B11V3'
    E1_B1203 = 'E1-B1203'
    E1_B1204 = 'E1-B1204'
    E1_B1400 = 'E1-B1400'
    E1_B1401 = 'E1-B1401'
    E1_B1402 = 'E1-B1402'
    E1_B1403 = 'E1-B1403'
    E1_B14V0 = 'E1-B14V0'
    E1_B14V1 = 'E1-B14V1'
    E1_B14V2 = 'E1-B14V2'
    E1_B14V3 = 'E1-B14V3'


LAB_SENSORS = Sensors('logins',
                    [LabUnit.E1_04201, LabUnit.E1_05204, LabUnit.E1_05300,
                    LabUnit.E1_053L0, LabUnit.E1_053V0, LabUnit.E1_05402,
                    LabUnit.E1_06101, LabUnit.E1_06102, LabUnit.E1_06103,
                    LabUnit.E1_061V2, LabUnit.E1_07403, LabUnit.E1_07404,
                    LabUnit.E1_07405, LabUnit.E1_07406, LabUnit.E1_08409,
                    LabUnit.E1_09405, LabUnit.E1_10104, LabUnit.E1_11300,
                    LabUnit.E1_11302, LabUnit.E1_11403, LabUnit.E1_B1100,
                    LabUnit.E1_B1102, LabUnit.E1_B1103, LabUnit.E1_B11V2,
                    LabUnit.E1_B11V3, LabUnit.E1_B1203, LabUnit.E1_B1204,
                    LabUnit.E1_B1400, LabUnit.E1_B1401, LabUnit.E1_B1402,
                    LabUnit.E1_B1403, LabUnit.E1_B14V0, LabUnit.E1_B14V1, LabUnit.E1_B14V2, LabUnit.E1_B14V3])
