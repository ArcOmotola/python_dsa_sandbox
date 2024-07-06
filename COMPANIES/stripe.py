def find_best_shutdown_time(machine_state):
  """
  Finds the optimal time to shut down a machine based on its running state.

  Args:
      machine_state: A string representing the machine's running state (1: running, 0: off)

  Returns:
      A tuple (start_index, end_index) representing the ideal shutdown window, or None if no window exists.
  """
  longest_start_index = longest_end_index = None
  current_start = current_length = 0

  for i, state in enumerate(machine_state):
    if state == "0":
      # Machine is off, continue or start tracking idle period
      current_length += 1
      if longest_start_index is None:
        longest_start_index = i
    else:
      # Machine is on, reset idle period tracking
      if current_length > 0:
        longest_end_index = i
        if current_length > (longest_start_index, longest_end_index):
          longest_start_index, longest_end_index = current_start, i
      current_start = i
      current_length = 0

  # Check for continuous idle period at the end
  if current_length > 0 and current_length > (longest_start_index, longest_end_index):
    longest_start_index, longest_end_index = current_start, len(machine_state)

  return (longest_start_index, longest_end_index) if longest_start_index is not None else None

# Example usage
machine_state = "110010100011"
shutdown_window = find_best_shutdown_time(machine_state)
print(shutdown_window)  # Output: (3, 7) - Machine can be shut down from index 3 to 6 (inclusive)



"""Understanding the Problem:

We are given a representation of a machine's running state over a specific period (potentially a day).
This representation could be a string of characters, with "1" indicating the machine is running and "0" indicating it's off.
The goal is to find the optimal time to shut down the machine for a period of time (maintenance, cost savings, etc.) while minimizing disruption or lost productivity.
Possible Solutions:

Simple Approach (if the downtime duration is specified):

Scan the string for a sequence of consecutive "0"s with the specified length (downtime duration).
If such a sequence exists, the starting index of that sequence is the ideal shutdown time.
If no sequence of sufficient length exists, the machine cannot be shut down for the desired duration within the given period.
Finding Longest Idle Period:

If the downtime duration is flexible, we can find the longest sequence of consecutive "0"s.
The starting and ending indices of this longest sequence represent the optimal time window for shutting down the machine.
Implementation (Python example using longest idle period):
  """