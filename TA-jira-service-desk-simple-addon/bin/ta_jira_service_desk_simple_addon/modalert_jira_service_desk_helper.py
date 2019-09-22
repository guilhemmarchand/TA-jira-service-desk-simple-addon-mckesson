# encoding = utf-8

def process_event(helper, *args, **kwargs):
    """
    # IMPORTANT
    # Do not remove the anchor macro:start and macro:end lines.
    # These lines are used to generate sample code. If they are
    # removed, the sample code will not be updated when configurations
    # are updated.

    [sample_code_macro:start]

    # The following example gets and sets the log level
    helper.set_log_level(helper.log_level)

    # The following example gets the setup parameters and prints them to the log
    jira_url = helper.get_global_setting("jira_url")
    helper.log_info("jira_url={}".format(jira_url))
    jira_username = helper.get_global_setting("jira_username")
    helper.log_info("jira_username={}".format(jira_username))
    jira_password = helper.get_global_setting("jira_password")
    helper.log_info("jira_password={}".format(jira_password))
    jira_ssl_certificate_validation = helper.get_global_setting("jira_ssl_certificate_validation")
    helper.log_info("jira_ssl_certificate_validation={}".format(jira_ssl_certificate_validation))

    # The following example gets the alert action parameters and prints them to the log
    jira_project = helper.get_param("jira_project")
    helper.log_info("jira_project={}".format(jira_project))

    jira_issue_type = helper.get_param("jira_issue_type")
    helper.log_info("jira_issue_type={}".format(jira_issue_type))

    jira_priority = helper.get_param("jira_priority")
    helper.log_info("jira_priority={}".format(jira_priority))

    jira_labels = helper.get_param("jira_labels")
    helper.log_info("jira_labels={}".format(jira_labels))

    jira_summary = helper.get_param("jira_summary")
    helper.log_info("jira_summary={}".format(jira_summary))

    jira_description = helper.get_param("jira_description")
    helper.log_info("jira_description={}".format(jira_description))

    jira_custom_fields = helper.get_param("jira_custom_fields")
    helper.log_info("jira_custom_fields={}".format(jira_custom_fields))


    # The following example adds two sample events ("hello", "world")
    # and writes them to Splunk
    # NOTE: Call helper.writeevents() only once after all events
    # have been added
    helper.addevent("hello", sourcetype="sample_sourcetype")
    helper.addevent("world", sourcetype="sample_sourcetype")
    helper.writeevents(index="summary", host="localhost", source="localhost")

    # The following example gets the events that trigger the alert
    events = helper.get_events()
    for event in events:
        helper.log_info("event={}".format(event))

    # helper.settings is a dict that includes environment configuration
    # Example usage: helper.settings["server_uri"]
    helper.log_info("server_uri={}".format(helper.settings["server_uri"]))
    [sample_code_macro:end]
    """

    # TODO: Implement your alert action logic here
    #query the url from setup

    helper.set_log_level(helper.log_level)
    helper.log_info("Alert action jira_service_desk started.")

    # Retrieve JIRA connnection parameters and settings
    jira_url = helper.get_global_setting("jira_url")
    helper.log_debug("jira_url={}".format(jira_url))
    
    jira_username = helper.get_global_setting("jira_username")
    helper.log_debug("jira_username={}".format(jira_username))

    jira_password = helper.get_global_setting("jira_password")
    #helper.log_debug("jira_password={}".format(jira_password))
    
    jira_ssl_certificate_validation = helper.get_global_setting("jira_ssl_certificate_validation")
    if jira_ssl_certificate_validation == 0:
        ssl_certificate_validation = False
    elif jira_ssl_certificate_validation == 1:
        ssl_certificate_validation = True
    else:
        ssl_certificate_validation = True

    helper.log_debug("jira_ssl_certificate_validation={}".format(ssl_certificate_validation))

    #call the query URL REST Endpoint and pass the url and API token
    content = query_url(helper, jira_url, jira_username, jira_password, ssl_certificate_validation)  

    #write the response returned by Virus Total API to splunk index
    #helper.addevent(content, sourcetype="VirusTotal")
    #helper.writeevents(index="main", host="localhost", source="VirusTotal")    

    # Retrieve parameters
    jira_project = helper.get_param("jira_project")
    jira_issue_type = helper.get_param("jira_issue_type")
    jira_priority = helper.get_param("jira_priority")
    jira_summary = helper.get_param("jira_summary")
    jira_description = helper.get_param("jira_description")
    jira_custom_fields = helper.get_param("jira_custom_fields")

    return 0
    
