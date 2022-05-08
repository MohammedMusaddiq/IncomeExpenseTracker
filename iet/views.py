from datetime import datetime

from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from xhtml2pdf import pisa

from accounts.models import User
from .forms import AddTransaction
from .models import Transactions, Category, ExpenseType


def Dashboard(request):
    categories_obj = Category.objects.select_related('expense_type')
    expense_obj = ExpenseType.objects.all()
    current_month = datetime.now().month
    fm = AddTransaction()
    if request.method == 'POST':
        fm = AddTransaction(request.POST)
        print(request.POST)
        if fm.is_valid():
            obj = fm.save(commit=False)
            obj.user = request.user
            obj.save()
            messages.success(request, 'added the transaction details successfully')
            return redirect('iet:dashboard')

    else:
        if 'q' in request.GET:
            q = request.GET['q']
            all_transactions_list = Transactions.objects.select_related('user', 'expense', 'category').filter(
                user=request.user).filter(
                Q(expense__name__icontains=q) | Q(category__category_name__icontains=q) | Q(note__icontains=q) | Q(
                    amount__icontains=q) | Q(closing_balance__icontains=q)
            ).order_by('-date_time')

        elif 'f' in request.GET:
            f = request.GET['f']
            all_transactions_list = Transactions.objects.select_related('user', 'expense', 'category').filter(
                user=request.user).filter(
                Q(expense__name__icontains=f) | Q(category__category_name__icontains=f)).order_by('-date_time')

        elif 'from-date' in request.GET:
            f_date = request.GET['from-date']
            t_date = request.GET['to-date']
            all_transactions_list = Transactions.objects.select_related('user', 'expense', 'category').filter(
                user=request.user).filter(created__range=[f_date, t_date]).order_by('-date_time')

        else:
            all_transactions_list = Transactions.objects.select_related('user', 'expense', 'category').filter(
                user=request.user, created__month=current_month).order_by('-date_time')
        paginator = Paginator(all_transactions_list, 10)
        page_number = request.GET.get('page', 1)
        all_transactions = paginator.get_page(page_number)
        pdf_data = []
        for i in all_transactions:
            data = {
                'date': str(i.created),
                'type': i.expense.name,
                'category': i.category.category_name,
                'amount': i.amount,
                'note': i.note,
                'closing_balance': i.closing_balance,
            }
            pdf_data.append(data)

        request.session['data'] = pdf_data

        context = {
            'all_transactions': all_transactions,
            'categories_obj': categories_obj,
            'expense_obj': expense_obj,
            'form': fm,
            'title': 'Income/Expense Tracker'
        }
        return render(request, 'iet/index.html', context)


def generate_pdf_view(request):
    current_date = datetime.now().today().date()
    template_path = 'iet/pdf.html'
    data_obj = request.session['data']
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f"filename=Transactions Statement-({request.user.name}-{current_date}).pdf"
    template = get_template(template_path)
    html = template.render({
        "data_obj": data_obj,
        'title': request.user,
        'date': current_date,
    })
    pisa_status = pisa.CreatePDF(
        html, dest=response, )

    if pisa_status.err:
        return HttpResponse(f'We had some errors <pre>{html}</pre>')
    return response


def send_mail(request):
    user_email = User.objects.get(email__iexact=request.user).email
    data = request.session['data']
    html_content = render_to_string('iet/email_template.html', {'title': 'Email Report', 'content': data})
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(
        "Income/Expense Report",
        text_content,
        settings.EMAIL_HOST_USER,
        ['musaddiq838@gmail.com'],
    )
    email.attach_alternative(html_content, 'text/html')
    email.send()
    messages.success(request, "Email Sent with Report, Please Check Yur Email")
    return redirect('iet:dashboard')


def ajax_query(request):
    if 'query' in request.GET:
        q = request.GET.get('query')
        cat_obj = list(Category.objects.filter(expense_type__id=q).values())
        return JsonResponse({'data': cat_obj})
