# Resturant_project
Hello, This repository contains Restaurant Management System Project. GUI-based project in Python using module Tkinter

# General
Welcome to the Restaurant Management System project repository. This system provides a convenient interface for customers to view the menu, select items, customize orders, calculate the total payment including tax, and generate receipts. Additionally, it includes a calculator feature for verifying calculations. There are the files related to the project
- system.py
# Features
- View menu items
- Select items for order
- Customize order quantities
- Calculate total payment including tax
- Generate receipts with reference number, date, and time
- Calculator for verifying calculations

The Graphical User Interface in this project [Restaurant Management System GUI](https://github.com/TasniaSanta/Resturant_project/blob/main/Gui_screenshort.png)
<!--[![GUI](https://github.com/TasniaSanta/Resturant_project/blob/main/Gui_screenshort.png)]-->
<!--[![Restaurant Management System GUI](Gui_screenshort.png)]-->

<!--[![Restaurant Management System GUI](Gui_screenshort.png)](https://github.com/TasniaSanta/Resturant_project/blob/main/Gui_screenshort.png)-->

The Graphical User Interface with the features in this project [System GUI](https://github.com/TasniaSanta/Resturant_project/blob/main/Gui_screenshort_total.png)

# 1. Git
Throughout the journey of building this project, I delved into the world of Git, a powerful tool for managing project versions. Before this project, I was pretty green when it came to Git. But as I dove in, pushed code, pulled changes, and merged branches, I found myself gaining confidence with each commit. Git became my trusty companion, helping me organize my work, collaborate effectively with teammates, and navigate through the twists and turns of development. Moreover, Integrating SonarCloud and GitHub Actions into our workflow has been a game-changer. It's like having a personal assistant to track our project's progress.
GitHub: 
<!--![alt text](https://github.com/TasniaSanta/Resturant_project/blob/main/photo/imageGitHub.png)-->
<img src="https://github.com/TasniaSanta/Resturant_project/blob/main/photo/imageGitHub.png" alt="alt text" width="400"/>

# 2. UML
For my project, I have used these 3 UML diagrams :
1. [SequenceDiagram](https://github.com/TasniaSanta/Resturant_project/blob/main/UMLDiagram/SequenceDiagram.png)- These diagrams offer a clear representation of the flow of operations and communication between different modules, helping to illustrate the behavior and logic of the system.
2. [UseCaseDiagram](https://github.com/TasniaSanta/Resturant_project/blob/main/UMLDiagram/UseCaseRMDiagram.png)-The diagram defining the various interactions between actors (users or external systems) and the system itself. These diagrams provide a high-level overview of the system's functionalities and the different roles involved in interacting with the system.
3. [ClassDiagram](https://github.com/TasniaSanta/Resturant_project/blob/main/UMLDiagram/classDiagramupdate.png)- The diagram has played a role in showing the static structure of our system. it illustrates the different classes, their attributes, methods, and the relationships between them.
   
# 3. DDD
In my project, I've chosen Domain-Driven Design (DDD) for its focus on modeling the core domain, establishing clear boundaries, and promoting collaboration through a ubiquitous language.
1. I conducted a collaborative brainstorming session to outline project goals and features. Through various techniques like mind mapping, I generated ideas and prioritized requirements, setting the foundation for the development plan.[Brainstorming](https://github.com/TasniaSanta/Resturant_project/blob/main/DDD/BrainstormingFirststep.png)
2. I recorded the key domain concepts, aiming for a deep understanding. This helped me to make a better decision.[Domain_concepts](https://github.com/TasniaSanta/Resturant_project/blob/main/DDD/domainidea.png)
3. After grasping domain ideas, I honed in on developing a 'ubiquitous language'—a common vocabulary that I could easily understand to ensure smooth communication.[ubiquitous language](https://github.com/TasniaSanta/Resturant_project/blob/main/DDD/domainUbiquitous%20Language.png)
4. After gathering ideas, I sketched out a context map a visual roadmap outlining key content and its relationships.[ContexMapping](https://github.com/TasniaSanta/Resturant_project/blob/main/DDD/ContexMapping.png)
5. And finally Core domain chart.[CoreDomainChart](https://github.com/TasniaSanta/Resturant_project/blob/main/DDD/CoreDomainChart.png)

# 4. Metrics
I have used the sonar cloud to maintain and analyze code quality
<!--<img src="https://github.com/TasniaSanta/Resturant_project/blob/main/photo/article-SonarCloud-Analysez-votre-projet-GitHub-via-VSTS.jpg" alt="alt text" width="200"/>-->

[![Click me](https://github.com/TasniaSanta/Resturant_project/blob/main/photo/Sonercloud.png)](https://sonarcloud.io/summary/overall?id=TasniaSanta_Resturant_project)

These are the metrics listed below :

- Quality Gate Status(Passed):[Status](https://sonarcloud.io/summary/overall?id=TasniaSanta_Resturant_project)
- Maintainability(0 Code Smells): [Maintainability Rating](https://sonarcloud.io/component_measures?metric=Maintainability&view=list&id=TasniaSanta_Resturant_proje)
- Duplications(Duplicated Lines (%)0.0%):[Duplications](https://sonarcloud.io/component_measures?id=TasniaSanta_Resturant_project&metric=duplicated_lines_density&view=list)
- Security (0 Vulnerabilities)(A):[Review](https://sonarcloud.io/component_measures?metric=Security&view=list&id=TasniaSanta_Resturant_p)
- Security Review(0 Security Hotspots)(A): [Review](https://sonarcloud.io/component_measures?id=TasniaSanta_Resturant_project&metric=security_review_rating&view=list)
- Reliability Rating(0 Bugs)(A): [Rating](https://sonarcloud.io/component_measures?id=TasniaSanta_Resturant_project&metric=reliability_rating&view=list)
- Lines of Code:534 

# 5. Clean Code Development
[Cheatsheet](https://github.com/TasniaSanta/Resturant_project/blob/main/Cheatsheet.txt) Clean code development and it's an example in my code

**Readability:** The code is easy to understand, with clear names, concise expressions, and consistent indentation. Plus, I have added helpful comments before each function to explain what it does. As one can see by the sonar cloud readability analysis.[Reliability_Rating](https://sonarcloud.io/component_measures?id=TasniaSanta_Resturant_project&metric=reliability_rating&view=list)

**Comments:** Use clear and concise comments that explain the why behind the code, not just what.
[Comments](https://github.com/TasniaSanta/Resturant_project/blob/main/system.py#L174)

**Naming conventions of variables and function:** Use of descriptive names for functions that convey their purpose. For example, exit_application,reset_values,calculate_costs, and generate_receipt_reference are named properly as per their functionality.[Naming convention](https://github.com/TasniaSanta/Resturant_project/blob/main/system.py#L175)

**Duplication:** Avoiding duplication of code, by creating reusable functions, modules, or libraries. As one can see by the sonar cloud metrics duplication is 0%[Duplications](https://sonarcloud.io/component_measures?id=TasniaSanta_Resturant_project&metric=duplicated_lines_density&view=list)

**Unittest:** There is a also comprehensive unit test[Unittest](https://github.com/TasniaSanta/Resturant_project/blob/main/test_system.py)
**Modularity:** The codes written are broken down into smaller ones, Use indentation, spacing, and line breaks to improve the code quality.[Check_here](https://github.com/TasniaSanta/Resturant_project/blob/main/system.py#217)





