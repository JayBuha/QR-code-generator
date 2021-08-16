from django.shortcuts import redirect, render
import qrcode
import qrcode.image.svg
from io import BytesIO

# Create your views here.
data = None
context = None


def home(request):
    return render(request, 'home.html')


def CreatCode(request):
    global data
    global context
    context = {}

    Student_ID = request.POST.get("s_id", "")
    Enrollment_No = request.POST.get("e_no", "")
    Student_Name = request.POST.get("s_name", "")
    Branch_Name = request.POST.get("b_name", "")
    Contact_No = request.POST.get("c_no", "")

    data = {
        "Student_ID": Student_ID,
        "Enrollment_No": Enrollment_No,
        "Student_Name": Student_Name,
        "Branch_Name": Branch_Name,
        "Contact_No": Contact_No
        }

    if request.method == "POST":
        factory = qrcode.image.svg.SvgImage
        img = qrcode.make(data, image_factory=factory, box_size=20)
        stream = BytesIO()
        img.save(stream)
        context["svg"] = stream.getvalue().decode()
    return render(request, "home.html", {"context": context})

def save(request):
    global context
    global data
    a=data['Student_ID']
    img=qrcode.make(data)
    img.save(a + ".jpg")
    return render(request, "home.html", {"context": context,"succes":"QRcode is Dowunloded"})
