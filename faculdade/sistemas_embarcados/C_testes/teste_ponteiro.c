#include <stdio.h>
#include <stdint.h>

int main() {
  volatile uint32_t endereco_simulado = 67;
  
  volatile uint32_t *ponteiro = &endereco_simulado;

  printf("Endereço de memoria: %p\n", ponteiro);
  printf("Valor armazenado: %u\n", *ponteiro);

  return 0;
}
