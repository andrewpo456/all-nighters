import feit_building
from feit_building import retrieve
from feit_building import sensor
import academic_date
import datetime

startDate = academic_date.AUTUMN_START.date_str()
endDate = academic_date.AcademicDate(datetime.datetime.now()).date_str()

print("Calculating all nighters between: ")
print("(AUTUMN COMMENCMENT) " + startDate)
print("(NOW) " + endDate)

lab_data = []

for l in sensor.LabUnit:
    (rc, json) = retrieve.Data.retrieve(startDate, endDate, 'logins', l.value)
    if rc:
        lab_data.append(json)

lab_allnighters = []
for data_points in lab_data:
    # Filter the data for points that occur 'overnight'
    lab_allnighters.append(
        list(filter(lambda x:
        academic_date.AcademicDate.is_all_nighter(x[0], '%Y-%m-%d %H:%M:%S'),
        data_points)))

# Currently not an accurate indicator. Must look at last data point in all nighter period. If same -> Ignore, Else if data point > than last + 1
print(str.format("\n\n{0}/{1} labs contained students who pulled an allnighter", len(sensor.LabUnit), len(lab_allnighters)))
