import random
from django.contrib import messages
from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate,login,logout as auth_logout
from django.contrib.auth.hashers import check_password, make_password
from django.core.mail import send_mail
from django.conf import settings
from datetime import date
# Create your views here.
def homefn(request):
    return render(request,'home.html')
def chome(request):
    return render(request,'coach_home.html')
def login(request):
    cp=Mycaptcha(request.POST)
    if(request.method=='POST'):
        email=request.POST['email']
        pwd=request.POST['pwd']
        if(email=='honey@gmail.com'):
            if(pwd=='honey123'):
                if(cp.is_valid()):
                    return redirect(ohome)
                else:
                    err='invalid captcha code!!!'
                    ctx={'error':err,'cpt':cp}
                    return render(request,'login.html',context=ctx)
            else:
                err='invalid password'
                ctx={'error':err,'cpt':cp}
                return render(request,'login.html',context=ctx)
        else:
            err = 'invalid emailId'
            ctx = {'error': err, 'cpt': cp}
            return render(request, 'login.html', context=ctx)
    else:
        return render(request,'login.html',{'cpt':cp})

def clogin(request):
    cp = Mycaptcha(request.POST)
    if(request.method=='POST'):
        unm=request.POST['uname']
        pwd=request.POST['pwd']
        try:
            c1=coach.objects.get(username=unm)
            if(c1.password==pwd):
                if (cp.is_valid()):
                    return redirect(chome)
                else:
                    err = 'invalid captcha code!!!'
                    ctx = {'error': err, 'cpt': cp}
                    return render(request, 'coach_login.html', context=ctx)
            else:
                err='Invalid Password'
                ctx = {'error': err, 'cpt': cp}
                return render(request,'coach_login.html',context=ctx)
        except:
            err='Username not found'
            ctx = {'error': err, 'cpt': cp}
            return render(request,'coach_login.html',context=ctx)
    else:
        return render(request,'coach_login.html',{'cpt':cp})

def forgotpwd(request):
    if(request.method=='POST'):
        ema=request.POST.get('email')
        request.session['email']=ema

        otp = f'{random.randint(0, 999999):06}'
        # f1=coach.objects.filter(email=ema).count()

        if coach.objects.filter(email=ema).exists():
            request.session['otp1'] = otp
            subject='OTP for Reset Password'
            message=f'your otp for password reset is:{otp}'
            from_email=settings.EMAIL_HOST_USER
            recipient_EMAIL=[ema]
            send_mail(subject,message,from_email,recipient_EMAIL)
            return redirect(otpverify)
        else:
            err='email not found'
            return render(request,'forgot_password.html',{'error':err})
    else:
        return render(request,'forgot_password.html')

def otpverify(request):
    if(request.method=='POST'):
        cotp=request.POST.get('otp')
        npwd=request.POST.get('npwd')
        cpwd=request.POST.get('cpwd')
        otp2=request.session.get('otp1')
        if cotp==otp2:
            if(npwd==cpwd):
                ema=request.session.get('email')
                try:
                    user=coach.objects.get(email=ema)
                    user.password=npwd
                    user.save()
                    return redirect(clogin)
                except coach.DoesNotExist:
                        err = 'User not found'
                        return render(request, 'otp_verify.html', {'error': err})
            else:
                err='both password must be same'
                return render(request,'otp_verify.html',context={'error':err})
        else:
            err = 'otp does not match'
            return render(request,'otp_verify.html',context={'error':err})
    else:
        return render(request,'otp_verify.html')

def logout(request):
    auth_logout(request)
    return redirect(homefn)

def coachlogout(request):
    auth_logout(request)
    return redirect(clogin)
def ohome(request):
    today=date.today()
    future_date = date(today.year, 12, 31)

    s1=schedule1.objects.filter(startdate=today)
    s2=schedule1.objects.filter(startdate=future_date)
    return render(request,'owner_home.html',context={'s1':s1,'s2':s2})
def coainfo(request):
    if(request.method=='POST'):
        cname=request.POST['cname']
        bdate=request.POST['bdate']
        gen=request.POST['gen']
        email = request.POST['email']
        add=request.POST['add']
        mob=request.POST['mob']
        expr=request.POST['expr']
        jdate=request.POST['jdate']
        edate=request.POST['edate']
        uname=request.POST['uname']
        pwd=request.POST['pwd']
        photo=request.FILES['photo']
        c1=coach(coachname=cname,birthdate=bdate,gender=gen,email=email,address=add,mobilenumber=mob,experience=expr,joindate=jdate,enddate=edate,username=uname,password=pwd,photo=photo)
        c1.save()
        return redirect(displaycoach)
    else:
        return render(request,'Addcoach_info.html')

