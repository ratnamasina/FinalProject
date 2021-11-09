from django.shortcuts import render, redirect, get_object_or_404
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.views.decorators.csrf import requires_csrf_token
from django.contrib import messages
from django.http import HttpResponse
from device.models import user, phone_brand, phone_modell, phone_feature, phone_feature_v, tab_brand, tab_modell, \
    tab_feature, tab_feature_v, watch_brand, watch_modell, watch_feature, watch_feature_v
from django.conf import settings
from django.contrib.auth.decorators import login_required
import pymysql


@csrf_exempt
@requires_csrf_token
def home(request):
    return render(request, 'home.html')


def login(request):
    if request.method == 'POST':
        try:
            x = user.objects.get(email_id=request.POST.get('email_id'))
            y = user.objects.get(password=request.POST.get('password'))
            z = user.objects.filter(email_id=x)
            if x.id == y.id:
                return render(request, 'device.html')
            else:
                messages.error(request, 'username or password not correct')
                return redirect('login')
        except:
            messages.error(request, 'username or password not correct')
            return redirect('login')
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        fn = request.POST.get('first_name')
        ln = request.POST.get('last_name')
        e_id = request.POST.get('email_id')
        pas = request.POST.get('password')
        d = user(first_name=fn, last_name=ln, email_id=e_id, password=pas)
        d.save()
        messages.success(request, 'Registered user has been created successfully')

        return redirect('register')
    else:
        return render(request, 'register.html')


def device(request):
    return render(request, 'device.html')


def tabCompare(request):
    return render(request, 'tabCompare.html')


def watch(request):
    return render(request, 'watch.html')


def phoneCompare(request):
    return render(request, 'phoneCompare.html')


def ipad(request):
    if request.method == "GET":
        u = user.objects.all()
        pb = tab_brand.objects.all()
        pm1 = tab_modell.objects.filter(tab_brand_id=1)
        pm2 = tab_modell.objects.filter(tab_brand_id=1)
        ipd = {
            "u_p": u,
            "p_m1": pm1,
            "p_m2": pm2,
            "p_b": pb,
        }
        return render(request, 'ipad.html', ipd)
    elif request.method == "POST":
        return render(request, 'tabbuy.html')


def ipadoutput(request):
    if request.method == 'POST':
        data5 = request.POST.get('device5')
        data6 = request.POST.get('device6')
        u = user.objects.all()
        tb = tab_brand.objects.all()
        tm = tab_modell.objects.filter(tab_brand_id=1)
        tf = tab_feature.objects.filter(tab_brand_id=1)
        tfv1 = tab_feature_v.objects.filter(tab_model_id__tab_model_name__exact=data5)
        tfv2 = tab_feature_v.objects.filter(tab_model_id__tab_model_name__exact=data6)
        ito = {
            "u_p": u,
            "t_b": tb,
            "t_m": tm,
            "t_f": tf,
            "t_fv1": tfv1,
            "t_fv2": tfv2,
            "data5": data5,
            "data6": data6,
        }
        return render(request, 'ipadoutput.html', ito)
    elif request.method == "GET":
        return redirect('tabbuy.html', data5=request.POST['data5'], data6=request.POST['data6'])


def samsungTab(request):
    if request.method == "GET":
        u = user.objects.all()
        tb = tab_brand.objects.all()
        tm1 = tab_modell.objects.filter(tab_brand_id=2)
        tm2 = tab_modell.objects.filter(tab_brand_id=2)
        std = {
            "u_p": u,
            "t_m1": tm1,
            "t_m2": tm2,
            "t_b": tb,
        }
        return render(request, 'samsungTab.html', std)
    elif request.method == "POST":
        return render(request, 'tabbuy.html')


def samsungtaboutput(request):
    if request.method == 'POST':
        data7 = request.POST.get('device7')
        data8 = request.POST.get('device8')
        u = user.objects.all()
        tb = tab_brand.objects.all()
        tm = tab_modell.objects.filter(tab_brand_id=2)
        tf = tab_feature.objects.filter(tab_brand_id=1)
        tfv1 = tab_feature_v.objects.filter(tab_model_id__tab_model_name__exact=data7)
        tfv2 = tab_feature_v.objects.filter(tab_model_id__tab_model_name__exact=data8)
        sto = {
            "u_p": u,
            "t_b": tb,
            "t_m": tm,
            "t_f": tf,
            "t_fv1": tfv1,
            "t_fv2": tfv2,
            "data7": data7,
            "data8": data8,
        }
        return render(request, 'samsungtaboutput.html', sto)
    elif request.method == "GET":
        return redirect('tabbuy.html', data7=request.POST['data7'], data8=request.POST['data8'])


def iphone(request):
    if request.method == "GET":
        u = user.objects.all()
        pb = phone_brand.objects.all()
        pm1 = phone_modell.objects.filter(phone_brand_id=1)
        pm2 = phone_modell.objects.filter(phone_brand_id=1)
        ip = {
            "u_p": u,
            "p_m1": pm1,
            "p_m2": pm2,
            "p_b": pb,
        }
        return render(request, 'iphone.html', ip)
    elif request.method == "POST":
        return render(request, 'phonebuy.html')


