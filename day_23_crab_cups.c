#include <stdlib.h>
#include <stdio.h>

typedef struct cup {
	uint32_t val;
	uint32_t prev_i;
	uint32_t next_i;
} Cup;

int main()
{
	uint32_t i, mark = 0;
	Cup cups[1000000] = { 	{ 6, 1000000, 1 },
				{ 8, 0, 2 },
				{ 5, 1, 3 },
				{ 9, 2, 4 },
				{ 7, 3, 5 },
				{ 4, 4, 6 },
				{ 2, 5, 7 },
				{ 1, 6, 8 },
				{ 3, 7, 9 }, };
	for(i = 10; i <= 1000000; ++i)
		cups[i - 1] = { i, i-2, i%1000000 };

	printf("%d", mark);

	return 0;
}