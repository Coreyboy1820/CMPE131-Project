from app import db, Session, user, userContact

# create a new session to interact with the database
session = Session()

# get the user whose contact list we want to open
user_to_open_contact_list = session.query(user).filter_by(email='user@example.com').first()

# get the user's contact list
contact_list = user_to_open_contact_list.contactList

# print the contact list
for contact in contact_list:
    print(f"Contact: {contact.contact.email}, Nickname: {contact.nickName}")

# close the session
session.close()
