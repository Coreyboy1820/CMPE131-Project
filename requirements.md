## Functional Requirements

1. create a user account - Corey Kelley
2. compose email 
3. receive email
4. draft
5. view message history
6. open contact list
7. add contact 
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
  
  
  6. view message history
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


  7. Remind messages
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
  
  
 
