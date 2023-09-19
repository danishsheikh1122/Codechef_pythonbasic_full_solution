total_users,user_not_submitted_any_question,user_who_submitted_and_tried=map(int,input().split())

total_user_submitted=total_users-user_not_submitted_any_question
total_users_solved=total_user_submitted-user_who_submitted_and_tried
print(f"{total_user_submitted} {total_users_solved}")

