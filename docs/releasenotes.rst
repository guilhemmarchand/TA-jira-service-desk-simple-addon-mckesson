Release notes
#############

Version 1.0.0
=============

- initial and first public release

Version 1.0.1
=============

- unpublished

Version 1.0.2
=============

- Feature: Support for Web Proxy
- Feature: Full support for Python 3 (migration to newer Add-on builder libs, embedded custom commands)
- Fix: Support defining the JIRA instance URL with or without https://
- Fix: Potential creation failure with number type custom fields
- Fix: Metadata avoid sharing alerts, reports and views at global level
- Fix: Help block appears right shifted within Enterprise Security correlation search editor, but centered properly in Splunk core alert editor

Version 1.0.3
=============

- Fix Issue #2: Avoids error messages on indexers in distributed mode to report error messages on jirafill and jiragetfields custom commands due to enabled distributed mode
- Fix Issue #2: Avoids error messages reported during execution of jirafill and jiragetfields custom commands related to insecure HTTP calls with urllib3

Version 1.0.4
=============

- Feature: resilient store improvements, catch all failures and exceptions during issue creation attempts
- Fix: minor fix in resilient store table
- Fix: remove redundant alert link in nav bar

Version 1.0.5
=============

- Fix: Provide an embedded role jira_alert_action that can be inherited for non admin users to be allowed to fire the action and work with the resilient store feature

Version 1.0.6
=============

- Change: For Splunk Cloud vetting purposes, explicit Python3 mode in restmap.conf handler

Version 1.0.7
=============

- Fix: Default timed out value during REST calls are too short and might lead to false positive failures and duplicated creation of JIRA issues
