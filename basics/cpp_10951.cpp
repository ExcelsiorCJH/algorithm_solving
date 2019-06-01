// https://www.acmicpc.net/problem/10951
#include <iostream>
using namespace std;

int main(){

    int a, b;

    while( scanf("%d %d", &a, &b) == 2){
        int sum = a + b;
        printf("%d\n", sum);
    }
    return 0;
}