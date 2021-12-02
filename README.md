# cardAuditUtility
This script simplifies the process that was being used by student workers in which they had to process 17 different card access reports and manually compile them into a single master excel list. This is done by creating a dictionary with people as keys and their respective info and card access in two lists for the values.

# Examples
This example shows what one card access report looks like and the final master list that is produced by the script.

## Initial Report
| Personnel with Select Clearance including Credential |       |            |         |   |             |         |   | 11/03/2021 12:39:00 |              |       |
|------------------------------------------------------|-------|------------|---------|---|-------------|---------|---|---------------------|--------------|-------|
|                                                      |       |            |         |   |             |         |   |                     |              |       |
| EmplID:                                              | 12345 | Last Name: | Doe     |   | First Name: | John    |   |                     | Card number: | 12345 |
|                                                      |       |            |         |   |             |         |   |                     |              |       |
| EmplID:                                              | 54321 | Last Name: | Doe     |   | First Name: | Jane    |   |                     | Card number: | 54321 |
|                                                      |       |            |         |   |             |         |   |                     |              |       |
| EmplID:                                              | 23415 | Last Name: | Anthony |   | First Name: | Savelle |   |                     | Card number: | 23415 |
|                                                      |       |            |         |   |             |         |   |                     |              |       |
| EmplID:                                              | 13245 | Last Name: | Mon     |   | First Name: | Dave    |   |                     | Card number: | 13245 |

## Final Product
| First Name | Last Name | Employee ID | Card Number | Clearance Group            |
|------------|-----------|-------------|-------------|----------------------------|
| John       | Doe       | 12345       | 12345       | Example Clearance Report_2 |
| John       | Doe       | 12345       | 12345       | Example Clearance Report_3 |
| John       | Doe       | 12345       | 12345       | Example Clearance Report   |
| Jane       | Doe       | 54321       | 54321       | Example Clearance Report_2 |
| Jane       | Doe       | 54321       | 54321       | Example Clearance Report_3 |
| Jane       | Doe       | 54321       | 54321       | Example Clearance Report   |
| Savelle    | Anthony   | 23415       | 23415       | Example Clearance Report_2 |
| Savelle    | Anthony   | 23415       | 23415       | Example Clearance Report_3 |
| Savelle    | Anthony   | 23415       | 23415       | Example Clearance Report   |
| Dave       | Mon       | 13245       | 13245       | Example Clearance Report_2 |
| Dave       | Mon       | 13245       | 13245       | Example Clearance Report_3 |
| Dave       | Mon       | 13245       | 13245       | Example Clearance Report   |
| Santa      | Claus     | 15423       | 15423       | Example Clearance Report_3 |
