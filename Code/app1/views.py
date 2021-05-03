from django.shortcuts import render, redirect
from .models import Profile
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io

# Create your views here.


def input_form(request):

    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        aboutMe = request.POST.get("aboutMe", "")
        address = request.POST.get("address", "")
        github_link = request.POST.get("github_link", "")
        linkedIn_link = request.POST.get("linkedIn_link", "")
        college = request.POST.get("college", "")
        degree_college = request.POST.get("degree_college", "")
        cgpa_college = request.POST.get("cgpa_college", "")
        time_college = request.POST.get("time_college", "")
        class12 = request.POST.get("class12", "")
        score_12th = request.POST.get("score_12th", "")
        stream_12th = request.POST.get("stream_12th", "")
        time_class12 = request.POST.get("time_class12", "")
        prev_work_company = request.POST.get("prev_work_company", "")
        prev_work_role = request.POST.get("prev_work_role", "")
        prev_work_location = request.POST.get("prev_work_location", "")
        prev_work_description = request.POST.get("prev_work_description", "")
        proj_title = request.POST.get("proj_title", "")
        proj_description = request.POST.get("proj_description", "")
        languages = request.POST.get("languages", "")
        tools_and_framework = request.POST.get("tools_and_framework", "")

        profile = Profile(name=name, email=email, phone=phone, aboutMe=aboutMe, address=address,
                          github_link=github_link, linkedIn_link=linkedIn_link, college=college, degree_college=degree_college,
                          cgpa_college=cgpa_college, time_college=time_college, class12=class12, score_12th=score_12th, stream_12th=stream_12th,
                          time_class12=time_class12,
                          prev_work_company=prev_work_company, prev_work_role=prev_work_role,
                          prev_work_location=prev_work_location, prev_work_description=prev_work_description,
                          proj_title=proj_title, proj_description=proj_description, languages=languages, tools_and_framework=tools_and_framework
                          )
        profile.save()
    return render(request, 'app1/input_form.htm')


def check(request, id):
    user_p = Profile.objects.get(pk=id)

    template = loader.get_template('app1/check.html')
    html = template.render({"user_p": user_p})
    options = {
        'page-size': 'Letter',
        'encoding': "UTF-8"
    }

    pdf = pdfkit.from_string(html, False, options)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment'
    filename = "resume.pdf"
    return response


"""
    return render(request, 'app1/check.html', {"user_p":user_p})
    """
