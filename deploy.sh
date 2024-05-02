# Initialize a new GitHub repository if you don't have one
git init
git remote add origin <YOUR_GITHUB_REPO_URL>

# Add files to the repository and commit
git add index.html
git commit -m "Deploy chatbot frontend"

# Push to GitHub and enable GitHub Pages
git push -u origin master
