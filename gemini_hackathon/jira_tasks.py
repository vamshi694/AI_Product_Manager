from jira import JIRA
from dotenv import load_dotenv
import os

load_dotenv(".env")

jiraOptions = {'server' : "https://hackathon-projects.atlassian.net"}
jira = JIRA(options=jiraOptions, basic_auth=(os.getenv("JIRA_EMAIL_ID"), os.getenv("JIRA_API")))


def create_jira_epic(project_name, epic_name, epic_description):
    epic_fields = {
                    "project": {"key": project_name},
                    "issuetype": {"name": "Epic"},
                    "summary": epic_name,
                    "description": epic_description,
                }
    new_epic = jira.create_issue(fields = epic_fields)
    return f"{new_epic.key}"


def create_jira_user_story(project_name, epic_key, user_stories = []):
    epic_key = epic_key
    issue_ids = []
    for each_story in user_stories:
        issue_dict = {
            'project': {'key': project_name},  
            'summary': each_story["user_story_name"],  
            'description': each_story["user_story_description"],
            'issuetype': {'name': 'Task'},  
            'parent': {'key': epic_key}
        }
        new_issue = jira.create_issue(issue_dict)
        issue_ids.append(new_issue.id)
    return f"User stories created {issue_ids}"