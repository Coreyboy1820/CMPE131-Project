from app import myapp_obj, db, Session, user

@myapp_obj.route("/contacts")
def view_contacts():
    # create a new session to interact with the database
    session = Session()

    # get the user whose contact list we want to open
    user_to_open_contact_list = session.query(user).filter_by(email='user@example.com').first()

    # get the user's contact list
    contact_list = user_to_open_contact_list.contactList

    # close the session
    session.close()

    # render the contact list in a template
    return render_template('view_contacts.html', contact_list=contact_list)
