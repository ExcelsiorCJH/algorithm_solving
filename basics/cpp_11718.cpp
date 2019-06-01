// https://www.acmicpc.net/problem/11718
#include <iostream>
using namespace std;

int main(){

    char s[101];

    while ( scanf("%[^\n]\n", s) == 1) 
        printf("%s\n", s);
    return 0;
}