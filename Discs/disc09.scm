;; scheme ;;
;; scheme ;;

;;Tail-Call 

(define (fact n)
  (if (= n 0)
      1 
      (* n fact(-n 1))

(define (fact-tail n result)
  (if (= n 0)
      result
      (* n (fact-tail(- n 1)(* n result))

(define (sum lst)
  (define (sumer lster result)
    (if (null?lster)
	result
	(sumer (cdr lster) (+ result (car lster)))))
  (sumer lst 0)
)

(define (fib n)
  (define (fib-now n1 exp1 exp2)
    (if (= n1 n)
	exp1
	(fib-now (- n1 1) exp2 (+ exp1 exp2)))))

;;Macro

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(define-macro (make-lambda expr)
   `(lambda () ,expr)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(define (replicate expr n)
  (if (= n 0)
       nil
       (cons expr (replicate expr (- n 1)))))

(define-macro (repeat-n expr n)
  (cons 'begin (replicate expr n)))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(define-macro (or-macro expr1 expr2)
  `(let ((v1 ,expr1)(v2 ,expr2))
     (if v1
	 v1
	 v2)))


