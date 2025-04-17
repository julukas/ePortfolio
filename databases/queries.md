# MongoDB Compass Query Examples

Below are several examples of queries and operations performed on the MongoDB database using MongoDB Compass. The collections used include `drugs`, `patients`, and `prescriptions`.

---

### 1. Total Prescriptions per Drug
This aggregation counts the number of times each drug was prescribed.
![Alt Text](./total%20rx%20per%20drug.png)


### 2. Number of Patients on Lisinopril in Connecticut
This lookup joins prescriptions to patients and filters only those from Connecticut.
![Alt Text](./patients%20in%20CT%20on%20lisinopril.png)

### 3. User Creation for Role-Based Access
Users were created with different permissions for RBAC implementation.
![Alt Text](./user%20creation.png)

### 4. Verification of User Access
This displays all created users and their permissions.
![Alt Text](./verification%20of%20user%20access.png)

### 5. Number of Patients per State
This query shows patient distribution by state.
![Alt Text](./number%20of%20patients%20per%20state7:45 PM 4/16/2025.png)

### 6. Total Mentions of Drugs
This shows the amount of times a given drug or device shows up in the database.
![Alt Text](./sorted%20drugs.png)