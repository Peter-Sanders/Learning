       IDENTIFICATION DIVISION.
       PROGRAM-ID. Advent-24-1.

       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
           SELECT CALIBRATION-FILE 
           ASSIGN TO '../advent-storage/advent-23-1.txt'
           ORGANIZATION IS LINE SEQUENTIAL.

       DATA DIVISION.
       FILE SECTION.
           FD CALIBRATION-FILE.
           01 CALIBRATION-RECORD PIC X(1000).

       WORKING-STORAGE SECTION.
       01 FIRST-NUMERIC-CHARACTER-POSITION PIC 9.
       01 LAST-NUMERIC-CHARACTER-POSITION PIC 9.
       01 FIRST-DIGIT PIC 9.
       01 LAST-DIGIT PIC 9.
       01 CALIBRATION-VALUE PIC 99.
       01 TOTAL-SUM PIC 9(6).
       01 FILE-STATUS PIC XX.
       01 WS-EOF PIC A(1).
       01 CHAR-COUNTER-START PIC 9.
       01 CHAR-COUNTER-END PIC 9.
       01 CHAR-COUNTER PIC 9.
       01 FOUND-FIRST-DIGIT PIC X VALUE 'N'.
       01 FOUND-LAST-DIGIT PIC X VALUE 'N'.





       PROCEDURE DIVISION.
           OPEN INPUT CALIBRATION-FILE
       IF FILE-STATUS = '00'
           DISPLAY 'Error opening file: ' FILE-STATUS
           STOP RUN
       END-IF.
    
       PERFORM READ-CALIBRATION-RECORD UNTIL WS-EOF = 'Y'.
    
       CLOSE CALIBRATION-FILE.
    
       DISPLAY 'Total sum of calibration values: ' TOTAL-SUM
       STOP RUN.

       READ-CALIBRATION-RECORD.
           DISPLAY CALIBRATION-RECORD
           READ CALIBRATION-FILE INTO CALIBRATION-RECORD
               AT END MOVE 'Y' TO WS-EOF
               NOT AT END
                   CONTINUE
           END-READ.



         SET CHAR-COUNTER TO 1
    PERFORM UNTIL CHAR-COUNTER > LENGTH OF CALIBRATION-RECORD
        IF NOT FOUND-FIRST-DIGIT AND CALIBRATION-RECORD(CHAR-COUNTER:1) NUMERIC
            MOVE CALIBRATION-RECORD(CHAR-COUNTER:1) TO FIRST-DIGIT
            MOVE 'Y' TO FOUND-FIRST-DIGIT
        END-IF
        IF CALIBRATION-RECORD(CHAR-COUNTER:1) NUMERIC
            MOVE CALIBRATION-RECORD(CHAR-COUNTER:1) TO LAST-DIGIT
        END-IF
        ADD 1 TO CHAR-COUNTER
    END-PERFORM
    
    COMPUTE CALIBRATION-VALUE = FUNCTION NUMVAL(FIRST-DIGIT) + FUNCTION NUMVAL(LAST-DIGIT)
           ADD CALIBRATION-VALUE TO TOTAL-SUM.

