import sys
import time
import datetime
from django.conf import settings
from django.shortcuts import render, HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import authenticate
from .encrypt import encrypt, decrypt
from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .models import Stud, Multi, Results, Todo
from .forms import MuForm, ResForm, StudForm, StartForm, TeachForm
from django.views.decorators.csrf import csrf_exempt
from .myClasses import Choices

t1 = time.time()


def LoginRequiredView(LoginRequiredMixin):
    return HttpResponseRedirect('/admin/login/?next=/admin/')


def findstudid(name, klass):
    stud1 = Stud.objects.filter(name=name, klass=klass.upper())
    stud2 = Stud.objects.filter(name=name, klass=klass.lower())
    if(stud1.count() == 1):
        stud = stud1
    else:
        stud = stud2
    if(stud.count() > 0):
        studid = stud[0].studid
        # print('Name: {}, Studid: {}\n'.format(name,studid))
        return studid
    else:
        return None


@login_required
def TeachView(request):
    mults = Multi.objects.all()
    studs = Stud.objects.all()
    todo = Todo.objects.all()
    # results = Results.objects.all()
    klist = []
    wlist = []
    # Find all klasser in order
    # Warning with lower upper cases!!
    for stud in studs:
        k = stud.klass
        try:
            klist.index(k)
        except ValueError:
            klist.append(k)
    klist.sort()  # List of all classes
    for test in mults:
        w = test.week
        try:
            wlist.index(w)
        except ValueError:
            wlist.append(w)
    wlist.sort()  # List of all weeks
    if (request.method == 'POST'):
        return HttpResponseRedirect('/mu/teacher/')
    elif (request.method == 'GET'):

        # Pass arguments klist and wlist for klasser and weeks choices
        form = TeachForm(request.GET, klist=klist, wlist=wlist)
        dicGet = request.GET
        try:
            klasser = dicGet['klasser']
            week = dicGet['weeks']
        except KeyError:
            klasser = klist[0]  # Values for first render
            week = wlist[0]
        elever = studs.filter(klass=klasser)
        tester = mults.filter(week=week)
        # Initialise with first student
        tmp = tester.filter(studid_id=elever[0].studid)
        # Get all other students with no copy
        for e in elever:
            tmp = tmp.union(tester.filter(studid_id=e.studid), all=False)
        # Order by studid, date and correct answers
        tester = tmp.all().order_by('studid_id', 'date', 'correct')
        # Collect all wrong answers
        todos = {}
        for test in tester:
            if test.errors > 0:
                td = todo.filter(testid_id=str(test.testid))
                todos[str(test.testid)] = td[0].todo

        context = {
            'form': form,
            'studs': studs,
            'tests': tester,
            'week': week,
            'klasser': klasser,
            'elever': elever,
            'todos': todos,
        }

        return render(request, 'teacher.html', context)


def StartView(request):
    if (request.method == 'POST'):
        startform = StartForm(request.POST)
        if (startform.is_valid()):
            name = startform.cleaned_data['name']
            password = startform.cleaned_data['password']

            # user = User.objects.get(username=name)
            spass = authenticate(username=name, password=password)

            if spass is None:
                # return ender(request, 'StartForm.html')
                # New stuff
                return HttpResponse('Username/password unvalid')
            else:
                context = {
                    'name': name,
                    'password': password
                }

                return HttpResponseRedirect('/mu/student/', context)

        else:
            return HttpResponse('Form unvalid {}'.format(startform))

    elif (request.method == 'GET'):
        form = StartForm()
        context = {
            'form': form,
        }
        return render(request, 'login.html', context)


# @csrf_exempt
def StudIn(request):
    fields = Stud.objects.all()

    if (request.method == 'POST'):
        studform = StudForm(request.POST)
        if (studform.is_valid()):

            name = studform.cleaned_data['name']
            klass = studform.cleaned_data['klass'].lower()
            studid = findstudid(name, klass)

            # Find the name in db and return the corresponing studid
            if(studid is None):
                return HttpResponse('Felt namn eller fel klass. Prova igen!')
            # studform.save()
        context = {
            'form': studform,
            'fields': fields
        }
        return render(request, 'login.html', context)


# @csrf_exempt
def StudIn(request):
    if (request.method == 'POST'):
        studform = StudForm(request.POST)
        if (studform.is_valid()):

            name = studform.cleaned_data['name']
            klass = studform.cleaned_data['klass'].lower()
            studid = findstudid(name, klass)

            # Find the name in db and return the corresponing studid
            if(studid is None):
                return HttpResponse('Felt namn eller fel klass. Prova igen!')
                # studform.save()

        context = {
            'form': studform,
        }
        return render(request, 'login.html', context)


# @csrf_exempt
def StudIn(request):

    if (request.method == 'POST'):
        studform = StudForm(request.POST)
        if (studform.is_valid()):

            name = studform.cleaned_data['name']
            klass = studform.cleaned_data['klass'].lower()
            studid = findstudid(name, klass)

            # Find the name in db and return the corresponing studid
            if(studid is None):
                return HttpResponse('Felt namn eller fel klass. Prova igen!')
                # studform.save()
        context = {
            'form': studform,
        }
        return render(request, 'login.html', context)


