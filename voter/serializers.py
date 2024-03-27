import datetime
import re

from rest_framework import serializers
from .models import Voter

class VoterSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = Voter


    def validate_fname(self, new_fname):
        if re.search("^[A-Za-z]{2,100}$", new_fname) is None:
            raise serializers.ValidationError('Only alphabets allowed in First name between 2 and 100 characters')

        return new_fname


    def validate_lame(self, new_lname):
        if re.search("^[A-Za-z]{2,100}$", new_lname) is None:
            raise serializers.ValidationError('Only alphabets allowed in Last name between 2 and 100 characters')

        return new_lname

    def validate_dob(self,dob:str):

        now = datetime.datetime.now()

        if now.year - dob.year < 18:
            raise serializers.ValidationError("must be 18 or older")
        elif now.year - dob.year == 18:
            if now.month < dob.month:
                raise serializers.ValidationError("must be 18 or older")
            elif now.month == dob.month:
                if now.day < dob.day:
                    raise serializers.ValidationError("Must be 18 or older")

        return dob

    def validate_nin(self, nin):
        if re.search("^[0-9]{11}$", nin)is None:
         raise serializers.ValidationError("Invalid nin format")

        return nin

    def validate_phone_no(self, phone_no):
        if re.search("^[+-][0-9]{11,15}$", phone_no) is None:
            raise serializers.ValidationError("Invalid number format")

        return phone_no

    def validate_vote(self, vote):
        if re.search("(APC|PDP|LP)$", vote) is None:
            raise serializers.ValidationError("Party not recognized")

        return vote






