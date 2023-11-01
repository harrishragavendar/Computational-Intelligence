(
    defun square(a)
        (* a a)
)

(
    defun rectangle(a b)
        (* a b)
)

(
    defun circle(r)
        (* pi r r)
)

(
    defun trapezium(a b h)
        (float (/ (* h (+ a b)) 2))
)

(
    defun cube(a)
        (* a a a)
)

(
    defun sphere(r)
        (float(* (/ 4 3) pi r r r))
)

(
    defun parallelogram(b h)
        (* b h)
)