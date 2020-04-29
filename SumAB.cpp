#include <bits/stdc++.h>

using namespace std;

#define EL printf("\n")
#define FOR(i, l, r) for (int i = l; i <= r; i++)
#define FOD(i, r, l) for (int i = r; i >= l; i--)

long long int sumAB(long long a, long long b) {	
	if (a > b) {
		return 0;
	}
	
	long long n = b - a;
	
	return (n + 1) * (2 * a + n) / 2;
}


int main() {
	printf("%ld", sumAB(1, 10e9));
	return 0;	
}

