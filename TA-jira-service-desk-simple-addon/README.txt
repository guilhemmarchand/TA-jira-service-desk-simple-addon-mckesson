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

Version 1.0.8:

- Feature: Switch to a KVstore based lookup for custom fields

Version 1.0.9:

- Fix: jirafill.py can fail under certain circumstances to retrieve the correct credentials in the credential store

Version 1.0.10:

- Fix: Prevents encoding issue

Version 1.0.11:

- Fix: allow non ascii chars by using strict mode false in json.loads

Version 1.0.12:

- Fix: better exception handling in Python json loads
- Fix: Prevent false positive in OOTB alert

Version 1.0.13:

- Fix: prevents json failure in every field (not only content of the issue to be created)

Version 1.0.14:

- Unpublished: failed appinspect

Version 1.0.15:

- Fix: avoids false positive with transaction command simplification
- Fix: typo in app.conf

Version 1.0.16:

- Feature: provides a priority dynamic text input which will allow to override the JIRA ticket priority based on a field result
