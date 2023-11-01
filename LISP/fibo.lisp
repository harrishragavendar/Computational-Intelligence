(
    defun fibo (n)
    (cond
        ((<= n 1) n)
        (t (+ (fibo (- n 1)) (fibo (- n 2))))
    )
)