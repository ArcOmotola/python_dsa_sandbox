import re


def is_valid(key, search_terms, suggestions):
    # Check if key is snake_case and between 3 and 20 characters long
    if not re.match(r'^[a-z_]{3,20}$', key):
        return False
    
    # Check if search_terms is not empty and has no duplicates
    if not search_terms or len(search_terms) != len(set(search_terms)):
        return False
    
    # Check if suggestions is not empty and has no duplicates
    if not suggestions or len(suggestions) != len(set(suggestions)):
        return False
    
    return True
  
  
# ////////////////////////////////////////////////////////////////


def is_valid(key, search_terms, suggestions):
    # Check if key is in snake_case and between 3 and 20 characters long
    if not (3 <= len(key) <= 20):
        return False
    if not all(c.islower() or c == '_' for c in key):
        return False
    if '__' in key or key[0] == '_' or key[-1] == '_':
        return False
    
    # Check if search_terms is not empty and has no duplicates
    if not search_terms or len(search_terms) != len(set(search_terms)):
        return False
    
    # Check if suggestions is not empty and has no duplicates
    if not suggestions or len(suggestions) != len(set(suggestions)):
        return False
    
    return True
  
  
  
  # ////////////////////////////////////////////////////////////////////////
  
#   Part 2: Error Messages
# After completeing the initial validator, your team decides to iterate it further. The team decides it would be useful to also provide users of the internal API feedback when a submitted guideline is invalid. So your second task is to write a function that provides useful error messages for invalid guidelines.

# Tips
# For the purposes of this task, here's what you need to support the following messages:

# "Key must be snake case (lower case letters and underscores)"
# "Key must be between 3 and 20 characters"
# "Search terms must not be empty"
# "Search terms must be unique"
# "Suggestions must not be empty"
# "Suggestions must be unique"
# "Guideline is valid"
# In the case of more than one error please provide errors in alphabetical order.

def messages(key, search_terms, suggestions):
    errors = []

    # Check if key is between 3 and 20 characters long
    if not (3 <= len(key) <= 20):
        errors.append("Key must be between 3 and 20 characters")
    
    # Check if key is snake_case (lower case letters and underscores)
    if not all(c.islower() or c == '_' for c in key) or '__' in key or key[0] == '_' or key[-1] == '_':
        errors.append("Key must be snake case (lower case letters and underscores)")
    
    # Check if search_terms is not empty
    if not search_terms:
        errors.append("Search terms must not be empty")
    
    # Check if search_terms has duplicates
    if len(search_terms) != len(set(search_terms)):
        errors.append("Search terms must be unique")
    
    # Check if suggestions is not empty
    if not suggestions:
        errors.append("Suggestions must not be empty")
    
    # Check if suggestions has duplicates
    if len(suggestions) != len(set(suggestions)):
        errors.append("Suggestions must be unique")
    
    # If no errors, guideline is valid
    if not errors:
        errors.append("Guideline is valid")
    
    return errors

# Examples to test the function
print(messages("man_hours", ["man hours","woman hours"], ["person hours","engineer hours"]))  # ["Guideline is valid"]
print(messages("ManHours", ["man hours","woman hours"], ["person hours","engineer hours"]))  # ["Key must be snake case (lower case letters and underscores)"]
print(messages("key_is_too_long_to_be_valid", ["man hours","woman hours"], ["person hours","engineer hours"]))  # ["Key must be between 3 and 20 characters"]
print(messages("man_hours", ["man hours","woman hours","woman hours"], ["person hours","engineer hours"]))  # ["Search terms must be unique"]



# Part 3: Conflict Detection
# After completeing the initial validator and the message function, your team decides to iterate even further. You point out that the validator could be extended to detect conflicts between guidelines -- for instance if keys are not unique, or search terms for multiple keys return hits.

# Another team member has already written a function to return an array of all the existing guideline keys. And another that returns a flat array of all existing seach terms so you can assume your function will be able to access to that data as input params.

# Your third task is therefore to write a function that takes in the params for a new guideline as well as arrays containing all existing keys and search terms. You should then returns true if the new guideline is conflict free and false if a conflict is detected.

# Tips
# For the purposes of this task, here's what you need to support:

# The key must not already be in the existing_keys
# Each of the search_terms must not already be in the existing_search_terms
# Each of the search_terms must not be a substring of any of the existing_search_terms
# Likewise each of the existing_search_terms must not be a substring of any of the search_terms
# If there aren't any conflicts return true. Otherwise return false.


def unconflicted(key, search_terms, suggestions, existing_keys, existing_search_terms):
  # Check if the key is already in existing_keys
    if key in existing_keys:
        return False
    
    # Check for conflicts with existing search terms
    for term in search_terms:
        # Term should not be in existing_search_terms
        if term in existing_search_terms:
            return False
        # Term should not be a substring of any existing search terms
        for existing_term in existing_search_terms:
            if term in existing_term or existing_term in term:
                return False
    
    return True
  
  
  
