#!/bin/bash

# Prompt the user for a commit message
read -p "Enter your commit message: " commit_message

# Add all changes to git
git add .

# Commit the changes with the provided message
git commit -m "$commit_message"

# Push the changes to the remote repository
git push origin master