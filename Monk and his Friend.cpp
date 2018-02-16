#problem:https://www.hackerearth.com/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/practice-problems/algorithm/monk-and-his-friend/
#Solution:
#include <iostream>
#include <cstdlib>
#include <string>
#include <math.h>

using namespace std;

int main(int argc, char** argv) {
    long int N,P;
    long int XOR;
    int counter=0;
    int t;
    cin>>t;// test cases
    for(int i=0;i<t;i++)
    {
        cin>>N>>P;
        XOR=N^P;        
        for(int i=0;i<=31;i++)
        {
            if(XOR&(1<<i)){counter++;}
        }
        cout<<counter<<endl;
        counter=0;
    }
    return 0;
}