def displaycoach(request):
    c1=coach.objects.all()
    return render(request,'display_coach.html',context={'c1':c1})

def vicoach(request,id):
    co=coach.objects.get(c_id=id)
    return render(request,'view_coach.html',{'co':co})
def coachinfo(request):
    coa=coach.objects.all()
    return render(request,'coach_info.html',{'coa':coa})

def editcoach(request,id):
    c=coach.objects.get(c_id=id)
    if(request.method=='POST'):
        cnm=request.POST['cname']
        bdate=request.POST['bdate']
        gen=request.POST['gen']
        email=request.POST['email']
        add=request.POST['add']
        mob=request.POST['mob']
        exp=request.POST['expr']
        jdate=request.POST['jdate']
        edate=request.POST['edate']
        unm=request.POST['uname']
        pwd=request.POST['pwd']
        photo=request.FILES['photo']
        c.coachname=cnm
        c.birthdate=bdate
        c.gender=gen
        c.email=email
        c.address=add
        c.mobilenumber=mob
        c.experience=exp
        c.joindate=jdate
        c.enddate=edate
        c.username=unm
        c.password=pwd
        c.photo=photo
        c.save()
        return redirect(displaycoach)
    else:
        return render(request,'Edit_coach.html',{'coach':c})

def delete(request,id):
    c1=coach.objects.get(c_id=id)
    c1.delete()
    return redirect(displaycoach)
def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        msg=request.POST['message']
        send_mail('Basketball Academy',
                  f'My Name is: {name},\n'
                    f'From Email is: {email}\n'
                    f'Massage Has form Submited: {msg}',
                    settings.EMAIL_HOST_USER,['honeypatelhp32@gmail.com',])
        return redirect(chome)
    else:
     return render(request,'coach_home.html')

def player(request):
    if request.method=='POST':
        pname=request.POST['pnm']
        add=request.POST['add']
        email=request.POST['email']
        mob=request.POST['mob']
        dob=request.POST['bdate']
        gen=request.POST['gen']
        het=request.POST['het']
        wet=request.POST['wet']
        pos=request.POST['pos']
        jdt=request.POST['jdt']
        edt=request.POST['edt']
        uname=request.POST['unm']
        pwd=request.POST['pwd']
        photo=request.FILES['pht']
        p1=player1(playername=pname,address=add,email=email,mobileno=mob,birthdate=dob,gender=gen,height=het,weight=wet,position=pos,joindate=jdt,enddate=edt,username=uname,password=pwd,photo=photo)
        p1.save()
        return redirect(displayplayer)
    else:
        return render(request,'Player_info.html')
def displayplayer(request):
    p1=player1.objects.all()
    return render(request,'display_player.html',{'p1':p1})
def viewplayer(request,id):
    pid=player1.objects.get(p_id=id)
    return render(request,'view_player.html',context={'pid':pid})
def editplayer(request,id):
    p1=player1.objects.get(p_id=id)
    if(request.method=='POST'):
        pname=request.POST['pnm']
        add=request.POST['add']
        em=request.POST['email']
        mob=request.POST['mob']
        bdate=request.POST['bdate']
        gen=request.POST['gen']
        het=request.POST['het']
        wet=request.POST['wet']
        pos=request.POST['pos']
        jdt=request.POST['jdt']
        edt=request.POST['edt']
        uname=request.POST['unm']
        pwd=request.POST['pwd']
        pht=request.FILES['pht']
        p1.playername=pname
        p1.address=add
        p1.email=em
        p1.mobileno=mob
        p1.birthdate=bdate
        p1.gender=gen
        p1.height=het
        p1.weight=wet
        p1.position=pos
        p1.joindate=jdt
        p1.enddate=edt
        p1.username=uname
        p1.password=pwd
        p1.photo=pht
        p1.save()
        return redirect(displayplayer)
    else:
        return render(request,'Edit_player.html',context={'ply':p1})
def deleteplayer(request,id):
    p1=player1.objects.get(p_id=id)
    p1.delete()
    return redirect(displayplayer)

def team(request):
    if(request.method=='POST'):
        tname=request.POST['tname']
        sch=request.POST['sch']
        cid=request.POST['cnm']
        cname=coach.objects.get(c_id=cid)
        t1=Team(teamname=tname,schedule=sch,coach_name=cname)
        t1.save()
        return redirect(displayteam)
    else:
        c1=coach.objects.all()
        ctx={'c1':c1}
        return render(request,'Team.html',context=ctx)

