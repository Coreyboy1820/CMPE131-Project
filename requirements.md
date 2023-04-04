## Functional Requirements

1. create a user account
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
  -user is then redirected to a new website


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