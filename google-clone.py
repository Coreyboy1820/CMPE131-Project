from app import myapp_obj, models
import secrets
from datetime import date

myapp_obj.debug=True
myapp_obj.config['SECRET_KEY'] = secrets.token_hex(16)

# u = models.user(email="nobito@gmailclone.com", passwordHash="nobito")
# u1 = models.user(email="khate22@gmailclone.com", passwordHash="khate22")
# u2 = models.user(email="lenat44@gmailclone.com", passwordHash="lenat44")
# u3 = models.user(email="coreyboy1820@gmailclone.com", passwordHash="hs")



# dbSession = models.Session()
# current_date = date.today()
# dbSession.begin()
# message = models.message(id=0, senderId= dbSession.query(models.user).filter_by(email="phongdiep@gmail.com").first().id ,message= "hs", sentDate= current_date, recievedDate = current_date, subject= "hs" )
# dbSession.add(message)
# dbSession.commit()


# dbSession = models.Session()
# dbSession.begin()
# receipient = models.recipient(id=0, userId=dbSession.query(models.user).filter_by(email="phongdiep@gmail.com").first().id , messageId= 0)
# dbSession.add(receipient)
# dbSession.commit()






# print(dbSession.query(models.message).first().message)
# dbSession.close()
# session.begin()
# session.add(u)
# session.add(u1)
# session.add(u2)
# session.commit()


if __name__ == "__main__":
    myapp_obj.run(port=5000)
