package main

import (
	"fmt"
	"os"
)

var Usage = func() {
	fmt.Println("Usage: calc command [arguments] ...")

}

func main() {
	args := os.Args
	if args == nil || len(args) <= 2 {
		Usage()
		return
	}
}
