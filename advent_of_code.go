package main

import (
	"fmt"
	"os"
	"strconv"

	"github.com/isinek/aoc/days"
)

func printHelp() {
	fmt.Println("go run advent_of_code.go [-d day] [-t task]")
	fmt.Println("    -d day  - day has values 1-12")
	fmt.Println("    -t task - task has values 1 or 2")
	fmt.Println("For other info check: https://adventofcode.com/")
}

func main() {
	args := os.Args[1:]

	for _, v := range args {
		if v == "-h" {
			printHelp()
			os.Exit(0)
		}
	}

	var runDays []int
	var runTasks []int

	for i, v := range args {
		switch v {
		case "-d":
			if i+1 > len(args)-1 {
				printHelp()
				os.Exit(1)
			}

			day, err := strconv.Atoi(args[i+1])
			if err != nil || day < 1 || day > 12 {
				printHelp()
				os.Exit(1)
			}

			runDays = append(runDays, day)
		case "-t":
			if i+1 > len(args)-1 {
				printHelp()
				os.Exit(1)
			}

			task, err := strconv.Atoi(args[i+1])
			if err != nil || task < 1 || task > 2 {
				printHelp()
				os.Exit(1)
			}

			runTasks = append(runTasks, task)
		}
	}
	if len(runDays) == 0 {
		for i := 1; i <= 12; i++ {
			runDays = append(runDays, i)
		}
	}
	if len(runTasks) == 0 {
		runTasks = []int{1, 2}
	}

	for _, d := range runDays {
		var dayMap map[int]func()
		var ok bool

		if dayMap, ok = days.Solutions[d]; !ok {
			fmt.Printf("Solutions for day %d do not exist\n", d)
			os.Exit(0)
		}

		for _, t := range runTasks {
			fmt.Printf("Day %d task %d - ", d, t)

			if fn, ok := dayMap[t]; ok {
				fn()
				continue
			}

			fmt.Println("Solution does not exist!")
			os.Exit(2)
		}
	}
}
