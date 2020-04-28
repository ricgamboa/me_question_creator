# Used only to test the function

import me_question_creator_pkg

qid = input("Enter the question global id: ")
n_letter = input("Enter number letters in the question: ")
me_question_creator_pkg.me_question_create(int(qid), int(n_letter))