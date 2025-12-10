import time
import pytest
from src.profile_service import get_user_avatar_url


# Helper function to wait for a condition to be true (DO NOT MODIFY)
def wait_for_condition(check_function, timeout=2, interval=0.1):
start_time = time.time()
while time.time() < start_time + timeout:
if check_function():
return True
time.sleep(interval)
return check_function() # Final attempt




def test_user_avatar_url_is_fetched():
user_id = "user_42"


# Trigger delayed background fetch
get_user_avatar_url(user_id)


# YOUR TASK STARTS HERE — implement polling logic
# check = lambda: ...
# result = wait_for_condition(check)
# assert result is True


pass # Remove after implementing
