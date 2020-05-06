#List remote branches
git branch -r --list

# Delete a local branch
git branch --delete <BRANCH_NAME
>
# Switch branch local
git checkout <BRANCH_NAME>

#Pull branch from remote and create local branch
git checkout -b LOCAL_BRANCH_NAME origin/<REMOTE_BRANCH_NAME>
