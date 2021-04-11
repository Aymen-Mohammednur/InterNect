def create(db):
    
    from interNect.models import User,Post,Pending,Company
    from flask_bcrypt import Bcrypt
    db.create_all()

    bcrypt=Bcrypt()
    password=bcrypt.generate_password_hash('1234').decode('utf-8')
    
    user=User(username='suraap',email='sutrap@gmail.com',password=password,lname="Aman",fname="aman",gender='male')
    u=User(username='aman',email='aman@gmail.com',password=password,lname="Aman",fname="aman",gender='male')
    
    c= Company(company_name="Google",email="g@gmail.com",password=password)
    company = Company(company_name="Microsoft",email="m@gmail.com",password=password)  
    
    db.session.add(user)  
    db.session.add(u)
    db.session.add(c)
    db.session.add(company)

    db.session.commit()
    post=Post(title="IT intern",content="Our Software Engineering company known for innovative technology seeks a self-directed IT intern with a passion for technology, collaboration, and creative problem-solving. The intern will actively contribute to meaningful projects and work closely with a mentor and with senior leadership.",company_id=1)
    post2 = Post(title="Software Engineering Intern",content="Our Company seeks an intern with experience in software design, coding and debugging. The intern will gain exciting real-world software engineering experience at a thriving company. We frequently work in small teams to solve problems, explore new technologies, and learn from one another. The ideal intern for this environment will be enthusiastic and collaborative.",company_id=2)
    post3 = Post(title="Manufacturing Intern Job",content="Our Company, an intense and exciting company, is looking for interns to join our creative team of engineers working to develop systems and analysis for a wide variety of companies and industries. Our engineers are hard-working, smart, goal-oriented and creative, and they are looking for interns to train to participate in every level of system design and orientation. The interns hired for this position should expect to learn all facets of manufacturing, and will leave this position with invaluable skills and industry knowledge. Also, this internship program is highly regarded in our field, so successful participation will be a great addition to your resume.",company_id=2)
    post4 = Post(title="Graphic Design Intern",content="Are you a student interested in building real-world graphic design experience with an award-winning team? We’re a forward-thinking advertising agency looking for a talented and knowledgeable designer with fresh, creative ideas and an excellent eye for detail. Come work for one of the area’s leading advertising agencies and learn from some of the best in the business.",company_id=2)
    post5 = Post(title="HR (Human Resources) Intern",content="Fast-growing marketing agency seeks a personable and highly motivated HR intern to support the HR manager in day-to-day administrative tasks and activities. If you’re ready to kickstart your career in Human Resources and build real-world experience with recruiting, payroll, employee development, and the coordination of HR policies and procedures, this is the internship for you.",company_id=2)
    db.session.add(post)  
    db.session.add(post2)  
    db.session.add(post3)  
    db.session.add(post4)  
    db.session.add(post5)  
    db.session.commit()
    print("\n")
    print(Post.query.all())
