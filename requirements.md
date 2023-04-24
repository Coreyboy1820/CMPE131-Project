## Functional Requirements

1. create a user account - Corey Kelley
2. compose email - Khate
3. receive email - Labibeh
4. view message history - Phong
5. open contact list
6. add contact
7. remove contact
8. change email
9. share todo list
10. add todo item
11. remove todo item
12. remind messages
13. edit task/todo item
14. checkbox for todo item
15. add comment to todo item
16. prioritize todo item
17. add todo date
18. logout
19. change username

## Non-functional Requirements

1. System will work on at least google chrome and edge
2. System registers new user after user clicks submit in under 1 second
3. System keep the set priority for each todo item
4. System will support multiple color schemes

## Use Cases

### 1. Create a user account

- **Pre-condition:**

  - the user navigates to the register page

- **Trigger:**

  - clicks the register button

- **Primary Sequence:**

  - user types in their email
  - user types in their password
  - user types in their password one more time (password confirmation)
  - user clicks the trigger

- **Primary Postconditions:**

  - the textbox pops up, displaying the message "You have successfully registered"
  - user now has a new account
  - user is redirected to a login page

- **Alternate Sequence:**

  - user types taken username
  - user types password
  - user clicks the trigger

- **Alternate Postconditions:**
  - The textbox pops up, displaying the error and preventing the user from registering

### 2. Add comment to todo item

- **Pre-condition:**

  - User has navigated to the todo list and is logged in

- **Trigger:**

  - User has clicked confirmed

- **Primary Sequence:**

  - User clicks the 3 dots on the todo item
  - User clicks the add comment button
  - User types in their comment
  - user clicks the trigger

- **Primary Postconditions:**

  - user can now see the comment under the todo item

- **Alternate Sequence:**

  - User clicks cancel

- **Alternate Postconditions:**
  - User lost everything they typed into the comment box

### 3. Add todo item

- **Pre-condition:**

  - User has navigated to the todo list and is logged in

- **Trigger:**

  - User has cliked on the Add todoItem button

- **Primary Sequence:**

  - todo item textBox pops up
  - User gives the name for the todo item
  - User gives the brief description for the item
  - User adds deadline for the item
  - User clicks the Add button located at the bottom right corner of the textBox

- **Primary Postconditions:**

  - User is navigated back to the todo list and now see the todo item

- **Alternate Sequence:**

  - User clicks cancel

- **Alternate Postconditions:**
  - User loses everything they typed into the todo item textBox
  - User is navigated back to the todo list page

### 4. Remove todo item

- **Pre-condition:**

  - User has navigated to the todo list and is logged in

- **Trigger:**

  - User has cliked on the trash can icon located at the end of the todo item

- **Primary Sequence:**

  - The alert pops up warning the user about their action
  - User clicks Delete button
  - the final confirmation alert pops up
  - User clicks Ok button

- **Primary Postconditions:**

  - User is navigated back to the todo list
  - The todo item is now gone

- **Alternate Sequence:**

  - User clicks Cancel button in the final confirmation alert
  - User is navigated back to the initial alert
  - User clicks the x icon at the top right corner of the alert

- **Alternate Postconditions:**
  - User is navigated back to the todo list
  - The todo item remains the same

### 5. Compose email

- **Pre-condition:**

  - User has navigated to the email page and is logged in

- **Trigger:**

  - User has clicked on the Compose Email button

- **Primary Sequence:**

  - A modal pops up with multiple fillable text boxes
  - User inputs the recipient email
  - User inputs the subject
  - User inputs the message
  - User clicks the send button

- **Primary Postconditions:**

  - The confirmation alert pops up indicating the email was successfully sent
  - User is navigated back to the email page

- **Alternate Sequence:**
  - User clicks Cancel button
- **Alternate Postconditions:**
  - User lost everything they inputed
  - User is navigated back to the email page

### 6. Add contact

- **Pre-condition:**

  - A registered user has logged in to his/her email account
  - User has to be in the contact list tab

- **Trigger:**

  - User clicks the “AddContacts” button

- **Primary Sequence:**

  - User clicks the "Add Contact" button in the main window
  - A box appears, with title "New Contact '', containing fields for the user to fill in the new Contact's first and last names and email address.
  - User clicks save.

- **Primary Postconditions:**

  - User is directed to the main page.

- **Alternate Sequence:**
  - User enters the contact that already added.
  - “Contact already added” message appears on the screen.
  - User clicks the Cancel button and exits the box.

### 7. Remove contact

- **Pre-condition:**

  - A registered user has logged in to his/her email account.
  - User has to be in the contact list tab.

- **Trigger:**

  - User clicks the “remove” button.

- **Primary Sequence:**

  - User selects the desired contact by clicking on the contact name.
  - The remove button appears on the right side of the contacts.
  - user selects delete.

- **Primary Postconditions:**

  - The deleted contact is removed from the contact list.

- **Alternate Sequence:**
  - User is unable to find the desired contact.
  - User clicks on sort Alphabetically.
  - User finds the contacts, selects, removes the contact.

### 8. view message history

- **Pre-condition:**
- The user has access to the internet and a web browser
- The web application is live and accessible by the user
- User has navigated to the message list and is logged in

- **Trigger:**
  -User has cliked on the message history button

- **Primary Sequence:**

  - The list of messages pops up
  - Scroll down to message filtering
  - user clicks filtering messages button
  - user clicks filter unread messages button
  - The list of unread messages pops up

- **Primary Postconditions:**

  - The confirmation alert pops up indicating the button for more options
  - user clicks filtering unknown senders
  - User is navigated to the list of unknown senders messages

- **Alternate Sequence:**
  - User clicks main page button
- **Alternate Postconditions:**
  - If the web application encounters an error, it asks the user to try again later

### 9. Remind messages

- **Pre-condition:**

  - The user has access to the internet and a web browser
  - The web application is live and accessible by the user
  - User has navigated to the message list and is logged in

- **Trigger:**

  - User has clicked on the setting button

- **Primary Sequence:**

  - The list of options pops up
  - Scroll down to notification messages
  - User choice all messages
  - User clicks to turn on button

- **Primary Postconditions:**

  - User is navigated back to the setting
  - Scroll down in list of option and choice times of remind
  - user choice two times of remind

- **Alternate Sequence:**

  - User clicks on the main page button
  - User has clicked on the setting button
  - User clicks to turn off notification button

- **Alternate Postconditions:**
  - If the web application encounters an error, it asks the user to try again later
