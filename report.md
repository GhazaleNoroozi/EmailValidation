## README.md
There are two common ways to document a project: 
1. README files are the first thing a random user should see in order to learn about a project. RAEDME file is quick and simple.
2. Wikis are files are for presenting the project in depth.

A README file usually consists of:
*	Project name
*	Description: Include what your project does exactly and the importance of it. Project description should be clear, short and on point.  
*	Table of contents: Optional. Works as a general overview and a quick navigation on a lengthy file 
*	Installation: Explain how to install the project. Optionally include a gif for better understanding.
*	Contribution: Could be another file. Include contribution guidelines and instructions.  
*	Versioning 
*	Documentation 
*	Credit
*	License
And  a lot more if needed.

## Markdowns
Markdowns are easy and lightweight syntax for text on GitHub.
Use markdowns in:
•	Gist
•	.md or .markdown files
•	In comments in issues or pull requests

## Workflows
Workflows are guidelines and strict syntaxes to keep consistency and efficiency through the team and accomplish work in a productive manner. Your team can have your own new workflow or a combination of other workflows, it doesn’t matter. The only thing that matters is that you need to use a workflow and it should be compatible with your team’s size, culture and your product.
### Centralized workflow
There is only one central repository that serves as the single point of entry for all changes. (usually the ‘master’ branch). Everyone has their own local repository to work without being bothered by other member’s work. In this workflow there is no defined pull request and is good for smaller sized teams.
### Feature branch workflow
All changes are committed at a dedicated branch instead of the master branch. Good for teams with larger size and multiple developers. Another benefit would be that master won’t contain broken code.
Your feature branches should live short. It means that you should allocate a specific task to one branch. This helps to reduce conflicts and deployment problems and to have cleaner merge and easier deploy.
These apply to all workflows but you should think beforehand about reverts. You want to keep reverts as minimized and simplified as possible. 
### Gitflow workflow
It has a strict branching model which assigns role to branches and determines how and when they should interact. 
The common roles are develop and production. The develop branch is where feature branches are merged into and tests are performed. The production branch (usually the master branch) contains the functionality that is live for costumers to use. It’s fully tested and approved and does not contain broken code. If you have a website or a product accessed live, you probably want to use this approach.
### Forking workflow
There is no single server-side repository as the center. Every developer has not one but two git repositories: one private local one and one public server side one.
You clone the repository you want to work on to your repository and after that you send a pull request for the owner to merge your work if approve.
This workflow is best for opensource projects.

workflow | Forking | Feature branch
-------- | ------- | --------------
Integration |	Merge | Pull request
Start a new task | Create a new branch | Fork the whole repository


workflow | Gitflow | Trunk Based Development
-------- | ------- | -----------------------
branches | Many branches like develop branch and production branch | One master branch
Integrate | Pull request | Merge with feature branches
Review | After pull request they have discussion and if the code is mature enough the owner merges it | Full source code review
application | Open source projects, junior developers, stablished product | iterate quickly, Senior developers only, Early stages

