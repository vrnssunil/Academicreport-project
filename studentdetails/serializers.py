from rest_framework import serializers
from .models import StudentMarks,SubjectFaculty

class SubjectFacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectFaculty
        fields = ('subject', 'name')

class StudentMarksSerializer(serializers.ModelSerializer):
    #reporter = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = StudentMarks
        fields = ('studentname', 'subject', 'marks')

#serializers usd to convert the data from Json format
