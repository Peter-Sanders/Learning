package main

import (
  "os"
  "log"
  "bufio"
  "fmt"
  "unicode"
  "strconv"
)

func main () {
  file, err := os.Open("../../advent-storage/advent-23-1.txt")
  if err != nil {
    log.Fatal(err)
  }
  defer file.Close()

  var result int 
  result = 0

  scanner := bufio.NewScanner(file)
  for scanner.Scan(){
    var s []string
    for _, char := range scanner.Text(){
      // fmt.Printf("%c\n", char)
      if unicode.IsDigit(char){
        s = append(s, string(char))
      }
    }
    calibration := s[0] + s[len(s)-1]
    cal_int, _ := strconv.Atoi(calibration)
    result += cal_int 
  }
  fmt.Println(result)
  if err := scanner.Err(); err != nil {
    log.Fatal(err)
  }
}

