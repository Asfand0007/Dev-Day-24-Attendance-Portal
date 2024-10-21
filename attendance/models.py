from mongoengine import Document, StringField, BooleanField, ReferenceField,DateTimeField, IntField
from datetime import datetime

class DevDayAttendance(Document):
    consumerNumber = StringField(required=True)
    Team_Name = StringField(required=True)
    Leader_name = StringField(required=True)
    Leader_email = StringField(required=True)
    mem1_name = StringField(default="")
    mem1_email = StringField(default="")
    mem2_name = StringField(default="")
    mem2_email = StringField(default="")
    mem3_name = StringField(default="")
    mem3_email = StringField(default="")
    mem4_name = StringField(default="")
    mem4_email = StringField(default="")
    att_code = StringField(required=True)
    Competition = StringField(required=True)
    attendance = BooleanField(default=False)


class Event(Document):
    competitionName = StringField(required=True)
    start_time = DateTimeField(required=True)
    end_time = DateTimeField(required=True)
