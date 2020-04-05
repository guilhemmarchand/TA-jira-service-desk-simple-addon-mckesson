
# encoding = utf-8
# Always put this line at the beginning of this file
import ta_jira_service_desk_simple_addon_declare

import os
import sys

from alert_actions_base import ModularAlertBase
import modalert_jira_service_desk_replay_helper

class AlertActionWorkerjira_service_desk_replay(ModularAlertBase):

    def __init__(self, ta_name, alert_name):
        super(AlertActionWorkerjira_service_desk_replay, self).__init__(ta_name, alert_name)

    def validate_params(self):

        if not self.get_global_setting("jira_url"):
            self.log_error('jira_url is a mandatory setup parameter, but its value is None.')
            return False

        if not self.get_global_setting("jira_username"):
            self.log_error('jira_username is a mandatory setup parameter, but its value is None.')
            return False

        if not self.get_global_setting("jira_password"):
            self.log_error('jira_password is a mandatory setup parameter, but its value is None.')
            return False

        return True

    def process_event(self, *args, **kwargs):
        status = 0
        try:
            if not self.validate_params():
                return 3
            status = modalert_jira_service_desk_replay_helper.process_event(self, *args, **kwargs)
        except (AttributeError, TypeError) as ae:
            self.log_error("Error: {}. Please double check spelling and also verify that a compatible version of Splunk_SA_CIM is installed.".format(ae.message))
            return 4
        except Exception as e:
            msg = "Unexpected error: {}."
            if e.message:
                self.log_error(msg.format(e.message))
            else:
                import traceback
                self.log_error(msg.format(traceback.format_exc()))
            return 5
        return status

if __name__ == "__main__":
    exitcode = AlertActionWorkerjira_service_desk_replay("TA-jira-service-desk-simple-addon", "jira_service_desk_replay").run(sys.argv)
    sys.exit(exitcode)
