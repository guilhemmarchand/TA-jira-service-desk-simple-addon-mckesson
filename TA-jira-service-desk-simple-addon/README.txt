# JIRA Service Desk simple addon

## Instructions:

- Deploy the add-on to any search head that needs to be able to create JIRA issues.

- Once the add-on has been deployed and the search head restarted, enter the configuration page of the addon

- Fill in the JIRA instance information, the URL to be entered will be automatically substituted with https://<URL>

## release notes:

Version 1.0.2:

- Initial version submitted for Splunk Cloud certification

Version 1.0.3:

- Various improvements

Version 1.0.4:

- Enforces https for Splunk Cloud app certification purposes

Version 1.0.5:

- Fix: avoid JIRA ticket creation failures if values contain double quotes such as in the issue description which allows free text from users.

Version 1.0.6:

- Fix: priority field is not being sent properly as part of the json data
- Fix: enable alert throttle by default

Version 1.0.7:

- Fix: Wrong label in lookup
