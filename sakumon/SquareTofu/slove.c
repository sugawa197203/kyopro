#include <stdio.h>
#include <stdlib.h>

int main()
{
	unsigned int a, b;
	ldiv_t qr;
	unsigned int ans = 0;
	scanf("%d %d", &a, &b);

	while (b)
	{
		qr = ldiv(a, b);
		ans += qr.quot;
		a = b;
		b = qr.rem;
	}
	printf("%d", ans);
}
