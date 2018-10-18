# Contributing to Dinder Team
Quick guide to contributing to the project.

### Git Flow
The basic steps of updating code locally, and commiting that to the remote
master branch.

```
# List local branches and see what branch you're on
$ git branch

# Pull down changes from the remote repository for the branch you're on
$ git pull

# Create a new branch for new changes. Each branch should just contain the
# code for a feature. Try to avoid putting unrelated changes into a single 
# branch.
$ git checkout -b <feature_branch_name>

# Now that you're on a new branch, make your code changes, then check the 
# status to see which files you've modified.
$ git status

# Add the files you want to commit to "staging". You can specify a file
# directly, or a directory to add all files changed within it.
# You can keep making changes, and adding files to staging before you commit
# by calling this command.
$ git add <file_name>|<dir_name>

# Once you're happy with your code, commit everything you've added to 
# "staging" to your branch.
$ git commit -m "A brief message that explains what you did"

# Your branch does not yet exist on the remote repository. So a remote version
# of your branch needs to be created, then your code can be pushed to it.
# This command will do both.
$ git push --set-upstream origin <feature_branch_name>
```
At this point, you can go to the github repo and you should see a big green
"Compare & pull request" button at the top of the page. Click this to create a pull
request. Here you can add a more detailed description if you think it's helpful.

At this point you have two options:
1. __Get someone to review__: You can add reviewers from the dropdown on the 
right side to ask people to look at the code. This is preferred for any
substantial code changes. _Especially_ if it's something that will affect
code other people are working on.
2. __Merge to master__: If it's something small that you're confident about,
just go ahead and merge to master :)
