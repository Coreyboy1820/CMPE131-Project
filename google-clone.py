from app import myapp_obj, models
import secrets
from datetime import date

myapp_obj.debug=True
myapp_obj.config['SECRET_KEY'] = secrets.token_hex(16)

<<<<<<< HEAD

# dbSession = models.Session()
# usercontact = models.userContact(id=0, userId=1, contactId=2, nickName='Phong')
# dbSession.add(usercontact)
# dbSession.commit()
# dbSession.close()

# u = models.user(email="nobito@gmailclone.com", passwordHash="nobito")
# todoList = models.todoList(id=0, userId=0, name="Test")
# todoItem = models.todoItem(id=0, todoListId=0, name="Test", priority=1, startDate=date.today(), dueDate=date.today(), status=False)
# u = models.user(id=0, email="test@gmailclone.com", passwordHash="test")
# u2 = models.user(email="lenat44@gmailclone.com", passwordHash="lenat44")
# u3 = models.user(email="coreyboy1820@gmailclone.com", passwordHash="hs")



# dbSession = models.Session()
# current_date = date.today()
# dbSession.begin()
# message = models.message(id=0, senderId= dbSession.query(models.user).filter_by(email="phongdiep@gmail.com").first().id ,message= "hs", sentDate= current_date, recievedDate = current_date, subject= "hs" )
# dbSession.add(message)
# message = models.message(id=0, senderId=0  ,message= "hs", sentDate= current_date, recievedDate = current_date, subject= "hs" )
# dbSession.add(u)
# dbSession.add(todoList)
# dbSession.add(todoItem)
# dbSession.commit()


# dbSession = models.Session()
# dbSession.begin()
# receipient = models.recipient(id=0, userId=dbSession.query(models.user).filter_by(email="phongdiep@gmail.com").first().id , messageId= 0)
# dbSession.add(receipient)
# dbSession.commit()






# print(dbSession.query(models.message).first().message)
# dbSession.close()
# session.begin()
# session.add(u1)
# session.add(u2)
# session.commit()

=======
models.database_setup()
>>>>>>> main

if __name__ == "__main__":
    myapp_obj.run(port=5000)
