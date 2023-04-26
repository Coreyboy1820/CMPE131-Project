from app import db, Session, message, recipient, user

# First, let's check if the recipient exists in the database
session = Session()
recipient = session.query(user).filter_by(id=recipient_id).first()
if recipient is None:
    print(f"No recipient with id {recipient_id} found in the database.")
else:
    # If the recipient exists, let's retrieve all the messages addressed to them
    messages = session.query(message).join(recipient).filter(recipient.id == recipient_id).all()
    if not messages:
        print(f"No messages found for recipient with id {recipient_id}.")
    else:
        # Display the messages on the recipient's page
        print(f"Messages for recipient with id {recipient_id}:")
        for msg in messages:
            print(f"Subject: {msg.subject}")
            print(f"Sender: {msg.sender.email}")
            print(f"Message: {msg.message}")
            print("")

        # Define the relationship between the recipient and the messages in the database
        for msg in messages:
            rec = recipient(user_id=recipient_id, message_id=msg.id)
            session.add(rec)

        # Commit the changes to the database
        session.commit()

