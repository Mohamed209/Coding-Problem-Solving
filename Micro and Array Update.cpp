#problem :https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/micro-and-array-update/
#Solution:
#include <iostream>
#include <cstdlib>
#include <string>
#include <math.h>

using namespace std;
int main(int argc, char** argv) {
    unsigned int T;
    cin>>T;
    for(unsigned int i=0;i<T;i++)
    {
        unsigned long int N,K;
        cin>>N>>K;
        unsigned long int a[N];
        for(long int j=0;j<N;j++)
        {
            cin>>a[j];
        }
        unsigned long int min=a[0];
        for(long int l=0;l<N;l++)
        {
            if(a[l]<min){min=a[l];}
        }
        if(K>min){cout<<K-min<<endl;}
        else {cout<<0<<endl;}
    }
    return 0;
}
