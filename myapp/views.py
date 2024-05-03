from django.shortcuts import render
from openpyxl.reader.excel import load_workbook
from datetime import datetime
from django.contrib.auth.decorators import login_required
from .models import Application, ClientInfo, CreditPay, CreditPayment
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AppSerializer, ClientInfoSerializer, CreditPaySerializer, CreditPaymentSerializer
from django.http import JsonResponse
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .forms import ApplicationSearchForm
from django.contrib import messages

# Create your views here.

now = datetime.now()
dt_string = now.strftime("%d-%m-%Y %H:%M:%S")
date = str(dt_string)


@login_required()
def import_from_excel(request):
    if request.method == 'POST':
        excel_file = request.FILES.get('excel_file')
        if excel_file.name.endswith('.xlsx'):
            wb = load_workbook(excel_file)
            ws = wb.active
            instances = []
            for row in ws.iter_rows(min_row=2, values_only=True):
                if not Application.objects.filter(loan_id=row[5]).exists():
                    try:
                        change_date = datetime.strptime(row[4], '%d.%m.%Y').date()
                        credit_date = datetime.strptime(row[12], '%d.%m.%Y').date()
                        credit_term_date = datetime.strptime(row[13], '%d.%m.%Y').date()
                        first_pay_date = datetime.strptime(row[18], '%d.%m.%Y').date()
                        last_pay_date = datetime.strptime(row[19], '%d.%m.%Y').date()

                        a = Application.objects.create(
                            # mfo=row[0],
                            # branch_id=row[1],
                            # application_id=row[2],
                            # state=row[3],
                            # change_date=change_date,
                            # claim_id=row[5],
                            # region_code=row[6],
                            # district_code=row[7],
                            # client_type=row[8],
                            # client_name=row[9],
                            # client_id=row[10],
                            # credit_num=row[11],
                            # credit_date=credit_date,
                            # credit_term_date=credit_term_date,
                            # credit_sum=row[14],
                            # credit_percent=row[15],
                            # credit_account=row[16],
                            # total_pay_sum=row[17],
                            # first_pay_date=first_pay_date,
                            # last_pay_date=last_pay_date,
                            # debt_sum=row[20],
                            # loan_id=row[21],
                            # credit_purpose_code=row[22],
                            # credit_purpose_name=row[23],
                            mfo=row[0],
                            branch_id=row[1],
                            application_id=row[2],
                            state=row[3],
                            change_date=change_date,
                            loan_id=row[5],
                            # claim_id=row[5],
                            region_code=row[6],
                            district_code=row[7],
                            client_type=row[8],
                            client_name=row[9],
                            client_id=row[10],
                            credit_num=row[11],
                            credit_date=credit_date,
                            credit_term_date=credit_term_date,
                            credit_sum=row[14],
                            credit_percent=row[15],
                            credit_account=row[16],
                            total_pay_sum=row[17],
                            first_pay_date=first_pay_date,
                            last_pay_date=last_pay_date,
                            debt_sum=row[20],
                            overdue_debt_sum=row[21],
                            credit_purpose_code=row[22],
                            credit_purpose_name=row[23],
                            account_16309_sum=row[24],
                            account_16323_sum=row[25],
                            account_16377_sum=row[26],
                            account_16379_sum=row[27],
                        )
                        instances.append(a)
                    except Exception as e:
                        print(f"Error processing row {row}: {e}")
                else:
                    messages.info(request, 'Your rows are not correspond to save it')
            if instances:
                messages.success(request, 'Your file successfully loaded')
            else:
                messages.info(request, 'Your rows are not correspond to save it')
        else:
            messages.warning(request, 'You must only excel file upload')
    return render(request, 'upload_file.html')


@login_required()
def credit_info_from_excel(request):
    if request.method == 'POST':
        excel_file = request.FILES.get('excel_file')
        if excel_file.name.endswith('.xlsx'):
            wb = load_workbook(excel_file)
            ws = wb.active
            instances = []
            for row in ws.iter_rows(min_row=2, values_only=True):
                if CreditPay.objects.filter(loan_id=row[0]).delete():
                    try:
                        a = CreditPay.objects.create(
                            loan_id=row[0],
                            nibbd_code=row[1],
                            mfo=row[2],
                            account=row[3],
                            branch_id=row[4],
                            account_status=row[5],
                            turnover_db_20208=row[6],
                            turnover_cr_20208=row[7],
                            turnover_cr_20218=row[8],
                            turnover_db_20218=row[9],
                            turnover_cr_22618=row[10],
                            turnover_db_22618=row[11],
                            turnover_db_20212=row[12],
                            turnover_cr_20212=row[13],
                            saldo_90963=row[14]
                        )
                        instances.append(a)
                    except Exception as e:
                        print(f"Error processing row {row}: {e}")
                else:
                    messages.info(request, 'Your rows are not correspond to save it')
            if instances:
                messages.success(request, 'Your file successfully loaded')
            else:
                messages.info(request, 'Your rows are not correspond to save it')
        else:
            messages.warning(request, 'You must only excel file upload')
    return render(request, 'upload_file.html')


