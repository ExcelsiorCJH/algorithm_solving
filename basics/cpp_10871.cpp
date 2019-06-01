// https://www.acmicpc.net/problem/10871
#include <iostream>
using namespace std;

int main(){

    int n, n_max;
    scanf("%d %d", &n, &n_max);

    for (int i=0; i<n; ++i){
        int x;
        scanf("%d", &x);
        if (x < n_max)
            cout << x << " ";
    }

    return 0;
}