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
    post=Post(title="1",content="asdad",company_id=1)
    p = Post(title="2",content="test",company_id=2)
    db.session.add(post)  
    db.session.add(p)  
    db.session.commit()
    print("\n")
    print(Post.query.all())
