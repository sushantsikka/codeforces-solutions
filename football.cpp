// Football
// http://codeforces.com/problemset/problem/96/A

#include<iostream>
#include<string.h>
using namespace std;

typedef long long val;

int main()
{
    string input;
    getline(cin,input);
    int len=input.size();
    int x=0;
    for(int i=1;i<len;i++)
    {
        if(input[i]==input[i-1])
        {
            x++;
        }
        else if(input[i]!=input[i-1] && x<7)
        {
            x=0;
        }
    }
    if(x>6)
    {
        cout<<"YES";
    }
    else
    {
        cout<<"NO";
    }
    
    return 0;
}
