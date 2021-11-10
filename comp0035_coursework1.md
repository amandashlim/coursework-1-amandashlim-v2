# Coursework 1

## Technical information
### Repository URL
[Repository](https://github.com/amandashlim/coursework-1-amandashlim-v2/blob/master/comp0035_coursework1.md)

## Selection of project methodology
### Methodology (or combination) selected
Scrum Methodology

![image](https://github.com/amandashlim/coursework-1-amandashlim-v2/blob/fba0ac4b2df012758dc0f263626aeacb7f5dfba7/images/scrum.png)

### Selection criteria and justification of selection
#### Hypothetical Project Scenario
This project using the borough tree list dataset (referred to as “trees dataset” throughout this repo) involves a group of 4-5 UCL students with some data science/computer science experience who would create a dashboarding web app for The London City Hall. The web app would include multiple dashboards to manage the planting and maintenance of London Borough trees (further explanation under “Definition of Business Need”). 

#### Selection Criteria & Justification of Selection
Given this scenario, one can compare the commonly used methodologies in a table.

![image](https://github.com/amandashlim/coursework-1-amandashlim-v2/blob/fba0ac4b2df012758dc0f263626aeacb7f5dfba7/images/methodologies-comparison.png)
_NOTE: Image rather than markdown used for coloured background cells since CSS not allowed on GitHub. Please allow time for images to load._

I decided to select the **scrum methodology** for my project based on the above selection criteria and prior experience using it in my Summer internship at Deutsche Bank. Furthermore, I am familiar with technologies used to manage development projects that use an agile approach. Using Jira (ticket task manager) and Bitbucket (like GitHub) allows the sprint tasks to be displayed to all team members, categorized, and even linked to specific branches, commits, builds, etc.

![image](https://github.com/amandashlim/coursework-1-amandashlim-v2/blob/fba0ac4b2df012758dc0f263626aeacb7f5dfba7/images/jira.png)

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

![image](https://github.com/amandashlim/coursework-1-amandashlim-v2/blob/fba0ac4b2df012758dc0f263626aeacb7f5dfba7/images/persona.png)

_Note: While the London City Hall is listed as a client, there is no persona as the service would be made for the London City Hall to provide to the partner organizations. Therefore, they are not actually using the service themselves but still do benefit monetarily from reduced costs._ 

### Questions to be answered using the dataset
- Based on  their species and age, what trees are likely to wilt/die soon and need to be cut down/arranged to have a new tree planted?
- Based on their age, when are the trees due for pruning?
- When are the trees due for routine health checkups?*

_*This question cannot be directly answered with the data since there is limited information on the health of the trees. However, there is potential for a feature where the web app users can manually enter when the last checkup of each tree was, and for the system to create visualizations that way._ 

### Suggested web app
#### Goals of the Project
1. Create a centralized, easy to understand service for upper management of tree planting/maintenance organizations across London boroughs
2. Reduce marginalized costs of tree planting and maintenance services across London boroughs by eliminating the need for separate data analysis and strategy teams. 
3. Optimize usage and allocation of resources such as gas, labour, time, trimming/pruning equipment, saplings/seeds, fertilizer, pesticide, etc.

#### Similar Web Apps/Inspiration
_Personal Experience – Deutsche Bank_

While it was not a web app, I helped develop an auto-refresh sanctions and embargoes and fraud alert dashboard in Tableau during my internship at Deutsche Bank. The process of receiving the new data, processing it into tables, and visualizing it on a dashboard under different dimensions would be the same for this project’s case with trees. 

_Teaching Dashboard With Schedule_
![image](https://github.com/amandashlim/coursework-1-amandashlim-v2/blob/022e9ebe435eb7ae2e1e2e29f1902a2f4e067a86/images/dashboard_ex1.png)

_Project Management Dashboard_
![image](https://github.com/amandashlim/coursework-1-amandashlim-v2/blob/022e9ebe435eb7ae2e1e2e29f1902a2f4e067a86/images/dashboard_ex2.jpeg)

_Project Status Dashboard_
![image](https://github.com/amandashlim/coursework-1-amandashlim-v2/blob/022e9ebe435eb7ae2e1e2e29f1902a2f4e067a86/images/dashboard_ex3.png)

Functional and non-functional requirements can be defined from this inspiration.

#### Functional Requirements
- Have descriptive dashboard displays to overview the status of the trees in each borough, such as:
  - Map of the ages of trees
  - Map of where trees were planted most recently
  - Pie chart of what species of trees there are and in what proportion
- Have informative dashboard displays such as: 
  - Suggested prune/trim dates of trees
  - Suggested health checkup dates of trees (manual entry)
  - Health of trees (manual entry)
- Create recommended schedules based on suggested prune & health checkup dates
- Create optimized truck route suggestions based on the schedule
- Have the ability to add data manually and have dashboards refresh
- Have the ability to add a task to the schedule directly, for instance if a tree fell down on a house today, that task could be added and the recommended schedule would update.

#### Non-Functional Requirements
- The application must support running on Windows and iOS as these are the most commonly used systems.
- Dashboards must refresh automatically when data refreshes (possible using Tableau API).
- Dashboards must not take longer than 30 minutes to load.
- The application must be easy to understand and use by a non-technical audience. For example, a new task button rather than having to edit the dataset from the backend.

#### Potential Improvements
There is much potential for improvements in the data quality about London borough trees, such as having accurate ages for the trees and exact planting dates down to the month or day. Improvements to this data would enhance the web app even more and further demand for an auto-refresh API.

#### Mockup
A potential mockup of the web app, using visualizations from data exploration where possible.
![image](https://github.com/amandashlim/coursework-1-amandashlim-v2/blob/e0d76887e57ad5c2703269088e21e09a9d7bee72/images/mockup.png)

## Data preparation and exploration
### Data preparation

[Data Preparation](data_preparation.py)

### Prepared data set
- [Original data set](Borough_tree_list_2021July.xlsx)
- [Prepared data set](trees_cleaned.csv)

### Data exploration

[Data Exploration]()

#### Map of London Borough Trees by Species
![image](https://github.com/amandashlim/coursework-1-amandashlim-v2/blob/022e9ebe435eb7ae2e1e2e29f1902a2f4e067a86/images/1_map_by_species.png)

#### Pie Chart of Percentages of Tree Species in London Boroughs
![image](https://github.com/amandashlim/coursework-1-amandashlim-v2/blob/022e9ebe435eb7ae2e1e2e29f1902a2f4e067a86/images/2_pie_by_species.png)

#### Map of London Borough Trees by Age Group
![image](https://github.com/amandashlim/coursework-1-amandashlim-v2/blob/022e9ebe435eb7ae2e1e2e29f1902a2f4e067a86/images/3_map_by_age.png)

#### Count of Trees in London Boroughs by Age Group
![image](https://github.com/amandashlim/coursework-1-amandashlim-v2/blob/022e9ebe435eb7ae2e1e2e29f1902a2f4e067a86/images/4_bar_by_age.png)

#### Count of Trees in London Boroughs Over Time
![image](https://github.com/amandashlim/coursework-1-amandashlim-v2/blob/022e9ebe435eb7ae2e1e2e29f1902a2f4e067a86/images/5_bar_by_time.png)

Graph is limited as we only have the year the trees were entered into the dataset rather than the actual date it was planted. A tree planted Jan 1st is practically a year older than a tree planted December 31st. There is also possibility that the tree was only added to the dataset that year rather than being planted that year. Year 2019 is also missing. 

#### Approximate Prune Dates of Trees in London Boroughs
![image](https://github.com/amandashlim/coursework-1-amandashlim-v2/blob/022e9ebe435eb7ae2e1e2e29f1902a2f4e067a86/images/6_map_by_prune.png)

We assume that the tree is pruned when it was planted/loaded into the dataset. Referenced https://www.ronstreeserviceandfirewood.com/how-often-should-i-have-my-trees-trimmed/ for pruning times by tree age. In practice, there would be further code that would use ML to determine what trees to prune in batches based on their recommended prune date. Limitations are that most of the trees have an unknown age group. Potential solutions would be to use linear regression to predict age  based on trunk diameter, canopy cover, species etc.

## Weekly progress reports
Copy and paste from Moodle or use the following structure. Delete this instruction text.

### Report 1
What I did in the last week:
- Went through the coursework specification
- Opened the dataset
- Set up GitHub, Git, and Pycharm
- Brainstormed initial questions that could be answered with the data 
- Thought of graphs that could be interesting to make.

What I plan to do in the next week:
- Draft problem statement

Issues blocking my progress (state ‘None’ if there are no issues):
- None

### Report 2
What I did in the last week:
- Background research on tree planting and maintenance in London
- Started drafting problem statement

What I plan to do in the next week:
- Finish problem statement

Issues blocking my progress (state ‘None’ if there are no issues):
- Fell sick

### Report 3
What I did in the last week:
- Finished problem statement
- Brainstormed potential persona

What I plan to do in the next week:
- Start preparing my dataset

Issues blocking my progress (state ‘None’ if there are no issues):
- Still sick

### Report 4
What I did in the last week:
- Prepared data
- Finished persona in note form
- Finalized potential questions to answer from the data

What I plan to do in the next week(s):
- Finish coursework 1

Issues blocking my progress (state ‘None’ if there are no issues):
- None

## References

