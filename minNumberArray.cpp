#include <bits/stdc++.h>
#include <algorithm>

using namespace std;

typedef vector<int> vi;
#define EL printf("\n")
#define FOR(i, l, r) for (int i = l; i < r; i++)
#define FOD(i, r, l) for (int i = r; i >= l; i--)

int minNumberArray(vector<int> a){
	int d[a.size() + 1];
		
	FOR(i, 0, a.size()) {
		d[i] = 0;	
	}
		
 	FOR(i, 0, a.size()) {
		if (a[i] < a.size()) {
			d[a[i]]++;
		}
	}
		
	FOR(i, 0, a.size()) {
		if (d[i] == 0) {
			return i;
		}
	}
	
	return a[a.size() - 1] + 1;
}


int main() {
	printf("%ld", minNumberArray(vi({4,8,3,2,9})));
	return 0;	
}



