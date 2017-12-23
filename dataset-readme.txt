
Comments:
* Employees interests can change over time.
* Scenarios are plentiful in this dataset, so finding 1 interesting “thing” would be the absolute minimum.



logon.csv
* Fields: id, date, user, pc, activity (Logon/Logoff)
* some logons have been removed from the dataset, to mimic a “messy” scenario
* Each user has an assigned machine, but can share others
* 100 machines shared (physically shared) by some of the users in addition to their assigned PC. 
* Some logons occur after-hours 
*Note: Screen unlocks are recorded as logons. Screen locks are not recorded.


device.csv
* Fields: id, date, user, pc, activity (connect/disconnect)
* Some users use a portable zip drive
* Some connect(s) may be missing disconnect(s), since machine may be turned off without a proper disconnect. 


http.csv
* Fields: id, date, user, pc, url, content
* content has a set of key words which relate to the site.
* Per-usual, webpages can have multiple topics
* Websites have been randomly generated, some may be real sites, others not. Exercise care when visiting websites. 


email.csv
* Fields: id, date, user, pc, to, cc, bcc, from, size, attachment_count, content
* Per usual,emails can have multiple recipients
* Emails can be sent to non-employees. The company name is randomly initialized DTAA (there isn’t any significance here), and can be used to identify other employees.
* Email size is in bytes, not including any possible attachments.
* Emails have carbon copy info.
* Per usual- content and subjects may not match 


file.csv
Fields: id, date, user, pc, filename, content
* Each item represents an item copied to a thumb-drive
* Files are summarized by keywords of the “content”


psychometric.csv
* Fields: employee_name, user_id, O, C, E, A, N
* Big 5 psychometric score
* OCEAN describes the Big-5 personality traits. You’ll want to examine extraneous materials to understand the significance of each personality type.