def displayteam(request):
    t1=Team.objects.all()
    return render(request,'display_team.html',context={'t1':t1})

def editteam(request,id):
    t1=Team.objects.get(t_id=id)
    if(request.method=='POST'):
        tnm=request.POST['tname']
        sch=request.POST['sch']
        cid=request.POST['cnm']
        cname=coach.objects.get(c_id=cid)
        t1.teamname=tnm
        t1.schedule=sch
        t1.coach_name=cname
        t1.save()
        return redirect(displayteam)
    else:
        c1=coach.objects.all()
        return render(request,'Edit_team.html',context={'team':t1,'c1':c1})

def deleteteam(request,id):
    t1=Team.objects.get(t_id=id)
    t1.delete()
    return redirect(displayteam)

def assigntm(request):
    if(request.method=='POST'):
        cid=request.POST['cname']
        tid=request.POST['tname']
        pid=request.POST['pname']
        cname=coach.objects.get(c_id=cid)
        tname=Team.objects.get(t_id=tid)
        pname=player1.objects.get(p_id=pid)
        a1=assign_tb(coa_id=cname,tea_id=tname,ply_id=pname)
        a1.save()
        return redirect(disassigntm)
    else:
        c1=coach.objects.all()
        t1=Team.objects.all()
        p1=player1.objects.all()
        return render(request,'Assign_team.html',context={'c1':c1,'t1':t1,'p1':p1})

def editassign(request,id):
    a1=assign_tb.objects.get(a_id=id)
    if(request.method=='POST'):
        cid=request.POST['cname']
        tid=request.POST['tname']
        pid=request.POST['pname']
        cname=coach.objects.get(c_id=cid)
        tname=Team.objects.get(t_id=tid)
        pname=player1.objects.get(p_id=pid)
        a1.coa_id=cname
        a1.tea_id=tname
        a1.ply_id=pname
        a1.save()
        return redirect(disassigntm)
    else:
        c1=coach.objects.all()
        t1=Team.objects.all()
        p1=player1.objects.all()
        ctx={'c1': c1, 't1': t1, 'p1': p1,'assign':a1}
        return render(request,'Edit_assigntm.html',context=ctx)
def delete_assigntm(request,id):
    a1=assign_tb.objects.get(a_id=id)
    a1.delete()
    return redirect(disassigntm)

def disassigntm(request):
    a1=assign_tb.objects.all()
    return render(request,'display_assigntm.html',{'a1':a1})
def viewteam(request):
    if(request.method=='POST'):
        tnm=request.POST['tname']
        a1=assign_tb.objects.filter(tea_id=tnm)
        tname=Team.objects.get(t_id=tnm)
        return render(request,'view_team_player.html',context={'a1':a1,'tname':tname})
    else:
        t1=Team.objects.all()
        return render(request,'View_Team.html',context={'t1':t1})

def viewteamply(request):
    return render(request,'view_team_player.html')

def tmreport(request):
    t1=Team.objects.all()
    return render(request,'Team_Report.html',context={'t1':t1})
def playreport(request):
    a1=assign_tb.objects.all()
    return render(request,'player_report.html',context={'a1':a1})
def schedulereport(request):
    s1=schedule1.objects.all()
    return render(request,'schedule_report.html',context={'s1':s1})
def matchreport(request):
    s1=schedule1.objects.all()
    return render(request,'man_match_report.html',context={'s1':s1})
def winlossreport(request):
    s1=schedule1.objects.all()
    return render(request,'winloss_report.html',context={'s1':s1})

def schedule(request):
    if(request.method=='POST'):
        cid=request.POST['cnm']
        tid=request.POST['tnm']
        sdsc=request.POST['sdsc']
        add=request.POST['add']
        sdate=request.POST['sdt']
        edate=request.POST['edt']
        stime=request.POST['stime']
        etime=request.POST['etime']
        rol=request.POST['rol']
        match=request.POST['match']
        cname=coach.objects.get(c_id=cid)
        tname=Team.objects.get(t_id=tid)
        s1=schedule1(coa_id=cname,tm_id=tname,description=sdsc,Address=add,startdate=sdate,enddate=edate,starttime=stime,endtime=etime,role=rol,man_of_match=match)
        s1.save()
        return redirect(displayschedule)
    else:
        c1=coach.objects.all()
        t1=Team.objects.all()
        return render(request,'schedule.html',context={'c1':c1,'t1':t1})

