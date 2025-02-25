from rest_framework.views import APIView
from django.http import JsonResponse
from django.shortcuts import render

class StaticAPIView(APIView):

    def get(self, request):
        # player = {
        #     'name':'Virat kohli',
        #     'ipl_team': 'RCB',
        #     'national_team':'India',
        #     'centureis': 82,
        #     'odi': 52,
        #     'test': 29,
        #     't20': 1
        # }
        print('Yashvin')
        return JsonResponse({'name':'Yashvin'})

class PlayerAPIView(APIView):
     def get(self, request):
        player = {
            'name':'Virat kohli',
            'ipl_team': 'RCB',
            'national_team':'India',
            'centureis': 82,
            'odi': 52,
            'test': 29,
            't20': 1
        }
 
        return JsonResponse(player)