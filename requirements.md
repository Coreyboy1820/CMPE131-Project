## Functional Requirements

1. create a user account - Corey Kelley
2. compose email 
3. receive email
4. draft
5. view message history
6. open contact list
7. add contact Labibeh Taghizadeh
8. remove contact 
9. change credential
10. share todo list
11. add todo item
12. remove todo item
13. remind messages
14. edit task/todo item
15. checkbox for todo item
16. add comment to todo item 
17. prioritize todo item
18. add todo date

## Non-functional Requirements

1. System sends and user recieves email in under 1 second
2. system registers new user after user clicks submit in under 1 second
3. System keep the set priority for each todo item
4. System will complete any removals from the app in under 1 second

## Use Cases

1. Create a user account
- **Pre-condition:** 
  -the user navigates to the register page

- **Trigger:** 
  -clicks the register button

- **Primary Sequence:**
  -user types in their username
  -user types in their password
  -user clicks the trigger

- **Primary Postconditions:**
  -user now has a new account
  -user is redirected to a new website


- **Alternate Sequence:**
  -user types taken username
  -user types password
  -user clicks the trigger

2. Add comment to todo item 
- **Pre-condition:** 
  -User has navigated to the todo list and is logged in

- **Trigger:** 
  -User has clicked confirmed

- **Primary Sequence:**
  -User clicks the 3 dots on the todo item
  -User clicks the add comment button
  -User types in their comment
  -user clicks the trigger

- **Primary Postconditions:**
  -user can now see the comment under the todo item

- **Alternate Sequence:**
  -User clicks cancel

- **Alternate Postconditions:**
  -User lost everything they typed into the comment box
  

3. Add todo item
- **Pre-condition:** 
  -User has navigated to the todo list and is logged in

- **Trigger:** 
  -User has cliked on the Add todoItem button

- **Primary Sequence:**
  - toDo item textBox pops up 
  - User gives the name for the todo item 
  - User gives the brief description for the item
  - User adds deadline for the item 
  - User clicks the Add button located at the bottom right corner of the textBox

- **Primary Postconditions:**
  -User is navigated back to the todo list and now see the todo item

- **Alternate Sequence:**
  -User clicks cancel

- **Alternate Postconditions:**
  -User loses everything they typed into the todo item textBox
  -User is navigated back to the todo list page
  
  
4. Remove todo item
- **Pre-condition:** 
  -User has navigated to the todo list and is logged in

- **Trigger:** 
  -User has cliked on the trash can icon located at the end of the todo item

- **Primary Sequence:**
  - The alert pops up warning the user about their action
  - User clicks Delete button 
  - the final confirmation alert pops up 
  - User clicks Ok button


- **Primary Postconditions:**
  -User is navigated back to the todo list
  -The todo item is now gone

- **Alternate Sequence:**
  -User clicks Cancel button in the final confirmation alert
  -User is navigated back to the initial alert
  -User clicks the x icon at the top right corner of the alert
  

- **Alternate Postconditions:**
  -User is navigated back to the todo list
  -The todo item remains the same
  


5. Compose email 
- **Pre-condition:** 
  -User has navigated to the email page and is logged in

- **Trigger:** 
  -User has cliked on the Compose Email button

- **Primary Sequence:**
  - The textBox pops up
  - User inputs the recipient  
  - User inputs the subject
  - User inputs the content 
  - User clicks Send button


- **Primary Postconditions:**
  -The confirmation alert pops up indicating the email was successfully sent
  -User is navigated back to the email page

- **Alternate Sequence:**
  -User clicks Cancel button 
  

- **Alternate Postconditions:**
  -Everything the user inputed is saved as a draft
  -The draft goes into the drafts container located in the email page
  -User is navigated back to the email page
  

6.Add contact 
Add contact Pre-condition: A registered user has logged in to his/her email account. User has to be in the contact list tab. 
Trigger: -User clicks the “AddContacts” button
Primary Sequence:
 User clicks the "Add Contact" button in the main window.
 A box appears, with title "New Contact '', containing fields for the user to fill in the new Contact's first and last names and email address. 
User clicks save. 
Primary Postconditions: User is directed to the main page.
Alternate Sequence: -User enters the contact that already existed. “Contact already exists” message appears on the screen. User clicks the Cancel button and exits the box.

7.Remove contact 
Remove contact Pre-condition: A registered user has logged in to his/her email account. User has to be in the contact list tab.  
Trigger: -User clicks the “remove” button.
Primary Sequence: 
User selects the desired contact by clicking on the contact name.
the remove button  appears on the right side of the contacts.
user selects delete.
Primary Postconditions: The deleted contact is removed from the contact list.
Alternate Sequence: User is unable to find the desired contact. User clicks on sort Alphabetically. User finds the contacts, selects, removes the contact.

8.Draft email
Draft email Pre-condition: A registered user has logged in to his/her email account. User is in the compose window.  
Trigger: -User clicks the “Save” button.
Primary Sequence:
User writes a text 
User adds the links/files. 
User Clicks the “Save” button.
Primary Postconditions: Saved email is listed in the Draft tab.
Alternate Sequence: User clicks the close window button. “Save” and “Do not save” buttons appear on the screen. User clicks the save button. 