def iphoneoutput(request):
    if request.method == 'POST':
        data1 = request.POST.get('device1')
        data2 = request.POST.get('device2')
        u = user.objects.all()
        pb = phone_brand.objects.all()
        pm = phone_modell.objects.filter(phone_brand_id=1)
        pf = phone_feature.objects.filter(phone_brand_id=1)
        pfv1 = phone_feature_v.objects.filter(phone_model_id__phone_model_name__exact=data1)
        pfv2 = phone_feature_v.objects.filter(phone_model_id__phone_model_name__exact=data2)
        ipo = {
            "u_p": u,
            "p_b": pb,
            "p_m": pm,
            "p_f": pf,
            "p_fv1": pfv1,
            "p_fv2": pfv2,
            "data1": data1,
            "data2": data2,
        }
        return render(request, 'iphoneoutput.html', ipo)
    elif request.method == "GET":
        return redirect('phonebuy.html', data1=request.POST['data1'], data2=request.POST['data2'])


def Samsung(request):
    if request.method == "GET":
        u = user.objects.all()
        pb = phone_brand.objects.all()
        pm1 = phone_modell.objects.filter(phone_brand_id=2)
        pm2 = phone_modell.objects.filter(phone_brand_id=2)
        sp = {
            "u_p": u,
            "p_m1": pm1,
            "p_m2": pm2,
            "p_b": pb,
        }
        return render(request, 'samsung.html', sp)
    elif request.method == "POST":
        return render(request, 'phonebuy.html')


def samsungoutput(request):
    if request.method == 'POST':
        data3 = request.POST.get('device3')
        data4 = request.POST.get('device4')
        u = user.objects.all()
        pb = phone_brand.objects.all()
        pm = phone_modell.objects.filter(phone_brand_id=2)
        pf = phone_feature.objects.filter(phone_brand_id=1)
        pfv1 = phone_feature_v.objects.filter(phone_model_id__phone_model_name__exact=data3)
        pfv2 = phone_feature_v.objects.filter(phone_model_id__phone_model_name__exact=data4)
        spo = {
            "u_p": u,
            "p_b": pb,
            "p_m": pm,
            "p_f": pf,
            "p_fv1": pfv1,
            "p_fv2": pfv2,
            "data3": data3,
            "data4": data4,
        }
        return render(request, 'samsungoutput.html', spo)
    elif request.method == "GET":
        return redirect('phonebuy.html', data3=request.POST['data3'], data4=request.POST['data4'])


def watchCompare(request):
    return render(request, 'watchCompare.html')


def applewatch(request):
    if request.method == "GET":
        u = user.objects.all()
        wb = watch_brand.objects.all()
        wm1 = watch_modell.objects.filter(watch_brand_id=1)
        wm2 = watch_modell.objects.filter(watch_brand_id=1)
        aw = {
            "u_p": u,
            "w_m1": wm1,
            "w_m2": wm2,
            "w_b": wb,
        }
        return render(request, 'applewatch.html', aw)
    elif request.method == "POST":
        return render(request, 'watchbuy.html')


def applewatchoutput(request):
    if request.method == 'POST':
        data9 = request.POST.get('device9')
        data10 = request.POST.get('device10')
        u = user.objects.all()
        wb = watch_brand.objects.all()
        wm = watch_modell.objects.filter(watch_brand_id=1)
        wf = watch_feature.objects.filter(watch_brand_id=1)
        wfv1 = watch_feature_v.objects.filter(watch_model_id__watch_model_name__exact=data9)
        wfv2 = watch_feature_v.objects.filter(watch_model_id__watch_model_name__exact=data10)
        awo = {
            "u_p": u,
            "w_b": wb,
            "w_m": wm,
            "w_f": wf,
            "w_fv1": wfv1,
            "w_fv2": wfv2,
            "data9": data9,
            "data10": data10,
        }
        return render(request, 'applewatchoutput.html', awo)
    elif request.method == "GET":
        return redirect('watchbuy.html', data9=request.POST['data9'], data10=request.POST['data10'])


def samsungwatch(request):
    if request.method == "GET":
        u = user.objects.all()
        wb = watch_brand.objects.all()
        wm1 = watch_modell.objects.filter(watch_brand_id=2)
        wm2 = watch_modell.objects.filter(watch_brand_id=2)
        sw = {
            "u_p": u,
            "w_m1": wm1,
            "w_m2": wm2,
            "w_b": wb,
        }
        return render(request, 'samsungwatch.html', sw)
    elif request.method == "POST":
        return render(request, 'watchbuy.html')


