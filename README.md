# Resturant_project
Hello, This repository contains Restaurant Management System Project. GUI-based project in Python using the module Tkinter

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
<img src="https://github.com/TasniaSanta/Resturant_project/blob/main/photo/imageGitHub.png" alt="alt text" width="200"/>

Throughout the journey of building this project, I delved into the world of Git, a powerful tool for managing project versions. Before this project, I was pretty green when it came to Git. But as I dove in, pushed code, pulled changes, and merged branches, I found myself gaining confidence with each commit. Git became my trusty companion, helping me organize my work and collaborate effectively with my teammates. Moreover, Integrating SonarCloud and GitHub Actions into the workflow has been a game-changer. It's like having a personal assistant to track our project's progress.
GitHub: 

# 2. UML
For my project, I have used these 3 UML diagrams :
1. [SequenceDiagram](https://github.com/TasniaSanta/Resturant_project/blob/main/UMLDiagram/SequenceDiagram.png)- These diagrams offer a clear representation of the flow of operations and communication between different modules, helping to illustrate the behavior and logic of the system.
2. [UseCaseDiagram](https://github.com/TasniaSanta/Resturant_project/blob/main/UMLDiagram/UseCaseRMDiagram.png)-The diagram defining the various interactions between actors (users or external systems) and the system itself. These diagrams provide an overview of the system's functionalities and the different roles involved in interacting with the system.
3. [ClassDiagram](https://github.com/TasniaSanta/Resturant_project/blob/main/UMLDiagram/classDiagramupdate.png)- The diagram has played a role in showing the static structure of the system. it illustrates the different classes, their attributes, methods, and the relationships between them.
   
# 3. DDD
In my project, I've chosen Domain-Driven Design (DDD) for its focus on modeling the core domain, establishing clear boundaries, and promoting collaboration through a ubiquitous language.
1. I conducted a collaborative brainstorming session to outline project goals and features. Through various techniques like mind mapping, I generated ideas and prioritized requirements, setting the foundation for the development plan.[Brainstorming](https://github.com/TasniaSanta/Resturant_project/blob/main/DDD/BrainstormingFirststep.png)
2. I recorded the key domain concepts, aiming for a deep understanding. This helped me to make a better decision.[Domain_concepts](https://github.com/TasniaSanta/Resturant_project/blob/main/DDD/domainidea.png)
3. After grasping domain ideas, I honed in on developing a 'ubiquitous language'—a common vocabulary that I could easily understand to ensure smooth communication.[ubiquitous language](https://github.com/TasniaSanta/Resturant_project/blob/main/DDD/domainUbiquitous%20Language.png)
4. After gathering ideas, I sketched out a context map a visual roadmap outlining key content and its relationships.[ContexMapping](https://github.com/TasniaSanta/Resturant_project/blob/main/DDD/ContexMapping.png)
5. And finally Core domain chart.[CoreDomainChart](https://github.com/TasniaSanta/Resturant_project/blob/main/DDD/CoreDomainChart.png)

# 4. Metrics
<img src="https://github.com/TasniaSanta/Resturant_project/blob/main/photo/article-SonarCloud-Analysez-votre-projet-GitHub-via-VSTS.jpg" alt="alt text" width="200"/>

I have used the sonar cloud to maintain and analyze code quality

<!--[![Click me](https://github.com/TasniaSanta/Resturant_project/blob/main/photo/Sonercloud.png)](https://sonarcloud.io/summary/overall?id=TasniaSanta_Resturant_project)-->
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

**Duplication:** Avoiding duplication, by creating reusable functions, modules, or libraries. As one can see by the sonar cloud metrics duplication is 0%[Duplications](https://sonarcloud.io/component_measures?id=TasniaSanta_Resturant_project&metric=duplicated_lines_density&view=list)

**Unittest:** There is a also comprehensive unit test[Unittest](https://github.com/TasniaSanta/Resturant_project/blob/main/test_system.py)

**Modularity:** The codes written are broken down into smaller ones, Use indentation, spacing, and line breaks to improve the code quality.[Check_here](https://github.com/TasniaSanta/Resturant_project/blob/main/system.py#217)

# 6. & 7. Build and CI/CD
<img src="https://github.com/TasniaSanta/Resturant_project/blob/main/photo/44036562.png" alt="alt text" width="150"/>

For me, points 6 and 7 are integrated. I have used GitHub action for the build and Continuous Integration/Continuous Deployment. As my project is in Python, hence I have used GitHub action.it is possible to use build management systems such as Ant, Maven, and Gradle for Python projects, although they are more commonly associated with Java projects. While these tools are primarily designed for managing Java projects and dependencies, they can be adapted to work with Python projects with some additional configuration.so I decided to work with GitHub Action.

**Build:** The pipeline builds our project, compiling source code, bundling assets, and generating artifacts for deployment. [Build](https://github.com/TasniaSanta/Resturant_project/blob/main/photo/build.png)

**Test:** Unit tests and integration tests are executed to ensure the quality and reliability of the codebase. Any failures during testing will halt the pipeline. After putting in a lot of effort and trying multiple times, I finally succeeded in passing this test. It took quite a bit of time and determination, but I didn't give up, and in the end, I was able to achieve my goal.[Test](https://github.com/TasniaSanta/Resturant_project/actions/runs/8474537710/job/23221096526)

GitHub Actions is a powerful automation tool provided by GitHub that enables Continuous Integration (CI) and Continuous Deployment (CD) pipelines directly within your GitHub repository
I define my CI/CD pipeline using a YAML-based configuration file called a workflow file. This file resides in the .github/workflows directory of my GitHub repository.[.yml](https://github.com/TasniaSanta/Resturant_project/blob/main/.github/workflows/python-app.yml)file



# 8. UnitTest
I have imported a unit test module for unit testing. I have written three unit tests based on the calculator function

**test_btn_click:**
- This test checks the functionality of the btn_click function.
- It simulates clicking a button with the number 7.
- It asserts that after clicking the button, the text_Input.set method is called once with the current input text concatenated with "7".

**test_btn_clear:**
- This test checks the functionality of the btn_clear function.
- It simulates clicking a clear button.
- It asserts that after clicking the clear button, the text_Input.set method is called once with an empty string.

**test_btn_equals:**
- This test checks the functionality of the btn_equals function.
- It mocks the return value of the get method to simulate the input "3+5".
- It triggers the btn_equals function.
-It asserts that after clicking the equals button, the text_Input.set method is called once with the result of the expression "3+5", which is "8".

These unit tests ensure that the calculator functions (btn_click, btn_clear, and btn_equals) behave as expected when invoked with certain inputs or actions. By verifying these behaviors, I can ensure the correctness and reliability of the calculator application. The results of the unit tests for the functions calculator application [Result](https://github.com/TasniaSanta/Resturant_project/blob/main/photo/unittest_screenshot.png)

Here is [Unittest](https://github.com/TasniaSanta/Resturant_project/blob/main/test_system.py) file


# 9. IDE
I choose Visual Studio as an IDE for this Project. I choose Visual Studio for coding for several reasons. Visual Studio provides a comprehensive set of features and tools for software development, including code editing, debugging, testing, version control integration, and more. It supports a wide range of programming languages, frameworks, and platforms

some of My Favorite Shortcut tools are:

**1) ctrl + L:** It allows me to clear the output console

**2) Alt+Click :** It Inserts a cursor

**3) Ctrl+Shift+N:** It opens a new window/instance

**4) Ctrl+Shift+W :** It Close window/instance

**5) Ctrl + Shift + K:** for deleting the current line.

**6)Ctrl + Shift + T:** for navigating to a test.

# 10. DSL

my [DSL.py](https://github.com/TasniaSanta/Resturant_project/blob/main/DSL.py) file defines a Domain-Specific Language (DSL) for managing a menu and orders.

It consists of three main classes:
- MenuItem
- Order and
- MenuDSL.

MenuItem represents items on the menu with options, Order represents customer orders, and MenuDSL acts as a DSL for creating menu items, orders and displaying the menu. The DSL allows for defining menu items with options and creating orders with specific items and options.
Final Data Structures:

# 11.  Functional Programming

To cover all the mentioned functional programming aspects, I have written a small Python program. The Link for the complete program can be found at [functional_programming.py](https://github.com/TasniaSanta/Resturant_project/blob/main/functional_programming.py)

**Final Data Structures:** The drinks_dict and cakes_dict hold the final data regarding available drinks and cakes, respectively.

**Side-effect-free Functions:** The calculate_costs function calculates costs based on the input parameters and returns the result without modifying any global state.

**Higher-order Functions:** The apply_discount function is a higher-order function that returns a function (discount) that applies a discount to the total cost.

**Functions as Parameters and Return Values:** The apply_discount function takes discount_rate as a parameter and returns another function (discount) as a result.

**Closures / Anonymous Functions:** The discount function returned by apply_discount is a closure, as it captures the discount_rate parameter from the enclosing scope.












