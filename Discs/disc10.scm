;;scheme;;
;;scheme;;

;1.3
(define (naturals n)
  (cons-stream n (naturals (+ n 1))))

(define nat (naturals 0))

(define (map-stream f s)
  (cons-stream (f (car s)) (map-stream f (cdr-stream s))))

(define evens (map-stream (lambda (x) (* x 2)) nat))

;1.4


