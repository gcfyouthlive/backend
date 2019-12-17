from rest_framework import serializers
from .models import User, UserProfile, Aylive, Events, Transaction, Reciept

# Users
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('birthday','school','level','address','city')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = UserProfileSerializer(required=True)

    class Meta:
        model = User
        fields = ('username','url','id','email','firstname','lastname','password','signup_date','profile')
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
        profile.school = profile_data.get('school', profile.school)
        profile.level = profile_data.get('level', profile.level)
        profile.address = profile_data.get('address', profile.address)
        profile.city = profile_data.get('city', profile.city)
        profile.save()
        return instance

# Ask.YouthLIVE
class AyliveSerializer(serializers.HyperlinkedModelSerializer):
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