# ranelagh-time-keeping
Test deployment for a barcode and timing service based on my assumption of how parkrun timing works.
The parkrun app records positions and time. These are correlated with a barcode against a central user database.
I have simulated this with a dynamodb table pre-populated with users, with a unique id (bardcode).
The results.csv contains the id, time and position.
When the results.csv file is uploaded to the results s3 bucket, it triggers a lambda which ingests the rsults into Athena, lookign up the user name from the dynamodb table.
The results are processed and published dynmaically by a javascript/html web front end which sits behind cloudfront, and API gateway.
