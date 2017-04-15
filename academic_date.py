from datetime import datetime
from datetime import timedelta


class AcademicDate():
    """Used to minipulate dates within the UTS academic calendar."""

    def __init__(self, date, format='%Y-%m-%dT%I:%M:%S'):
        """Format -- The type of format to specify when converting to string."""
        self.date = date
        self.format = format

    def date_str(self, format='%Y-%m-%dT%I:%M:%S'):
        """Convert datetime object to string."""
        return self.date.strftime(format)

    def is_all_nighter(dateStr, parseFormat):
        """Determine if the date is out of hours (9pm - 6am the next day)."""
        date = datetime.strptime(dateStr, parseFormat)
        startDate = datetime(date.year, date.month, date.day, 21, 0, 0)
        endDate = datetime(date.year, date.month, date.day, 6, 0, 0) + timedelta(days=1)

        return (startDate < date < endDate)


AUTUMN_START = AcademicDate(datetime(datetime.now().year, 2, 20, 0, 0, 0))
ORIENTATION_END = AcademicDate(AUTUMN_START.date + timedelta(weeks=3))
FIRST_HALF_END = AcademicDate(ORIENTATION_END.date + timedelta(weeks=5))
MID_BREAK_END = AcademicDate(FIRST_HALF_END.date + timedelta(weeks=1))
SECOND_HALF_END = AcademicDate(MID_BREAK_END.date + timedelta(weeks=7))
ASSESSMENT_END = AcademicDate(SECOND_HALF_END.date + timedelta(weeks=3))
