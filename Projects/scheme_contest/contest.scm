;;; Scheme Recursive Art Contest Entry
;;;
;;; Please do not include your name or personal info in this file.
;;;
;;; Title: <Your title here>
;;;
;;; Description:
;;;   <It's your masterpiece.
;;;    Use these three lines to describe
;;;    its inner meaning.>

(define (draw)
  ; YOUR CODE HERE
    (begin_fill)
  (circle 20)
  (penup)
  (right 90)
  (forward 60)
  (left 90)
  (pendown)
  (circle 20)
  (end_fill)
  (left 90)
  (penup)
  (forward 50)
  (left 90)
  (pendown)
  (forward 40)
  (penup)
  (forward 80)
  (left 90)
  (forward 40)
  (pendown)
  (left 90)
  (circle 40 180)
  (left 90)
  (penup)
  (forward 10)
  (left 90)
  (forward 40)
  (color "blue")
  (pendown)
  (forward 10)
  (penup)
  (forward 10)
  (pendown)
  (forward 10)
  (penup)
  (forward 10)
  (pendown)
  (forward 10)
  (penup)
  (forward 10)
  (pendown)
  (forward 10)
  (right 90)
  (penup)
  (forward 60)
  (right 90)
  (pendown)
  (forward 10)
  (penup)
  (forward 10)
  (pendown)
  (forward 10)
  (penup)
  (forward 10)
  (pendown)
  (forward 10)
  (penup)
  (forward 10)
  (pendown)
  (forward 10)
  (penup)
  (forward 10)
  (left 180)
  (penup)
  (forward 30)
  (right 90)
  (forward 70)
  (pendown)
  (left 90)
  (color "yellow")
  (circle 100)`
  (exitonclick))

; Please leave this last line alone.  You may add additional procedures above
; this line.
(draw)
