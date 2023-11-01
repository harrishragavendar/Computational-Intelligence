(defun pali(s1)
    (setq s2(reverse s1))

    (if (string-equal s1 s2)
    (format t "~%~d is a palindrome"s1))

    (if (string-not-equal s1 s2)
    (format t "~%~d is not a palindrome"s1))
)