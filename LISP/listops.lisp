; car():This function is used to display the first element in the list

(car '(1 2 3 4 5))

(car '(a b c d e f))

(car '(a 1 b 2 c 3))

; cdr():This function is used to display the list of all elements excluding the first element 

(cdr '(1 2 3 4 5))

(cdr '(a b c d e f))

(cdr '(a 1 b 2 c 3))

; cons():This function inserts the value into first place in the list and returns the new list

(cons 6 '(1 2 3 4 5))

(cons 'g'(a b c d e f))

(cons 0 '(a 1 b 2 c 3))

; append():This function will append the two or more lists.

(append '(a b c d e) '(1 2 3 4 5))

(append '(h e l l o) '( w o r l d))

; last(): This function returns the list that contains the last element in the list

(last '(a b c d e f))

(last '(a 1 b 2 c 3))

(last '(1 2 3 4 5 6))

; member():If the value is present in the list, then it will return the list. 
; Otherwise, NIL is returned.

(member 1 '(1 2 3 4 5))

(member 0 '(1 2 3 4 5))
