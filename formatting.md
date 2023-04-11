# Code Formatting/Tips

### Variable and Function Names
1. Snake case EX: this_is_snake_case
2. Be descriptive, even if the variable name is long. This will allow for greater code readability. EX: time_of_event = datetime(hours = 1)

### Code Formatting
1. Break out large snippets of code into more object oriented code to make it more readable and modular. Modular: When code is broken down into small usable pieces which helps with code reusability
2. Each file should end with a newline 
3. Comment on the inputs and outputs of each function above the function name, if the code is readable then no comments are needed inside of the code. But when someone is trying to us a function someone else created, having comments on what the inputs are and the expected outputs could help with reusability.

### Development Flow
1. Checkout to the main branch before new branch is made
2. Pull the latest changes
3. Make your new branch
4. Add your feature in code
5. Run the commands to push code to the remote (github)
6. Make a pull request by going to the following link: https://github.com/Coreyboy1820/CMPE131-Project/pulls and clicking on the green button
7. Request someone as a reviewer to ensure your code is up to par and works as intended
8. Merge changes post review
9. Delete branch so we don't have random open branches on our repository
10. Code: 
    1. **git checkout main**
    2. **git pull origin main** (or **git pull**), if this doesn't update it, sometimes **git fetch -a** will solve the issue
    3. **git add .**
    4. **git commit -m ":gitmoji: commit message here"**
    5. **git push**

### Merge Conflicts
1. If you don't have VSCode installed, please do so. As this will make your life much easier to deal with merge conflicts
2. Usually, this will happen because two people touched the same area of a file, one merged code into main, and the other tried pushing their code on top of the changes someone else recently made
3. If this happens, github will notify you that you have merge conflicts
4. To deal with this please do the following:
    1. **git checkout main**
    2. **git pull**
    3. **git checkout -** if this doesn't work run **git checkout branch-name-you-just-came-from**
    4. **git merge main**
    5. When you do this, all the changes someone else pushed to main will then be brought into your branch, and in your terminal in VSCode (if it isn't open press ctrl + `) the conflicts and the files/lines they appear at will pop up.
    6. Now to deal with the merge conflicts ctrl click on the filename/line numbers that appear in your terminal and it will bring you over to where the merge conflicts are
    7. The places with merge conflicts will appear in two different colors, one with your changes, one with the changes from another person
    8. PLEASE try to communicate with the group to see what changes are best or why someone changes an area you are also working on, this way no bugs are introduced to our system.
    9. Buttons above the highlighted areas will appear saying "accept incoming changes" which is someones elses changes, "accept current changes" your own, then "accept both"
    10. Click one of the buttons to accepting the changes that you need ***AFTER*** talking to the group about what changes to keep.
    11. After ALL the merge conflicts are handled push your changes one more time and then request another approval

### Commit Messages
1. Your commit messages are more important then you think, so please be very descriptive with every one.
2. Don't forget that git is a version control tool, if you aren't descriptive with your commits, then when you introduce an accidental bug in your branch you won't be able to find the correct one as easily
3. Try to use gitmoji's in your commit history. This is a fun, unique, and descriptive way to help us all see what is going on in each commit, here is the link: https://gitmoji.dev/

### Branch Names
1. Branch names are just as important as commit messages/history
2. You will want to be able to see what each branch is by just looking at the name and the easiest way to do this is by naming it with a good convention
3. Our branch naming convention will be First-Name-Feature-That-You-Are-Implementing EX: Corey-Sending-email

### File Names
1. All lower case and -'s between words, try to keep the file names to a few words at most
2. EX: file-name.py

### Issue handling
1. In the future we will be using projects in github along with the issues
2. When we do this, each issue will be assigned to a person, and github has a cool feature when making a pr that lets you close them when you merge your code into the main branch
3. Issues on github: https://github.com/Coreyboy1820/CMPE131-Project/issues
4. Project boards on github: https://github.com/Coreyboy1820/CMPE131-Project/projects?query=is%3Aopen
5. Issues example on github: https://github.com/Coreyboy1820/CMPE131-Project/issues/11
6. To take advantage of the feature I mentioned in 2, when you make a PR, goto the description and type "resolves #issue_number" where issue number is the number of the issue, if you goto the link in 5, you will see the issue number is right next to the issue name.
7. Issues can also be assigned to people, when you get a task go ahead and assign yourself to it, or whenever you see another thing that needs to be done, please goto the link in 3 and press the new issue button to create an issue. Project lead isn't the only one who can do this, the more autonomous you guys are, the more prodcutive we can be