(define (repeatedly-cube n x)
    (if (zero? n)
        x
        (let ((y x))
	  (repeatedly-cube (- n 1) (* y y y)))))

(define-macro (def func bindings body)
    `(define ,(cons func bindings) ,body))



