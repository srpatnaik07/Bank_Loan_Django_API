from rest_framework import serializers
from . models import Approvals

class approvalsSerializers(serializers.ModelSerializer):
	class Meta:
		model=Approvals
		fields='__all__'

        # fields = (
        #     'firstname',
        #     'lastname',
        #     'dependants',
        #     'applicantincome',
        #     'coapplicatincome',
        #     'loanamt',
        #     'loanterm',
        #     'credithistory',
        #     'gender',
        #     'married',
        #     'graduatededucation',
        #     'selfemployed',
        #     'area',
        # )
