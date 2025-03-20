from django.http import JsonResponse    #return the data as json
from django.views.decorators.csrf import csrf_exempt # crsf means cross-site request forgery
from django.shortcuts import get_object_or_404
import json   #send to the json format
from .models import*
 
@csrf_exempt #disable csrf production
def studentdetails(request):
    if request.method == "POST":  # check the  methods
        # Create a new student detail table
        data = json.loads(request.body)  # converts jsons string into a python dictorinary
        student = StudentDetails.objects.create(
            name=data['name'],
            rollnumber=data['rollnumber'],
            standard=data['standard'],
            dateofbirth=data['dateofbirth'],
            gender=data['gender']
            
            
        )
        return JsonResponse({
            "id": student.id,
            "name": student.name,
            "rollnumber": student.rollnumber,
            "standard": student.standard,
            "dateofbirth":student.dateofbirth,
            "gender":student.gender
        }, status=201) # status =201 indicates create sucessfully

    elif request.method == "GET":
        # Retrieve all students
        students = StudentDetails.objects.all()
        studentlist = [
            {
                "id": student.id,
                "name": student.name,
                "rollnumber": student.rollnumber,
                "standard": student.standard
            } for student in students
        ]
        return JsonResponse({"students": studentlist})
    elif request.method == "PUT":
        # Update an  student by ID
        data = json.loads(request.body)
        student = get_object_or_404(StudentDetails, id=data['id'])  # Fetch the student to update
        student.name = data['name']
        student.rollnumber = data['rollnumber']
        student.standard = data['standard']
        student.dateofbirth=data['dateofbirth']
        student.gender=data['gender']
        student.save()  # Save changes to the database

        return JsonResponse({
            "id": student.id,
            "name": student.name,
            "rollnumber": student.rollnumber,
            "standard": student.standard,
            "dateofbirth":student.dateofbirth,
            "gender":student.gender,
            
        }, status=200)
    elif request.method == "DELETE":
        data = json.loads(request.body)
        student = get_object_or_404(StudentDetails, id=data['id'])
        student.delete()
        return JsonResponse({"message": "Student deleted successfully."}, status=200)

@csrf_exempt
def marks(request):
    if request.method == "POST":
        data = json.loads(request.body)
        student = get_object_or_404(StudentDetails, id=data['student_id'])
        marks = Marks.objects.create(
            student=student,
            subject=data['subject'],
            marks=data['marks']
        )
        return JsonResponse({
            "id": marks.id,
            "student": marks.student.name,
            "subject": marks.subject,
            "marks": marks.marks
        }, status=201)

    elif request.method == "GET":
        marks = Marks.objects.all()
        markslist = [
            {
                "id": marks.id,
                "student": marks.student.name,
                "subject": mark.subject,
                "marks": marks.marks
            } for mark in marks
        ]
        return JsonResponse({"marks": markslist})
    elif request.method == "PUT":
        data = json.loads(request.body)  # Parse the incoming data from the request body
        mark = get_object_or_404(Marks, id=data['id'])  # Fetch the marks entry by ID
        mark.subject = data['subject']
        mark.marks = data['marks']
        mark.save()  # Save the updated marks entry
        return JsonResponse({
            "id": mark.id,
            "subject": mark.subject,
            "mark": mark.mark
        }, status=200)  # Return status 200 for success
    elif request.method == "DELETE":
        data = json.loads(request.body)
        mark = get_object_or_404(Marks, id=data['id'])
        mark.delete()
        return JsonResponse({"message": "Marks deleted successfully."}, status=200)


@csrf_exempt
def score(request):
    if request.method == "POST":
        # Create new score entry
        data = json.loads(request.body)
        marks = get_object_or_404(Marks, id=data['marks_id'])
        score = Score.objects.create(
            marks=marks,
            grade=data['grade']
        )
        return JsonResponse({
            "id": score.id,
            "marks": score.marks.id,
            "grade": score.grade
        }, status=201)

    elif request.method == "GET":
        # Retrieve all scores
        scores = Score.objects.all()
        scorelist = [
            {
                "id": score.id,
                "marks": score.marks.id,
                "grade": score.grade
            } for score in scores
        ]
        return JsonResponse({"scores": scorelist})
    elif request.method == "PUT":
        data = json.loads(request.body)  # Parse the incoming data from the request body
        score = get_object_or_404(Score, id=data['id'])  # Fetch the score entry by ID
        score.grade = data['grade']  # Update the grade
        score.save()  # Save the updated score 
        return JsonResponse({
            "id": score.id,
            "marks": score.marks.id,
            "grade": score.grade
        }, status=200) 
    elif request.method == "DELETE":
        data = json.loads(request.body)
        score = get_object_or_404(Score, id=data['id'])
        score.delete()
        return JsonResponse({"message": "Score deleted successfully."}, status=200)
@csrf_exempt
def personaldetails(request):
    if request.method == "POST":
        # Create new personal details
        data = json.loads(request.body)
        student = get_object_or_404(StudentDetails, id=data['student_id'])
        personaldetails = PersonalDetails.objects.create(
            student=student,
            address=data['address'],
            parentname=data['parentname'],
            phonenumber=data['phonenumber'],
            email=data['email']
        )
        return JsonResponse({
            "id": personaldetails.id,
            "student": personaldetails.student.name,
            "address": personaldetails.address,
            "parentname":personaldetails.parentname,
            "phonenumber": personaldetails.phonenumber,
            "email": personaldetails.email
        }, status=201)

    elif request.method == "GET":
        # Retrieve all personal details
        details = PersonalDetails.objects.all()
        detailslist = [
            {
                "id": detail.id,
                "student": detail.student.name,
                "address": detail.address,
                "parentname":detail.parentname,~
                "phonenumber": detail.phonenumber,
                "email": detail.email
            } for detail in details
        ]
        return JsonResponse({"personaldetails": detailslist})
    elif request.method == "PUT":
        data = json.loads(request.body)  # Parse the incoming data from the request body
        personaldetails = get_object_or_404(PersonalDetails, id=data['id'])  # Fetch the personal details by ID
        personaldetails.address = data['address']
        personaldetails.parentname = data['parentname']
        personaldetails.phonenumber = data['phonenumber']
        personaldetails.email = data['email']
        personaldetails.save()  # Save the updated personal details 
        return JsonResponse({
            "id": personaldetails.id,
            "student": personaldetails.student.name,
            "address": personaldetails.address,
            "parentname": personaldetails.parentname,
            "phonenumber": personaldetails.phonenumber,
            "email": personaldetails.email
        }, status=200)  
    elif request.method == "DELETE":
        data = json.loads(request.body)
        personaldetails = get_object_or_404(PersonalDetails, id=data['id'])
        personaldetails.delete()
        return JsonResponse({"message": "Personal details deleted successfully."}, status=200)
