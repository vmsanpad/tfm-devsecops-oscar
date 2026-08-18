package main

import (
	"crypto/rand"
	"fmt"
	"math/big"
)

func main() {
	// Corrección: Generador criptográficamente seguro
	limite := big.NewInt(10000)
	n, err := rand.Int(rand.Reader, limite)
	if err != nil {
		fmt.Println("Error generando número:", err)
		return
	}

	fmt.Printf("Token seguro generado: %d\n", n)
}
