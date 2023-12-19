from django.shortcuts import render
from rest_framework.views import APIView
from .models import Member
from .api_serializer import MemberSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# Create your views here.

class MemberList(APIView):
    
    def get(self, request, format = None):
        membersList = Member.objects.all()
        memberSerializer = MemberSerializer(membersList, many = True)
        return Response(memberSerializer.data)
    
    def post(self, request, format = None):
        memberSerializer = MemberSerializer(data = request.data)
        if memberSerializer.is_valid():
            memberSerializer.save()
            return Response(memberSerializer.data, status = status.HTTP_201_CREATED)
        return Response(memberSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class MemberDetails(APIView):
    
    def get_object(self, pk):
        try:
            return Member.objects.get(pk = pk)
        except Member.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format = None):
        member = self.get_object(pk)
        memberSerializer = MemberSerializer(member)
        return Response(memberSerializer.data)
    
    '''
        Update
    '''
    def put(self, request, pk, format = None):
        member = self.get_object(pk)
        memberSerializer = MemberSerializer(member, data = request.data)
        if(memberSerializer.is_valid()):
            memberSerializer.save()
            return Response(memberSerializer.data)
        return Response(memberSerializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    '''
        Delete
    '''
    def delete(self, request, pk, format = None):
        member = self.get_object(pk)
        member.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)