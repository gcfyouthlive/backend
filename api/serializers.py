from rest_framework import serializers
from .models import User, UserProfile, Camper, Aylive, Events, Transaction, Reciept

# Users
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(required=True)

    class Meta:
        model = User
        fields = '__all__'
        read_only_fields= ['cash_onhand']
        extra_kwargs = {'password':{'write_only':True},'signup_date':{'read_only':True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.username = validated_data.pop('username')
        user.save()
        UserProfile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.save()
    
        profile.birthday = profile_data.get('birthday', profile.birthday)
        profile.contact = profile_data.get('contact', profile.contact)
        profile.school = profile_data.get('school', profile.school)
        profile.level = profile_data.get('level', profile.level)
        profile.year = profile_data.get('year', profile.level)
        profile.cash_onhand = profile_data('cash_onhand', profile.cash_onhand)
        #profile.address = profile_data.get('address', profile.address)
        #profile.city = profile_data.get('city', profile.city)
        profile.save()
        return instance

#Camp
class CamperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Camper
        fields = '__all__'
# Ask.YouthLIVE
class AyliveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aylive
        fields = ['question','timestamp']

# Events
class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ['id','url','eventname','datetime','attendees']

# Transaction System
class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id','url','user','trans_date','purpose','attendees']

class RecieptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reciept
        fields = ['transaction','acc_title','reci_establishment','reci_amt','reci_date','reci_or','img']