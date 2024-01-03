import re

def remove_strings_by_index(collection, first_index_to_remove, last_index_to_remove):

    if first_index_to_remove < 0 or last_index_to_remove > len(collection) - 1:
        return

    del collection[first_index_to_remove:last_index_to_remove+1]
    
def remove_header_information(jira_burndown_list, string_indicator_for_useful_data = "Sprint started by"):

    startingIndexForBurndownData = 0

    for i in range(len(jira_burndown_list)):
        if jira_burndown_list[i].startswith(string_indicator_for_useful_data):
            startingIndexForBurndownData = i + 1 # would like to remove "Sprint started by" as well
            break
    
    remove_strings_by_index(jira_burndown_list, 0, startingIndexForBurndownData - 1)

    return jira_burndown_list

def contains_number(string):
    return bool(re.search(r'^\d+(\.\d+)?$', string))

# This function will return the committed story points for the sprint
# It will stop when it does not find any other numbers in the collection.
def get_committed_story_points(collection):
    
    committed_story_points = 0
    no_more_numbers = False

    for item in collection:

        if contains_number(item):
            committed_story_points += int(item)
        else:
            no_more_numbers = True

        if no_more_numbers:
            break
        
    return committed_story_points

def set_story_point_commitment(collection, story_point_commitment):

    if len(collection) == 0:
        return
    
    collection[0] = f"{collection[0]}, {story_point_commitment}"