def samsungwatchoutput(request):
    if request.method == 'POST':
        data11 = request.POST.get('device11')
        data12 = request.POST.get('device12')
        u = user.objects.all()
        wb = watch_brand.objects.all()
        wm = watch_modell.objects.filter(watch_brand_id=2)
        wf = watch_feature.objects.filter(watch_brand_id=1)
        wfv1 = watch_feature_v.objects.filter(watch_model_id__watch_model_name__exact=data11)
        wfv2 = watch_feature_v.objects.filter(watch_model_id__watch_model_name__exact=data12)
        swo = {
            "u_p": u,
            "w_b": wb,
            "w_m": wm,
            "w_f": wf,
            "w_fv1": wfv1,
            "w_fv2": wfv2,
            "data11": data11,
            "data12": data12,
        }
        return render(request, 'samsungwatchoutput.html', swo)
    elif request.method == "GET":
        return redirect('watchbuy.html', data11=request.POST['data11'], data12=request.POST['data12'])


@csrf_protect
def phonebuy(request):
    if request.method == "POST":
        if 'buy1' in request.POST:
            data = request.POST.get('buy1')
            pmi1 = phone_modell.objects.filter(phone_model_name__exact=data)
            pf = phone_feature.objects.filter(phone_brand_id=1)
            pfv1 = phone_feature_v.objects.filter(phone_model_id__phone_model_name__exact=data)
            ipb1 = {
                "pmi1": pmi1,
                "data": data,
                "pfv1": pfv1,
                "pf": pf,
            }
            return render(request, 'phonebuy.html', ipb1)
        elif 'buy2' in request.POST:
            data = request.POST.get('buy2')
            pmi2 = phone_modell.objects.filter(phone_model_name__exact=data)
            pf = phone_feature.objects.filter(phone_brand_id=1)
            pfv2 = phone_feature_v.objects.filter(phone_model_id__phone_model_name__exact=data)
            ipb2 = {
                "pmi2": pmi2,
                "data": data,
                "pfv2": pfv2,
                "pf": pf,

            }
            return render(request, 'phonebuy.html', ipb2)
    elif request.method == "GET":
        if 'buy1' in request.GET:
            return render(request, "phonePayment.html")


def tabbuy(request):
    if request.method == "POST":
        if 'buy1' in request.POST:
            data = request.POST.get('buy1')
            tmi1 = tab_modell.objects.filter(tab_model_name__exact=data)
            tf = tab_feature.objects.filter(tab_brand_id=1)
            tfv1 = tab_feature_v.objects.filter(tab_model_id__tab_model_name__exact=data)
            itb1 = {
                "tmi1": tmi1,
                "data": data,
                "tfv1": tfv1,
                "tf": tf,
            }
            return render(request, 'tabbuy.html', itb1)
        elif 'buy2' in request.POST:
            data = request.POST.get('buy2')
            tmi2 = tab_modell.objects.filter(tab_model_name__exact=data)
            tf = tab_feature.objects.filter(tab_brand_id=1)
            tfv2 = tab_feature_v.objects.filter(tab_model_id__tab_model_name__exact=data)
            itb2 = {
                "tmi2": tmi2,
                "data": data,
                "tfv2": tfv2,
                "tf": tf,

            }
            return render(request, 'tabbuy.html', itb2)
    elif request.method == "GET":
        if 'buy1' in request.GET:
            return render(request, "phonePayment.html")


def watchbuy(request):
    if request.method == "POST":
        if 'buy1' in request.POST:
            data = request.POST.get('buy1')
            wmi1 = watch_modell.objects.filter(watch_model_name__exact=data)
            wf = watch_feature.objects.filter(watch_brand_id=1)
            wfv1 = watch_feature_v.objects.filter(watch_model_id__watch_model_name__exact=data)
            iwb1 = {
                "wmi1": wmi1,
                "data": data,
                "wfv1": wfv1,
                "wf": wf,
            }
            return render(request, 'watchbuy.html', iwb1)
        elif 'buy2' in request.POST:
            data = request.POST.get('buy2')
            wmi2 = watch_modell.objects.filter(watch_model_name__exact=data)
            wf = watch_feature.objects.filter(watch_brand_id=1)
            wfv2 = watch_feature_v.objects.filter(watch_model_id__watch_model_name__exact=data)
            iwb2 = {
                "wmi2": wmi2,
                "data": data,
                "wfv2": wfv2,
                "wf": wf,

            }
            return render(request, 'watchbuy.html', iwb2)
    elif request.method == "GET":
        if 'buy1' in request.GET:
            return render(request, "phonePayment.html")


def phonePayment(request):
    if request.method == "POST":
        data = request.GET.get("buy3")
        pm = phone_modell.objects.filter(phone_model_name__exact=data)
        pf = phone_feature.objects.filter(phone_brand_id__phone_modell__phone_model_name__exact=data,
                                          phone_feature_name__exact="Price")
        pfv = phone_feature_v.objects.filter(phone_brand_id__phone_modell__phone_model_name__exact=data,
                                             phone_feature_id=11)
        ap = {
            'p_m': pm,
            'p_f': pf,
            'p_fv': pfv,
        }
        return render(request, 'phonePayment.html', ap)


def shipment(request):

    return render(request, 'shipment.html')


def thankyou(request):

    return render(request, 'thankyou.html')