def query_url(helper, jira_url, jira_username, jira_password, ssl_certificate_validation):
    
    import requests
    import json

    # Build the jira_url    
    jira_url = jira_url + '/rest/api/2/issue'

    # Retrieve parameters
    jira_project = helper.get_param("jira_project")
    helper.log_debug("jira_project={}".format(jira_project))

    jira_issue_type = helper.get_param("jira_issue_type")
    helper.log_debug("jira_issue_type={}".format(jira_issue_type))

    jira_priority = helper.get_param("jira_priority")
    helper.log_debug("jira_priority={}".format(jira_priority))

    jira_summary = helper.get_param("jira_summary")
    helper.log_debug("jira_summary={}".format(jira_summary))

    jira_description = helper.get_param("jira_description")
    # Manage line breaks
    jira_description = jira_description.replace("\n","\\n")
    helper.log_debug("jira_description={}".format(jira_description))

    jira_labels = helper.get_param("jira_labels")
    helper.log_debug("jira_labels={}".format(jira_labels))

    # Retrieve the custom fields
    customfield_16408 = helper.get_param("customfield_16408")
    helper.log_debug("customfield_16408={}".format(customfield_16408))

    customfield_15050 = helper.get_param("customfield_15050")
    helper.log_debug("customfield_15050={}".format(customfield_15050))

    customfield_15051 = helper.get_param("customfield_15051")
    helper.log_debug("customfield_15051={}".format(customfield_15051))

    customfield_15020 = helper.get_param("customfield_15020")
    helper.log_debug("customfield_15020={}".format(customfield_15020))

    customfield_15334 = helper.get_param("customfield_15334")
    helper.log_debug("customfield_15334={}".format(customfield_15334))

    customfield_12207 = helper.get_param("customfield_12207")
    helper.log_debug("customfield_12207={}".format(customfield_12207))

    customfield_15052 = helper.get_param("customfield_15052")
    helper.log_debug("customfield_15052={}".format(customfield_15052))

    customfield_14509 = helper.get_param("customfield_14509")
    helper.log_debug("customfield_14509={}".format(customfield_14509))

    customfield_16403 = helper.get_param("customfield_16403")
    helper.log_debug("customfield_16403={}".format(customfield_16403))

    customfield_16310 = helper.get_param("customfield_16310")
    helper.log_debug("customfield_16310={}".format(customfield_16310))

    customfield_15048 = helper.get_param("customfield_15048")
    helper.log_debug("customfield_15048={}".format(customfield_15048))

    customfield_15203 = helper.get_param("customfield_15203")
    helper.log_debug("customfield_15203={}".format(customfield_15203))

    customfield_15639 = helper.get_param("customfield_15639")
    helper.log_debug("customfield_15639={}".format(customfield_15639))

    customfield_15025 = helper.get_param("customfield_15025")
    helper.log_debug("customfield_15025={}".format(customfield_15025))

    customfield_15335 = helper.get_param("customfield_15335")
    helper.log_debug("customfield_15335={}".format(customfield_15335))

    customfield_14504 = helper.get_param("customfield_14504")
    helper.log_debug("customfield_14504={}".format(customfield_14504))

    customfield_14583 = helper.get_param("customfield_14583")
    helper.log_debug("customfield_14583={}".format(customfield_14583))

    customfield_15333 = helper.get_param("customfield_15333")
    helper.log_debug("customfield_15333={}".format(customfield_15333))

    customfield_14857 = helper.get_param("customfield_14857")
    helper.log_debug("customfield_14857={}".format(customfield_14857))

    customfield_16402 = helper.get_param("customfield_16402")
    helper.log_debug("customfield_16402={}".format(customfield_16402))

    customfield_15332 = helper.get_param("customfield_15332")
    helper.log_debug("customfield_15332={}".format(customfield_15332))

    customfield_15027 = helper.get_param("customfield_15027")
    helper.log_debug("customfield_15027={}".format(customfield_15027))

    customfield_16404 = helper.get_param("customfield_16404")
    helper.log_debug("customfield_16404={}".format(customfield_16404))

    customfield_16406 = helper.get_param("customfield_16406")
    helper.log_debug("customfield_16406={}".format(customfield_16406))

    customfield_16407 = helper.get_param("customfield_16407")
    helper.log_debug("customfield_16407={}".format(customfield_16407))    

    headers = {
        'Content-Type': 'application/json',
    }
    
    # Manage custom fields properly
    data = '{\n' + '"fields": {\n' + '"project":\n {\n"key": "' + jira_project + '"' + '\n },\n"summary": "' + jira_summary + '",\n"description": "' + jira_description + '",\n"issuetype": {\n"name": "' + jira_issue_type + '"\n}'

    if jira_labels not in ["", "None", None]:
        jira_labels = jira_labels.split(",")
        altered = map(lambda x: '\"%s\"' % x, jira_labels)
        jira_labels = " [ "+",".join(altered) + " ]"
        data = data + ',\n "labels" :' + jira_labels

    if customfield_16408 not in ["", "None", None]:
        if customfield_16408 == "1":
            customfield_16408 = "Yes"
        data = data + ',\n "customfield_16408" : [ { "value": "' + customfield_16408 + '"}]'

    if customfield_15050 not in ["", "None", None]:
        data = data + ',\n "customfield_15050" : "' + customfield_15050 + '"'

    if customfield_15051 not in ["", "None", None]:
        data = data + ',\n "customfield_15051" : "' + customfield_15051 + '"'

    if customfield_15020 not in ["", "None", None]:
        data = data + ',\n "customfield_15020" : [ { "value": "' + customfield_15020 + '"}]'

    if customfield_15334 not in ["", "None", None]:
        data = data + ',\n "customfield_15334" : "' + customfield_15334 + '"'

    if customfield_12207 not in ["", "None", None]:
        data = data + ',\n "customfield_12207" : "' + customfield_12207 + '"'

    if customfield_15052 not in ["", "None", None]:
        data = data + ',\n "customfield_15052" : "' + customfield_15052 + '"'

    if customfield_14509 not in ["", "None", None]:
        data = data + ',\n "customfield_14509" : [ { "value": "' + customfield_14509 + '"}]'

    if customfield_16403 not in ["", "None", None]:
        if customfield_16403 == "1":
            customfield_16403 = "Yes"
        data = data + ',\n "customfield_16403" : [ { "value": "' + customfield_16403 + '"}]'

    if customfield_16310 not in ["", "None", None]:
        data = data + ',\n "customfield_16310" : { "value": "' + customfield_16310 + '"}'

    if customfield_15048 not in ["", "None", None]:
        data = data + ',\n "customfield_15048" : { "value": "' + customfield_15048 + '"}'

    if customfield_15203 not in ["", "None", None]:
        data = data + ',\n "customfield_15203" : "' + customfield_15203 + '"'

    if customfield_15639 not in ["", "None", None]:
        data = data + ',\n "customfield_15639" : "' + customfield_15639 + '"'

    if customfield_15025 not in ["", "None", None]:
        data = data + ',\n "customfield_15025" : [ { "value": "' + customfield_15025 + '"}]'

    if customfield_15335 not in ["", "None", None]:
        data = data + ',\n "customfield_15335" : "' + customfield_15335 + '"'

    if customfield_14504 not in ["", "None", None]:
        if customfield_14504 == "0":
            customfield_14504 = "False"
        elif customfield_14504 == "1":
            customfield_14504 = "True"
        data = data + ',\n "customfield_14504" : { "value": "' + customfield_14504 + '"}'

    if customfield_14583 not in ["", "None", None]:
        data = data + ',\n "customfield_14583" : "' + customfield_14583 + '"'

    if customfield_15333 not in ["", "None", None]:
        data = data + ',\n "customfield_15333" : "' + customfield_15333 + '"'

    if customfield_14857 not in ["", "None", None]:
        data = data + ',\n "customfield_14857" : [ { "value": "' + customfield_14857 + '"}]'

    if customfield_16402 not in ["", "None", None]:
        data = data + ',\n "customfield_16402" : "' + customfield_16402 + '"'

    if customfield_15332 not in ["", "None", None]:
        data = data + ',\n "customfield_15332" : "' + customfield_15332 + '"'

    if customfield_15027 not in ["", "None", None]:
        data = data + ',\n "customfield_15027" : [ { "value": "' + customfield_15027 + '"}]'

    if customfield_16404 not in ["", "None", None]:
        data = data + ',\n "customfield_16404" : "' + customfield_16404 + '"'

    if customfield_16406 not in ["", "None", None]:
        data = data + ',\n "customfield_16406" : "' + customfield_16406 + '"'

    if customfield_16407 not in ["", "None", None]:
        if customfield_16407 == "1":
            customfield_16407 = "Yes"
        data = data + ',\n "customfield_16407" : [ { "value": "' + customfield_16407 + '"}]'

    # Finally close
    data = data + '\n}\n}'

    # Pretty print json
    data = json.dumps(json.loads(data), indent=4)

    helper.log_debug("json data for final rest call:={}".format(data)) 

    response = requests.post(jira_url, headers=headers, data=data, auth=(jira_username, jira_password), verify=ssl_certificate_validation)
    
    if  response.status_code not in (200, 201, 204):
        helper.log_error('JIRA Service Desk ticket creation has failed!. url={}, HTTP Error={}, content={}'.format( jira_url, response.status_code, response.text))
        return 0
    else:

        helper.log_info('JIRA Service Desk ticket successfully created. {}, content={}'.format(jira_url, response.text))
        return response.text    
    