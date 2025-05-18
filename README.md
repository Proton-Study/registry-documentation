# PROTON Registry Documentation
A Documentation for PROTON Registry. <br>
PROTON - Programme for Ocular Inflammation and Infection Translational Research represents the seamless integrated platform of multicentric interdisciplinary collaboration aimed at confronting the complexities of ocular inflammatory and infectious diseases (OIID). By uniting a diverse team of experts from biological, immunological, cellular, and computational sciences, PROTON is dedicated to pioneering research and developing innovative solutions that address the pressing challenges of OIID.
## Screens
A summary of all the main screens in the PROTON Registry, and a description of the features on each screen.

## 1. Dashboard Screen
This screen is the first screen that users see when they log in to the PROTON Registry. It provides a visual overview of the registry's data.
### Screenshot:
![dashboard screen screenshot](/src/images/dashboard.png)

### Features on the screen:
| Feature | Location | Description |
| ---- | ---- | ---- |
| Logo | Top Left Corner | Shows the PROTON Logo, and can be used to quickly navigate back to the dashboard screen. |
| Registry Tab | Top Right Section | Takes you to the actual Patient Registry that the user has created and / or has access to. More details in the [Registry Screen Documentation](#registry-screen). |
| Site Selector | Below PROTON Logo | This is a dropdown list that allows users to choose the site they want to see the data of. Default is 'All'. |
| Dummy Selector | Right of Site Selector | This is a dropdown list that allows users to select whether they want to include Dummy data in the stats they are seeing on the dashboard. Default is 'Exclude Dummy'. |
| Records Count | Below Selectors | This is a set of numbers representing the total records, according to the selections made in the 2 previous selectors. |
| Main Dashboard | Below Records Count | Shows graphs and records based on various features and parameters. |

## 2. Registry Screen
This is the screen that users can use to see the Patient Registry, and see stats, images that have been uploaded, and more for the patients that are registered in the PROTON Registry.

### Screenshot
![registry screen screenshot](/src/images/registry%20screen.png)

### Features on the Screen:
| Feature | Location | Description |
| ---- | ---- | ---- |
| Search Bar | Top Right | Search and filter for records using the Patient Codes |
| Create New Button | Right of Search Bar | Takes user to a new page to create a new Patient Record. Shown in [Action tutorial](#1-create-new-patient-record). |
| Export Button | Right of Create New | Downloads a csv file with all the Patient Records shown |
| EM Button | Right of Export Button | Downloads the medication and doses data of patients in a csv format |
| Patient Record Table | Main Screen Component | Contains the following information in a tabular format: Patient Code, Study Class, Month of Presentation, Gender, Age, Visits, Update Date and Number of Images uploaded |

## Actions

This section describes the various actions that can be performed on the PROTON Registry, and how to perform them.

## 1. Create New Patient Record
This action allows users to create a new patient record in the PROTON Registry.

### Screenshot
![new patient record creation screenshot](/src/images/CreateNewRecord.png)

### Steps to perform the action:
1. Select the 'Site' from the dropdown list. This is the site that the patient that the patient will be registered to.
2. Select the 'Study Type' from the dropdown list. This is the type of study that this patient record will be linked to.
3. Select the 'Category' between 'Prospective' and 'Retrospective'.
4. Click on 'Create' button to create the new patient record.

