from django.shortcuts import render
from openpyxl.reader.excel import load_workbook
from datetime import datetime
from django.contrib.auth.decorators import login_required
from .models import Application
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AppSerializer
from django.http import JsonResponse
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
# Create your views here.

now = datetime.now()
dt_string = now.strftime("%d%m%Y%H%M%S")
date = int(dt_string)

now = datetime.now()


def import_from_excel(request):
    if request.method == 'POST':
        excel_file = request.FILES.get('excel_file')
        if excel_file:
            wb = load_workbook(excel_file)
            ws = wb.active
            instances = []
            for row in ws.iter_rows(min_row=2, values_only=True):
                try:
                    credit_date = datetime.strptime(row[12], '%d.%m.%Y').date()
                    a = Application.objects.create(
                        mfo=row[0],
                        application_id=row[1],
                        client_type=row[2],
                        client_id=row[3],
                        client_name=row[4],
                        claim_id=row[5],
                        state=row[6],
                        credit_sum=row[7],
                        credit_percent=row[8],
                        region_code=row[9],
                        district_code=row[10],
                        branch_id=row[11],
                        credit_date=credit_date
                    )
                    instances.append(a)
                except Exception as e:
                    print(f"Error processing row {row}: {e}")
            if instances:
                messages.success(request, 'Objects successfully created')
            else:
                messages.warning(request, 'No valid objects created')
        else:
            messages.error(request, 'No file uploaded')
    return render(request, 'upload_file.html')


class ApplicationView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        request_id = request.query_params.get('request_id')
        application_id = request.query_params.get('application_id')
        if application_id:
            try:
                # application_obj = Application.objects.get(id=request_id, application_id=application_id)
                application_obj = Application.objects.get(application_id=application_id)
                serializer = AppSerializer(application_obj)
                return Response([serializer.data])
            except Application.DoesNotExist:
                return Response({'error': 'Object not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'Both request_id and application_id are required'},
                            status=status.HTTP_400_BAD_REQUEST)
