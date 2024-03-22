package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func get_file (f string) (*bufio.Scanner, *os.File){
  file, err := os.Open(f)
  if err != nil {
    log.Fatal(err)
  }
  scanner := bufio.NewScanner(file)

  return scanner, file
}


func main() {
  const maxred int = 12 
  const maxgreen int = 13
  const maxblue int = 14

  fn := "../../advent-storage/advent-23-2.txt"
  scanner, file := get_file(fn)
  defer file.Close()

  var res int = 0
  for scanner.Scan(){
    s := strings.Split(scanner.Text(), ":")
    game_id := strings.Split(s[0], " ")[1]
    game_data := strings.Split(strings.Trim(s[1], " "), ";")
    var redcount int = 0
    var greencount int = 0
    var bluecount int = 0
    var ispossible bool = true

    for i :=0; i < len(game_data); i++{
      color_data := strings.Split(game_data[i], ",")
      for j := 0; j <len(color_data); j++{
        final_data := strings.Split(strings.TrimSpace(color_data[j]), " ")
        count, _ := strconv.Atoi(strings.TrimSpace(final_data[0]))
        color := strings.TrimSpace(final_data[1])

        switch c :=color; c {
        case "red":
          redcount += count 
          if redcount > maxred {
            ispossible =false
            break
          }
        case "green":
          greencount += count 
          if greencount > maxgreen {
            ispossible =false
            break
          }
        case "blue":
          bluecount += count
          if bluecount > maxblue {
            ispossible =false
            break
          }
        }
      }
    }
    if ispossible {
      game_int, _ := strconv.Atoi(game_id)
      res += game_int
    }
  }
  fmt.Printf("Result: %d\n", res)
}

