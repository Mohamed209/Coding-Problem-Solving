# Problem : https://www.hackerearth.com/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/practice-problems/algorithm/monk-and-the-box-of-cookies/
#Solution:
#include <iostream>
#include <cstdlib>

using namespace std;

int main(int argc, char** argv) {
    int t,N,b;
    int p=0;
    cin>>t;
    int record[32];//record for every position
    for(int i=0;i<t;i++)
    {
        for(int x=0;x<31;x++){record[x]=0;}//intialize records
        cin>>N;
        for(int j=0;j<N;j++)
        {
         cin>>b;
         for(int k=0;k<31;k++)
         {
             if(b&(1<<k)){record[k]++;}//if position k has set bit , increment its record
         }
        }
        int max=record[0];
        for(int x=0;x<31;x++)
        {
            if(max<record[x]){max=record[x];p=x;}//find most occurring position has set bit
        }
        cout<<p<<endl;
    }
    return 0;
}
