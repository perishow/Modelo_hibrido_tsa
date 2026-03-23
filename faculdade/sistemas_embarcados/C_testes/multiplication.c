#include <stdint.h>
#include <stdio.h>

uint16_t multiply_by_seven(uint8_t num) {
	return (num << 3) - num;
}

int main() {
	uint16_t catorze = multiply_by_seven(2);
	printf("%u\n", catorze);
	
	return 0;
}
