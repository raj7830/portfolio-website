from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

portfolio_data = {
    "name": "MD Sohail Ansari",
    "title": "M.Tech Student in Machine Learning and Computing",
    "about": "I'm a passionate developer pursuing M.Tech in Machine Learning and Computing at IIST with experience in Computer Vision, NLP, and IoT systems.",
    "email": "mdsohail9231@gmail.com",
    "contact_number": "7003167830",
    "linkedin": "md-sohail-ansari-a537a3187",
    "github": "raj7830",
    "brief_description": "MD Sohail Ansari is an M.Tech student in Machine Learning and Computing at IIST, with a passion for leveraging technology to solve real-world problems. With experience in Computer Vision, NLP, and IoT, he has worked on innovative projects like crop detection using Vision Transformers and intelligent power-saving systems. A GATE qualifier and avid learner, Sohail enjoys exploring the intersection of machine learning and practical applications.",
    "experience": [
        {
            "title": "Project Intern",
            "company": "Centre for Development of Advanced Computing (C-DAC)",
            "location": "Bangalore",
            "duration": "August 2024 - Present",
            "description": "Contributing to Crop and Pest Detection in Dense Agricultural Scene using Vision Transformer (ViT) with multi-modal approach."
        },
        {
            "title": "Graduate Engineering Apprentice",
            "company": "Bharat Petroleum Corporation Limited (BPCL)",
            "location": "Kolkata",
            "duration": "January 2020 - April 2021",
            "description": "Experienced in warehousing, stock accounting, maintenance, purchasing, logistics, and quality control."
        }
    ],
    "projects": [
        {
            "title": "Enhancing E-commerce Using an Advanced Search Engine and Recommendation System",
            "description": "Implemented using BERT on Flipkart E-commerce Dataset.",
            "category": "Natural Language Processing"
        },
        {
            "title": "Facial Emotion Detection Using Convolutional Neural Network",
            "description": "Built and trained on FER2013 dataset.",
            "category": "Computer Vision"
        },
        {
            "title": "Epidemic Modelling Using SIR Model",
            "description": "Implemented using ODEs, analyzed on COVID-19 dataset.",
            "category": "Statistical Models"
        },
        {
            "title": "Customer Churn Prediction",
            "description": "Developed using Waze Navigation App dataset.",
            "category": "Machine Learning"
        },
        {
            "title": "Intelligent Power Saving System using IoT",
            "description": "Designed using Arduino UNO and Proteus Simulation.",
            "category": "IoT"
        }
    ],
    "education": [
        {"degree": "M.Tech in Machine Learning and Computing", "institute": "IIST", "duration": "2023-2025", "cgpa": "8.38"},
        {"degree": "B.Tech in Electrical Engineering", "institute": "Aliah University", "duration": "2015-2019", "cgpa": "8.59"},
        {"degree": "Class XII", "institute": "National Institute of Open Schooling", "duration": "2015"},
        {"degree": "Class X", "institute": "Vikram Vidyalaya(Branch)", "duration": "2010-2012"}
    ],
    "skills": ["Python Programming", "Pandas", "NumPy", "PyTorch", "NetLogo"],
    "courses": ["Data Mining", "Numerical Linear Algebra", "Foundation of Machine Learning", "Optimization Techniques",
              "Digital Image Processing", "Graphical Models and Deep Learning", "Advance Machine Learning",
              "Computer Vision", "Statistical Models and Analysis", "Introduction to Complex Systems"],
    "achievements": ["3rd position in Debate Competition (PGCIL)", "GATE Qualified (2022, 2023)"],
    "hobbies": ["Playing Cricket", "Exploring places"],
    "blog_posts": [
        {
            "title": "Exploring Vision Transformers in Agriculture",
            "date": "February 15, 2025",
            "summary": "A deep dive into how Vision Transformers are revolutionizing crop detection in dense scenes."
        },
        {
            "title": "My Journey with Machine Learning",
            "date": "January 20, 2025",
            "summary": "Reflections on my M.Tech experience and key ML concepts I've learned."
        }
    ]
}

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "data": portfolio_data})

@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request, "data": portfolio_data})

@app.get("/projects", response_class=HTMLResponse)
async def projects(request: Request):
    return templates.TemplateResponse("projects.html", {"request": request, "data": portfolio_data})

@app.get("/contact", response_class=HTMLResponse)
async def contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request, "data": portfolio_data})

@app.get("/blog", response_class=HTMLResponse)
async def blog(request: Request):
    return templates.TemplateResponse("blog.html", {"request": request, "data": portfolio_data})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)