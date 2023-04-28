from app import db, Session, message, recipient, user

# First, let's check if the recipient exists in the database
session = Session()

    messages = session.query(message).all()
    for message in messages:
        if  messages.recipient.userId==user
        
        # Display the messages on the recipient's page
        print(f"Messages for recipient with id {recipient_id}:")
        for msg in messages:
            print(f"Subject: {msg.subject}")
            print(f"Sender: {msg.sender.email}")
            print(f"Message: {msg.message}")
            print("")

        # Define the relationship between the recipient and the messages in the database
        for msg in messages:
            rec = recipient(userId=recipient_id, message_id=msg.id)
            session.add(rec)

        # Commit the changes to the database
        session.commit()
