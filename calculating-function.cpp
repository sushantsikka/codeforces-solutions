#include <iostream>
#include<math.h>

using namespace std;

int main() {
    int n = 0, sum = 0;
    cin>>n;
    
    for(int i = 1; i < n+1; i++)
    {
        sum += pow(-1, i) * i;
    }
    cout<<sum;
}