@login_required()
def credit_payment_from_excel(request):
    if request.method == 'POST':
        excel_file = request.FILES.get('excel_file')
        if excel_file.name.endswith('.xlsx'):
            wb = load_workbook(excel_file)
            ws = wb.active
            instances = []
            for row in ws.iter_rows(min_row=2, values_only=True):
                if row:
                    try:
                        doc_date = datetime.strptime(row[10], '%d.%m.%Y')
                        credit_date = datetime.strptime(row[16], '%d.%m.%Y')

                        a = CreditPayment.objects.create(
                            branch_id=row[0],
                            cl_mfo=row[1],
                            cl_account=row[2],
                            cl_name=row[3],
                            cl_id=row[4],
                            ca_mfo=row[5],
                            ca_account=row[6],
                            ca_name=row[7],
                            ca_id=row[8],
                            doc_id=row[9],
                            doc_date=doc_date,
                            doc_num=row[11],
                            pay_sum=row[12],
                            pay_code=row[13],
                            pay_note=row[14],
                            pay_state=row[15],
                            pay_date=credit_date,
                            loan_id=row[18]
                        )
                        instances.append(a)
                    except Exception as e:
                        print(f"Error processing row {row}: {e}")
                else:
                    messages.info(request, 'Your rows are not correspond to save it')
            if instances:
                messages.success(request, 'Your file successfully loaded')
            else:
                messages.info(request, 'Your rows are not correspond to save it')
        else:
            messages.warning(request, 'You must only excel file upload')
    return render(request, 'upload_file.html')


class PaymentView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        request_id = request.query_params.get('request_id')
        loan_id = request.query_params.get('loan_id')
        brb = request.query_params.get('date')
        changed_date = datetime.strptime(brb, '%d.%m.%Y').strftime("%Y-%m-%d")
        if CreditPayment.objects.filter(loan_id=loan_id).exists():
            try:
                # ClientInfo.objects.create(request_id=request_id, application_id=application_id)
                application_obj = CreditPayment.objects.filter(loan_id=loan_id, pay_date=changed_date)
                serializer = CreditPaymentSerializer(application_obj, many=True)
                return Response(serializer.data)
            except CreditPayment.DoesNotExist:
                return Response({'error': 'Object not found'}, status=status.HTTP_404_NOT_FOUND)
        elif not CreditPayment.objects.filter(loan_id=loan_id).exists():
            return Response({'error': '00001',
                             'message': "loan_id or date not found",
                             'timestamp': date,
                             'status': 404})


class ApplicationView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        request_id = request.query_params.get('request_id')
        application_id = request.query_params.get('application_id')
        if Application.objects.filter(loan_id=application_id).exists():
            try:
                ClientInfo.objects.create(request_id=request_id, application_id=application_id)
                application_obj = Application.objects.filter(loan_id=application_id)
                serializer = AppSerializer(application_obj, many=True)
                return Response(serializer.data)
            except Application.DoesNotExist:
                return Response({'error': 'Object not found'}, status=status.HTTP_404_NOT_FOUND)
        elif not Application.objects.filter(loan_id=application_id).exists():
            return Response({'error': '00001',
                             'message': "application_id not found",
                             'timestamp': date,
                             'status': 404})


class CreditView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        request_id = request.query_params.get('request_id')
        nibbd_code = request.query_params.get('nibbd_code')
        if CreditPay.objects.filter(nibbd_code=nibbd_code).exists():
            try:
                # CreditPay.objects.create(request_id=request_id, application_id=application_id)
                application_obj = CreditPay.objects.filter(nibbd_code=nibbd_code)
                serializer = CreditPaySerializer(application_obj, many=True)
                return Response(serializer.data)
            except CreditPay.DoesNotExist:
                return Response({'error': 'Object not found'}, status=status.HTTP_404_NOT_FOUND)
        elif not CreditPay.objects.filter(nibbd_code=nibbd_code).exists():
            return Response({'error': '00001',
                             'message': "nibbd_code not found",
                             'timestamp': date,
                             'status': 404})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')

    return render(request, 'login.html')


@login_required()
def home(request):
    items_per_page = 20

    page = request.GET.get('page')

    queryset = Application.objects.all()
    search_form = ApplicationSearchForm(request.GET)

    if search_form.is_valid():
        loan_id = search_form.cleaned_data.get('loan_id')

        if loan_id:
            queryset = queryset.filter(loan_id__icontains=loan_id)

    paginator = Paginator(queryset, items_per_page)

    try:
        current_page = paginator.page(page)
    except PageNotAnInteger:
        current_page = paginator.page(1)
    except EmptyPage:
        current_page = paginator.page(paginator.num_pages)
    num_pages = paginator.num_pages
    current_page_number = current_page.number
    page_range = list(range(max(current_page_number - 2, 1), min(current_page_number + 3, num_pages + 1)))

    if page_range[0] > 2:
        page_range.insert(0, 1)
        page_range.insert(1, None)

    if page_range[-1] < num_pages - 1:
        page_range.append(None)
        page_range.append(num_pages)

    return render(request, 'home.html',
                  {'current_page': current_page, 'search_form': search_form, 'page_range': page_range})