# @csrf_exempt
def StudIn(request):
    fields = Stud.objects.all()

    if (request.method == 'POST'):
        studform = StudForm(request.POST)
        if (studform.is_valid()):

            name = studform.cleaned_data['name']
            klass = studform.cleaned_data['klass'].lower()
            studid = findstudid(name, klass)

            # Find the name in db and return the corresponing studid
            if(studid is None):
                return HttpResponse('Felt namn eller fel klass. Prova igen!')
                # studform.save()

                return render(request, 'StudForm.html')
            else:
                context = {
                    'studid': studid,
                    'name': name
                }

                # start = datetime.datetime.now().strftime('%H:%M:%S')
                start = datetime.datetime.now().strftime("%H:%M:%S")
                response = HttpResponseRedirect('/mu/test/', context)
                response.set_cookie('studid', studid, max_age=600)
                response.set_cookie('start', start, max_age=600)
                return response
        else:
            return HttpResponse('Form unvalid {}'.format(studform))

    elif (request.method == 'GET'):
        form = StudForm()
        context = {
            'form': form,
        }
        return render(request, 'StudForm.html', context)


def MuTest(request):
    studid = request.COOKIES['studid']
    stud = Stud.objects.filter(studid=studid)
    name = stud[0].name
    klass = stud[0].klass
    date = datetime.datetime.now().strftime('20%y-%m-%d')
    start = request.COOKIES['start']
    start = datetime.datetime.strptime(start, "%H:%M:%S")
    week = int(datetime.datetime.now().isocalendar()[1])

    if (request.method == 'POST'):
        muform = MuForm(request.POST)
        if muform.is_valid():
            # We need year 1900 fr both start and end times
            end = datetime.datetime.now()
            end = end.strftime("%H:%M:%S")
            end = datetime.datetime.strptime(end, "%H:%M:%S")
            # print('start:',start)
            # print('end: ',end)
            seconds = (end-start).seconds
            # print(seconds)
            end = end.strftime("%H:%M:%S")
            start = start.strftime("%H:%M:%S")
            # end = end.strftime('%H:%M:%S')

            # t2 = time.time()
            # dt = t2 -t1
            # print('t1=',t1)
            # print('t2=',t2)

            minutes = int(seconds/60)
            seconds = int(seconds - minutes*60)
            tid = "{}:{}".format(minutes, seconds)
            test = Multi(studid_id=studid, date=date, start=start, end=end,
                         week=week, tid=tid)

            correct = 0
            errors = 0
            ers = []
            # Check answers and collect statistics
            for i in range(120):
                mu = Multi.test_120[i]
                muid = "{}: {}x{}".format(i+1, mu[0], mu[1])
                studres = muform.cleaned_data[muid]

                if(studres is not None):
                    # Check if answer is correct
                    if (int(studres) == int(mu[0])*int(mu[1])):
                        correct += 1
                        setattr(test, muid, studres)
                    else:
                        errors += 1
                        setattr(test, muid, '!{}'.format(studres))
                        ers.append("{}x{}≠{}".format(mu[0], mu[1], studres))
                else:
                    # errors +=1      # No answer = error
                    # setattr(test,muid,'?')
                    pass
            test.__dict__.update(correct=correct, errors=errors)
            test.save()

            # If somes save students errors in Todo tabel
            if len(ers) > 0:
                todo = Todo(testid_id=test.testid, studid_id=studid)
                todo.__dict__.update(todo=str(ers))
                todo.save()

            muform = MuForm()  # Clear form to avoid student back corrections
            # response.set_cookie('studid','')

            context = {
                'form': muform,
                'stud': stud,
                'name': name,
                'klass': klass,
                'minutes': minutes,
                'seconds': seconds,
                'correct': correct,
                'errors': errors,
                'ers': ers
            }
            # return HttpResponseRedirect('/mu/results/',context)
            return render(request, 'ResForm.html', context)
        else:
            return HttpResponse('Form unvalid!')
    elif (request.method == 'GET'):

        # Start timer
        # time.tzset()
        # tm = time.localtime()
        # timeT = time.strftime('%H:%M:%S',tm)
        # dateT = time.strftime('20%y-%m-%d',tm)
        # a = datetime.datetime.now().replace(microsecond=0)
        # Update start time of the student
        # t1 = time.time()
        # print('t1_view: ',t1)

        muform = MuForm()
        context = {
            'form': muform,
            'stud': stud,
            'name': name,
            'klass': klass,
            'studid': studid,
        }
        return render(request, 'MuForm.html', context)


def StudView(request):
    mus = Stud.objects.all()

    html = ''
    for mu in mus:
        var = f'<li> Name: {mu.name}, Date: {mu.date}, Time: {mu.time}</li><br>'
        html = html + var
    return HttpResponse(html, status=200)


def PopTodo(db):
    mults = Multi.objects.all()

    # Find all errors to work with and populate Todo tabell

    t120 = Multi.test_120

    for test in mults:
        i = 0
        todo = []
        if db:
            todoTab = Todo(studid_id=test.studid_id, testid_id=test.testid)
        for m in t120:
            i = i+1
            mult = '{}: {}x{}'.format(i, m[0], m[1])
            att = getattr(test, mult)

            if (att[:1] == '!'):
                r = '{}x{}={}'.format(m[0], m[1], att)
                todo.append(r)
                if db:
                    todoTab.__dict__.update(todo=str(todo))
                    todoTab.save()
    return todo
