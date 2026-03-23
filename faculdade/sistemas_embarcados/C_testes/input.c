#include <stdio.h>

int main() {
  int input;
  printf("Digite um numero:\n>>");
  scanf("%d", &input);

  printf("Voce digitou: %d\n", input);
  printf("Que foi armazenado em: %p\n", &input);

  return 0;
}
