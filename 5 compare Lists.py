def compare_lists(list_one, list_two):
    if list_one == list_two:
        print "Lists are same"
    else:
        print "Lists not same"

list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]

compare_lists(list_one, list_two)

list_one = [1,2,5,6,5]
list_two = [1,2,5,6,5,3]

compare_lists(list_one, list_two)

list_one = [1,2,5,6,5,16]
list_two = [1,2,5,6,5]


compare_lists(list_one, list_two)

list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']

compare_lists(list_one, list_two)
