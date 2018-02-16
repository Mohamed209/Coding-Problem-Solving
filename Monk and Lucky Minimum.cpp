#Problem : https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/monk-and-lucky-minimum-3/
# Solution:
#include <iostream>
#include <cstdlib>
#include <string>
#include <math.h>

using namespace std;
int main(int argc, char** argv) {
    unsigned int T;
    cin>>T;
    unsigned long int occ=0;
    for(unsigned int i=0;i<T;i++)
    {
        unsigned long int N;
        cin>>N;
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
        //compute minimum occurance
        for(long int k=0;k<N;k++)
        {
         if(a[k]==min){occ++;}   
        }
        if(occ%2==0){cout<<"Unlucky"<<endl;}
        else {cout<<"Lucky"<<endl;}
        occ=0;
    }
    return 0;
    }
