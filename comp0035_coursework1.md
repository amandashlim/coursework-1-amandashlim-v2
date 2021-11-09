# Coursework 1

## Technical information
### Repository URL
[Repository](https://github.com/amandashlim/coursework-1-amandashlim-v2/blob/master/comp0035_coursework1.md)

## Selection of project methodology
### Methodology (or combination) selected
Scrum Methodology

![image](https://scrumorg-website-prod.s3.amazonaws.com/drupal/inline-images/2021-01/scrumorg-scrum-framework-3000.png)

### Selection criteria and justification of selection
#### Hypothetical Project Scenario
This project using the borough tree list dataset (referred to as “trees dataset” throughout this repo) involves a group of 4-5 UCL students with some data science/computer science experience who would create a dashboarding web app for The London City Hall. The web app would include multiple dashboards to manage the planting and maintenance of London Borough trees (further explanation under “Definition of Business Need”). 

#### Selection Criteria & Justification of Selection
Given this scenario, one can compare the commonly used methodologies in a table.

![image](https://drive.google.com/uc?export=view&id=1MeLmq0VznjCEH2e0xEkawLzl5SROVWPi)
_NOTE: Image rather than markdown used for coloured background cells since CSS not allowed on GitHub_

I decided to select the **scrum methodology** for my project based on the above selection criteria and prior experience using it in my Summer internship at Deutsche Bank. Furthermore, I am familiar with technologies used to manage development projects that use an agile approach. Using Jira (ticket task manager) and Bitbucket (like GitHub) allows the sprint tasks to be displayed to all team members, categorized, and even linked to specific branches, commits, builds, etc.

![image](https://atlassianblog.wpengine.com/wp-content/uploads/2017/12/create-branch-in-jira-blog.png)

#### Potential Concerns
Some potential concerns with the agile methodology is that it is difficult to catch up on tasks once the sprint is over. In my experience at DB, there were often times where tickets would get lost in the backlog while team members had to move onto the next sprint. Since my team at DB was bigger and we were managing multiple different projects, we could not afford for all team members to stay behind a sprint in this case. Having time constraints for each sprint poses the concern that the project may get disorganized if team members are not able to complete all their tasks in time. Despite this, I still think that the frequent check-ins that the agile approach allows is best for managing a development project around university students’ lives. Furthermore, it is possible that all team members could stay behind a couple days before starting the next sprint as we would all be working on the same project with the same deadline.

## Definition of the business need
### Problem definition
#### Clients
London City Hall & the London Urban Forest Partnership

#### Context
The Mayor of London, Sadiq Khan, has led various grants to help increase greenery and canopy cover in London. Some examples include the £12 billion Greener City fund, which funded tree planting, green infrastructure projects, creating urban forests, and community engagement projects to take place from 2016-2021, as well as the similar but smaller scale £1.2 million Grow Back Greener fund (src) and £4 million Green and Resilient Spaces fund (src) for projects taking place from 2022-2024. These grants are part of the Mayor’s London Environment Strategy to increase tree canopy cover to over 50% by 2050 (src) as “trees and woodlands make London a healthier, more attractive place to live, and help combat climate change and air pollution”(src). Currently, the London City Hall works with a network of organizations, called the London Urban Forest Partnership, that protect and manage the trees in London boroughs. 

The London City Hall’s current method of planting trees is a combination of grant projects and government-funded street trees. Organizations in the London Urban Forest Partnership are responsible for maintaining these trees after they are planted. Tree maintenance (e.g. trimming and pruning) depend on the tree’s age, distance from property, species, health, and other environmental factors (src). For instance, younger trees need pruning every 2-3 years to encourage proper growth and extend lifetime while mature trees only need it every 3-5 years (src). Currently, each London borough has its own maintenance team and spends time, money, and infrastructure to come up with an optimal approach to tree maintenance in their own borough. 

#### Problem Statement
Tree planting and maintenance budgets are “often an easy target at times of financial pressure” (src). This is an inhibiting factor to London Mayor Sa​diq Khan’s goal to increase the amount of greenery in London by 2050. A potential solution to this issue would be to invest in a centralized, optimized, data-driven tree planting and maintenance web service provided to all London boroughs, which would decrease marginal costs in the long run and improve efficiency of tree maintenance. 

#### Benefits of the Project
Since the data on the trees in London boroughs is already centralized, the London City Hall can provide a web-app-as-a-service to its partners in the London Urban Forest Partnership that would eliminate the need for borough-specific data analysis and strategy teams. Instead of each borough individually managing when and where to send its routine maintenance and health checkup teams, the web app can provide automated suggestions to indicate what services are needed based on tree age and species.

#### Limitations & Potential Extensions of the Project
Since the London Borough tree data is updated annually, and only includes descriptive data about the trees, maintenance needed on a case-by-case basis, such as fallen branches, fallen trees, branches blocking residential windows, pest outbreaks, etc. cannot be managed by this centralized system. However, since one of the Mayor’s goals in the London Greener City fund was to increase the amount of data collected about the trees in London (src), a potential extension of this project could be a feature in the web-app for the community to report tree maintenance requests and for those to be added into the recommendation system/scheduling aspect. 

### Target audience
The target audience for this service would be the upper-management of the London Urban Forest Partnership organizations, such as Molly the Manager as described in the persona below.

![image](https://drive.google.com/uc?export=view&id=1p16MqGaY1RYbI22Mi02b6ulL59hG0ysT)

_Note: While the London City Hall is listed as a client, there is no persona as the service would be made for the London City Hall to provide to the partner organizations. Therefore, they are not actually using the service themselves but still do benefit monetarily from reduced costs._ 

### Questions to be answered using the dataset
- What is the distribution of the different species of trees?
- What is the distribution of the different ages of trees?
- According to their species and age, what trees are likely to wilt/die soon?
- Aesthetics aside, having the same type of tree planted in the same area (e.g. as street trees could lead to more optimized trips since, if planted at the same time, all the trees in one area in theory would require routine maintenance at the same time. In the areas where new trees could be planted, what species of tree should be planted?
- Where are new trees being planted (geographically)?
- Based on their age and date of planting, when are the trees due for pruning? When are they due for routine health checks?

### Suggested web app
#### Goals of the Project
1. Create a centralized, easy to understand service for upper management of tree planting/maintenance organizations across London boroughs
2. Reduce marginalized costs of tree planting and maintenance services across London boroughs
3. Optimize usage and allocation of resources such as gas, labour, time, trimming/pruning equipment, saplings/seeds, fertilizer, pesticide, etc.


## Data preparation and exploration
### Data preparation

[Data Preparation](data_preparation.py)

### Prepared data set
Please add names of your data set files in this repository below, then delete this instruction text.
[Original data set]()
[Prepared data set]()

### Data exploration

[Data Exploration]()

## Weekly progress reports
Copy and paste from Moodle or use the following structure. Delete this instruction text.

What I did in the last week:
- item
- item

What I plan to do in the next week:
- item
- item

Issues blocking my progress (state ‘None’ if there are no issues):
- item
- item

### Report 1

### Report 2

### Report 3

### Report 4

## References
Use any [referencing style](https://library-guides.ucl.ac.uk/referencing-plagiarism/referencing-styles) that you are
used to using in your course.
