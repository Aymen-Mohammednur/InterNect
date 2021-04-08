def create(db):
    
    from interNect.models import User,Post,Pending,Company
    from flask_bcrypt import Bcrypt
    db.create_all()

    bcrypt=Bcrypt()
    password=bcrypt.generate_password_hash('1234').decode('utf-8')
  
    user=User(username='suraap',email='sutrap@gmail.com',password=password,lname="Aman",fname="aman",gender='male')
    
    db.session.add(user)  
    db.session.commit()
    # post=Post(title="1",content="asdad",user_id=1)
    
    # db.session.add(post)  
    db.session.commit()
    print("\n")
    print(User.query.first())
