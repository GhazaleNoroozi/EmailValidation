## README.md
There are two common ways to document a project: 
1. README files are the first thing a random user should see in order to learn about a project. RAEDME file is quick and simple.
2. Wikis are files are for presenting the project in depth.

A README file usually consists of:
*	Project name
*	Description: Include what your project does exactly and the importance of it. Project description should be clear, short and on point.  
![Alternate image text](http://s12.picofile.com/file/8403931068/Annotation_2020_07_25_193618.png)
*	Table of contents: Optional. Works as a general overview and a quick navigation on a lengthy file 
![Alternate image text](http://s13.picofile.com/file/8403931042/Annotation_2020_07_25_193613.png)
*	Installation: Explain how to install the project. Optionally include a gif for better understanding.
*	Contribution: Could be another file. Include contribution guidelines and instructions.  
![Alternate image text](http://s13.picofile.com/file/8403931018/Annotation_2020_07_25_193605.png)
*	Versioning 
![Alternate image text](http://s12.picofile.com/file/8403930976/Annotation_2020_07_25_193552.png)
*	Documentation 
![Alternate image text](http://s12.picofile.com/file/8403930992/Annotation_2020_07_25_193559.png)
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

## Semantic Versioning
In systems with many dependencies, either may dependencies are too tight and the project is in danger of _version lock_, which means being unable to upgrade without realeasing new version of each package, or dependencies may be too loose in which case the project is in danger of _version promiscuity_, which means assuming compaitbility with more versions in future than necessary. 
As a solution, we use semantic versioning. For semantic versioning first declare a public API. It can be a strict documentation or implemented in code. Then move foreward with Major.Minor.Patch structure. Start with 0.1.0 which is not a stable version and implies early stage of development. For every incompatible API change increment the Major part, for every new functionality in backward compatible manner increment Minor part and for every backward compatible bugfix increment Patch part of the structure.

## Conventions in commit messages
![Alternate image text](http://s12.picofile.com/file/8403932318/hi.png)

Commits should be consistent and concise. A team should have a guidline for style, content and use of metadata (use of issue tracking IDs and pull request numbers as reference) in a commit to ensure consistency. 

