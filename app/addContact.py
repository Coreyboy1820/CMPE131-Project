from app import db, Session, user, userContact

# create a new session to interact with the database
session = Session()

# get the user you want to add the contact for
user_to_add_contact = session.query(user).filter_by(email='user@example.com').first()

# create a new contact object
new_contact = userContact(userId=user_to_add_contact.id, contactId=2, nickName='John')

# add the new contact to the user's contact list
user_to_add_contact.contactList.append(new_contact)

# commit the changes to the database
session.commit()

# close the session
session.close()