def editschedule(request,id):
    s1=schedule1.objects.get(id=id)
    if(request.method=='POST'):
        cid=request.POST['cnm']
        tid=request.POST['tnm']
        sdsc=request.POST['sdsc']
        add=request.POST['add']
        sdate=request.POST['sdt']
        edate=request.POST['edt']
        stime=request.POST['stime']
        etime=request.POST['etime']
        role=request.POST['rol']
        match=request.POST['match']
        cname=coach.objects.get(c_id=cid)
        tname=Team.objects.get(t_id=tid)

        s1.coa_id=cname
        s1.tm_id=tname
        s1.description=sdsc
        s1.Address=add
        s1.startdate=sdate
        s1.enddate=edate
        s1.stime=stime
        s1.endtime=etime
        s1.role=role
        s1.man_of_match=match
        s1.save()
        return redirect(displayschedule)
    else:
        c1=coach.objects.all()
        t1=Team.objects.all()
        return render(request,'Edit_schedule.html',context={'s1':s1,'c1':c1,'t1':t1})

def displayschedule(request):
    s1=schedule1.objects.all()
    return render(request,'display_schedule.html',context={'s1':s1})
def deleteschedule(request,id):
    s1=schedule1.objects.get(id=id)
    s1.delete()
    return redirect(displayschedule)

def playerlogin(request):
    if request.method=='POST':
        unm=request.POST['uname']
        pwd=request.POST['pwd']
        try:
            p1=player1.objects.get(username=unm)
            if(p1.password==pwd):
                return redirect(plyhome)
            else:
                err='Invalid Password'
                return render(request,'player_login.html',context={'error':err})
        except:
            err='username not found'
            return render(request,'player_login.html',context={'error':err})
    else:
        return render(request,'player_login.html')

def plyhome(request):
    t1=Team.objects.all()
    ctx={'t1':t1}
    return render(request,'player_home.html',context=ctx)

def contactply(request):
    if request.method=='POST':
        name=request.POST['name']
        eml=request.POST['email']
        msg=request.POST['msg']
        send_mail('Basketball Academy',
                  f'My Name Is: {name}\n'
                  f'Email Is: {eml}\n'
                  f'your form has been submited: {msg}',
                  settings.EMAIL_HOST_USER,['honeypatelhp32@gmail.com',])
        return redirect(plyhome)
    else:
        return render(request,'player_home.html')

def plylogout(request):
    auth_logout(request)
    return redirect(homefn)

def plyschedule(request,id):
    t1=Team.objects.get(t_id=id)
    a1=assign_tb.objects.filter(tea_id=t1)
    s1=schedule1.objects.filter(tm_id=t1)
    return render(request,'Players_schedule.html',context={'a1':a1,'t1':t1,'s1':s1})
def plyforgotpwd(request):
    if (request.method == 'POST'):
        ema = request.POST.get('email')
        request.session['email'] = ema

        otp = f'{random.randint(0, 999999):06}'
        # f1=coach.objects.filter(email=ema).count()

        if player1.objects.filter(email=ema).exists():
            request.session['otp1'] = otp
            subject = 'OTP for Reset Password'
            message = f'your otp for password reset is:{otp}'
            from_email = settings.EMAIL_HOST_USER
            recipient_EMAIL = [ema]
            send_mail(subject, message, from_email, recipient_EMAIL)
            return redirect(otpverify1)
        else:
            err = 'email not found'
            return render(request, 'ply_forgotpwd.html', {'error': err})
    else:
        return render(request, 'ply_forgotpwd.html')


def otpverify1(request):
    if (request.method == 'POST'):
        cotp = request.POST.get('otp')
        npwd = request.POST.get('npwd')
        cpwd = request.POST.get('cpwd')
        otp2 = request.session.get('otp1')
        if cotp == otp2:
            if (npwd == cpwd):
                ema = request.session.get('email')
                try:
                    user = player1.objects.get(email=ema)
                    user.password = npwd
                    user.save()
                    return redirect(clogin)
                except player1.DoesNotExist:
                    err = 'User not found'
                    return render(request, 'otpverify.html', {'error': err})
            else:
                err = 'both password must be same'
                return render(request, 'otpverify.html', context={'error': err})
        else:
            err = 'otp does not match'
            return render(request, 'otpverify.html', context={'error': err})
    else:
        return render(request, 'otpverify.html')

def allplayer(request):
    p1=player1.objects.all()
    return render(request,'display_Allplayer.html',context={'p1':p1})