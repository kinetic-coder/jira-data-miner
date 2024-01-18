import re
import Utilities.JiraBurndownUtilities as jbu
import Models.BurndownSummaryItemDTO as models
import Utilities.DateUtilities as du

EVENT_DESCRIPTION_POSITION = 3

LINE_TYPE_NONE = 0
LINE_TYPE_BURNDOWN_CHANGE = 1
LINE_TYPE_STORY_POINT = 2
LINE_TYPE_STORY_POINT_RUNNING_TOTAL = 3

def contains_jira_reference(text):
    pattern = r'SBS-\d+'
    match = re.search(pattern, text)
    return match.group(0) if match else None

def remove_strings_by_index(collection, first_index_to_remove, last_index_to_remove):

    if first_index_to_remove < 0 or last_index_to_remove > len(collection) - 1:
        return

    del collection[first_index_to_remove:last_index_to_remove+1]
    
def remove_header_information(jira_burndown_list, string_indicator_for_useful_data = "Sprint started by"):

    startingIndexForBurndownData = 0
    foundFirstBurndownRecord = False

    for i in range(len(jira_burndown_list)):
        if jira_burndown_list[i].startswith(string_indicator_for_useful_data):
            startingIndexForBurndownData = i + 1 # would like to remove "Sprint started by" as well
            foundFirstBurndownRecord = True

        elif foundFirstBurndownRecord == True and du.string_contains_date(jira_burndown_list[i]):
            startingIndexForBurndownData = i
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

# todo: update method to save the story points to the burndown_summary_data_collection
def get_burndown_data_from_file(sprintDatesCollection, jiraBurndownInfo):

    line_type = LINE_TYPE_NONE #1 = date line, 2 = story points, 3 = summary total.

    burndown_summary_data_collection = []

    for jiraBurndownLine in jiraBurndownInfo:

        if du.string_contains_date(jiraBurndownLine):
        
            bsi = models.BurndownSummaryItemDTO(du.get_date_from_string(jiraBurndownLine), get_event_description(jiraBurndownLine))

            line_type = LINE_TYPE_BURNDOWN_CHANGE

        elif contains_jira_reference(jiraBurndownLine):
            bsi = models.BurndownSummaryItemDTO('', get_event_description(jiraBurndownLine))
            line_type = LINE_TYPE_BURNDOWN_CHANGE

        else:
                
            if line_type == LINE_TYPE_BURNDOWN_CHANGE:
                bsi.story_points = get_committed_story_points(jiraBurndownLine)
                line_type = LINE_TYPE_STORY_POINT

            elif line_type == LINE_TYPE_STORY_POINT:
                bsi.running_total = get_committed_story_points(jiraBurndownLine)
                burndown_summary_data_collection.append(bsi)
                line_type = LINE_TYPE_NONE
        
        
                
    return burndown_summary_data_collection

def get_event_description(string_info):

    sections = string_info.split('\t')

    if len(sections) < EVENT_DESCRIPTION_POSITION + 1:
        return ""

    return sections[EVENT_DESCRIPTION_POSITION]