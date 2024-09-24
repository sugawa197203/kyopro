#include <iostream>
#include <vector>
#include <stdio.h>

int _1, _2, _3, _4;
int indexbuf;

bool iszero()
{
	return _1 == 0 && _2 == 0 && _3 == 0 && _4 == 0;
}

int getmin()
{
	int min = 101;
	if (_1 <= min)
	{
		if (_1)
		{
			min = _1;
			indexbuf = 1;
		}
	}

	if (_2 <= min)
	{
		if (_2)
		{
			min = _2;
			indexbuf = 2;
		}
	}

	if (_3 < min)
	{
		if (_3)
		{
			min = _3;
			indexbuf = 3;
		}
	}

	if (_4 < min)
	{
		if (_4)
		{
			min = _4;
			indexbuf = 4;
		}
	}

	return min;
}

int getend()
{
	int nozeroindex = 0;
	int zerocount = 0;
	if (_1 == 0)
	{
		zerocount++;
	}
	else
	{
		nozeroindex = 1;
	}
	if (_2 == 0)
	{
		zerocount++;
	}
	else
	{

		nozeroindex = 2;
	}
	if (_3 == 0)
	{
		zerocount++;
	}
	else
	{

		nozeroindex = 3;
	}
	if (_4 == 0)
	{
		zerocount++;
	}
	else
	{

		nozeroindex = 4;
	}

	if (zerocount != 3)
	{
		return 0;
	}

	return nozeroindex;
}

int getnumfromindex(int index)
{
	switch (index)
	{
	case 1:
		return _1;
	case 2:
		return _2;
	case 3:
		return _3;
	case 4:
		return _4;
	default:
		return -1;
	}
}

int main()
{
	while (std::cin >> _1 >> _2 >> _3 >> _4)
	{
		if (iszero())
			break;

		int i;

		// fprintf(stderr, "DEGUB >> %d %d %d %d\n", _1, _2, _3, _4);

		while (!(i = getend()))
		{
			int m = getmin();

			if (indexbuf != 1 && _1)
			{
				_1 -= m;
			}
			if (indexbuf != 2 && _2)
			{
				_2 -= m;
			}
			if (indexbuf != 3 && _3)
			{
				_3 -= m;
			}
			if (indexbuf != 4 && _4)
			{
				_4 -= m;
			}
			// fprintf(stderr, "DEGUB >> %d %d %d %d MIN >> %d INDEX >> %d\n", _1, _2, _3, _4, m, indexbuf);
		}

		std::cout << getnumfromindex(i) << std::endl;
	}
}