
[jira_service_desk]
python.version = python3
param.jira_issue_type = <string> Issue type. It's a required parameter.
param.jira_labels = <string> Labels.
param.jira_assignee = <string> Jira assignee.
param.jira_description = <string> Description.
param.jira_summary = <string> Summary. It's a required parameter.
param._cam = <json> Active response parameters.
param.jira_priority = <string> Priority. It's a required parameter.
param.jira_priority_dynamic = <string> Priority override from results, optional.
param.jira_project = <list> Project. It's a required parameter.
param.customfield_15333 = <string> Source IP(s).
param.customfield_15332 = <string> Machine Name(s).
param.customfield_15335 = <string> Affected User(s).
param.customfield_15334 = <string> Destination IP(s).
param.customfield_15639 = <string> Detection Time (Time Example(UTC):"2018-10-15T09:56:00.000-0700").
param.customfield_16402 = <string> Containment Time.
param.customfield_16404 = <string> Eradication Time.
param.customfield_16406 = <string> Jira Hash.
param.customfield_16407 = <list> Handled by Automation.
param.customfield_16408 = <list> Is MSSP.
param.customfield_14857 = <list> SIEM.
param.customfield_16310 = <list> Kill Chain.
param.customfield_15048 = <list> Zone.
param.customfield_15052 = <string> IOC IP(s).
param.customfield_15050 = <string> IOC Hash(es).
param.customfield_15051 = <string> IOC URL(s).
param.customfield_12207 = <string> Remedy Ticket.
param.customfield_14583 = <string> Ethics Point ID.
param.customfield_16403 = <list> Is Malicious.
param.customfield_15203 = <string> IOC Email(s).
param.customfield_14504 = <list> SOC-Escalated.
param.customfield_14509 = <list> SOC-BU2.
param.customfield_15020 = <list> Incident Category.
param.customfield_15027 = <list> Region(s).
param.customfield_15025 = <list> CTI Source.

[jira_service_desk_replay]
python.version = python3
param.ticket_uuid = <string> UUID value stored in the KVstore.
param.ticket_data = <string> JSON object stored in the KVstore.
param.ticket_status = <string> Status stored in the KVstore.
param.ticket_no_attempts = <string> Number of attempts stored in the KVstore.
param.ticket_max_attempts = <string> Maximal number of attempts.
param.ticket_ctime = <string> Creation time stored in the KVstore.
param.ticket_mtime = <string> Modification time stored in the KVstore.
