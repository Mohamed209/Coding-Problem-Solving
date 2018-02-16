# problem :https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/the-great-kian/
# Solution:
#include <iostream>
#include <cstdlib>
#include <string>
#include <math.h>

using namespace std;

int main(int argc, char** argv) {
    long long int n;
    cin>>n;
    long long int a[n];
    long long int s1=0;
    long long int s2=0;
    long long int s3=0;
    for(int i=0;i<n;i++)
    {
        cin>>a[i];
    }
    for(int j=0;j<n;j+=3)
    {
        s1+=a[j];
    }
    cout<<s1<<" ";
    for(int j=1;j<n;j+=3)
    {
        s2+=a[j];
    }
    cout<<s2<<" ";
    for(int j=2;j<n;j+=3)
    {
        s3+=a[j];
    }
    cout<<s3;
    return 0;
}
