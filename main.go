package main

import (
	"fmt"
	"math/rand"
	"os/exec"
)

func main() {
	// Fallo 1: Generador pseudoaleatorio débil para seguridad (G404)
	tokenInseguro := rand.Intn(10000)
	fmt.Printf("Token generado: %d\n", tokenInseguro)

	// Fallo 2: Ejecución de comando del sistema sin sanitizar (G204)
	cmd := exec.Command("sh", "-c", "echo test")
	_ = cmd.Run()
}
