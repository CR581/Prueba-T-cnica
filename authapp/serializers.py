from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

User = get_user_model()

class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'cc', 'name', 'age', 'gender', 'phone']

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            cc=validated_data['cc'],
            name=validated_data['name'],
            age=validated_data['age'],
            gender=validated_data['gender'],
            phone=validated_data['phone']
        )
        user.set_password(validated_data['cc']) 
        user.save()
        return user

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    cc = serializers.CharField()  

    def validate(self, data):
        user = authenticate(email=data['email'], password=data['cc'])  
        if user is None:
            raise serializers.ValidationError('Correo o Número de documento incorrecto')
        return data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'cc', 'name', 'age', 'gender', 'phone']  