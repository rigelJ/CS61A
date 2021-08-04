; ; scheme ;;
; ; scheme ;;
; ;Tail-Call 
; Example
(define (fact n)
  (if (= n 0)
      1
      (* n fact (-n 1))
  )
)

(define (fact-tail n result)
  (if (= n 0)
      result
      (* n (fact-tail (- n 1) (* n result)))
  )
)

(define (sum lst)
  (define (sumer lster result)
    (if (null? lster)
        result
        (sumer (cdr lster) (+ result (car lster)))
    )
  )
  (sumer lst 0)
)

(define (fib n)
  (define (fib-so-far n1 pre1 pre2)
    (if (= n1 n)
        pre1
        (fib-so-far (+ n1 1) pre2 (+ pre1 pre2))
    )
  )
  (fib-so-far 0 0 1)
)


