# Postmortem

Incident Report, also referred to as a Postmortem
The importance of an incident postmortem process
What is an Incident Postmortem?

# Login Problem
on Tuesday between 10:15 and 13:00 on January 23, 2024, our system was down and this lead to authentication error while trying to login in , 
around 80% of our users experienced this issue leading to traffic and delays.

# Timeline
The issue was reported yesterday at the specified time and my team realised this after our system moniter raised error alerts 
due to increased traffic and misconfiguration of our load balancer. My team looked into the login logs to try and solve the issue.

# Root cause and resolution
After doing our investigation we came to realise the error occured due to Increased traffic and a misconfigured load balancer causing
uneven distribution of requests to user authentication servers. My team managed to Correctsettings relating to load balancer and conducted a rollingrestart for seamless implementation.

# Corrective and preventative measures
-Always keep an eye on your servers to ensure they are running properly
-Have extra back-up servers to prevent your program fro completely going offline during an issue
-Implement automated scaling to handle unexpected traffic surges more effectively.
-improve monitoring for load balancer performance and configuration


